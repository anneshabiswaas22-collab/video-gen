"""Fault-injected and responsive checks against an isolated running application."""

import os
from uuid import uuid4

from playwright.sync_api import expect, sync_playwright


def main():
    base = os.environ["VIDEOGEN_TEST_WEB_URL"]
    api = os.environ["VIDEOGEN_TEST_API_URL"]
    assertions = 0
    with sync_playwright() as tool:
        browser = tool.chromium.launch(
            headless=True,
            executable_path=os.environ.get("VIDEOGEN_BROWSER_EXECUTABLE"),
            args=["--no-sandbox"],
        )
        context = browser.new_context()
        page = context.new_page()
        errors = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        # All supported scenario examples remain usable at realistic narrow widths.
        for width in [320, 390, 768, 1440]:
            page.set_viewport_size({"width": width, "height": 900})
            page.goto(base + "/practice")
            expect(page.get_by_role("button", name="Yesterday I go market.")).to_be_enabled()
            assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
            assert (
                page.get_by_label("What would you like to say?").get_attribute("maxlength")
                == "1000"
            )
            assert page.get_by_role("button", name="Microphone coming later").is_disabled()
            assert page.evaluate("Object.keys(localStorage)") == []
            assertions += 4
        # A successful malformed JSON response is rejected as data, never rendered/crashed.
        page.route(
            "**/v1/english/scenarios", lambda route: route.fulfill(json={"scenarios": [None]})
        )
        page.reload()
        expect(page.locator(".pr-error")).to_contain_text("invalid response")
        assert not errors
        page.unroute("**/v1/english/scenarios")
        page.get_by_role("button", name="Reconnect to practice service").click()
        expect(page.get_by_role("button", name="Yesterday I go market.")).to_be_enabled()
        assertions += 2
        # A lost response after server completion must replay the same key and ID.
        seen_keys = []

        def lose_once(route):
            seen_keys.append(route.request.post_data_json["idempotency_key"])
            response = route.fetch()
            if len(seen_keys) == 1:
                route.abort("connectionfailed")
            else:
                route.fulfill(response=response)

        page.route("**/v1/english/sessions/*/turns", lose_once)
        page.get_by_label("What would you like to say?").fill("Yesterday I go market.")
        page.get_by_role("button", name="Send phrase").click()
        expect(page.locator(".pr-error")).to_be_visible()
        page.get_by_role("button", name="Send phrase").click()
        expect(page.locator(".pr-turn-correction")).to_have_count(1)
        assert len(seen_keys) == 2 and seen_keys[0] == seen_keys[1]
        page.unroute("**/v1/english/sessions/*/turns")
        assertions += 2
        # Fill metadata quota after closing pages; clear-all provides real recovery.
        page.get_by_role("button", name="Delete this session", exact=True).click()
        for _ in range(10):
            created = context.request.post(
                api + "/v1/english/sessions", data={"scenario_id": "everyday"}
            )
            assert created.status == 201
        assert (
            context.request.post(
                api + "/v1/english/sessions", data={"scenario_id": "everyday"}
            ).status
            == 429
        )
        page.on("dialog", lambda dialog: dialog.accept())
        page.get_by_role("button", name="Delete all practice data").click()
        page.get_by_label("What would you like to say?").fill("I've got two brothers.")
        page.get_by_role("button", name="Send phrase").click()
        expect(page.locator(".pr-turn-accepted")).to_have_count(1)
        assertions += 2
        # A second browser owner cannot resume/delete the first owner's saved session.
        page.get_by_role("button", name="Delete this session", exact=True).click()
        page.get_by_label("Save this session’s phrases in the local database").check()
        page.get_by_label("What would you like to say?").fill("Yesterday I go market.")
        page.get_by_role("button", name="Send phrase").click()
        expect(page.locator(".pr-turn-correction")).to_have_count(1)
        sid = page.locator(".pr-session-id").inner_text().split(": ")[1]
        stranger = browser.new_context()
        stranger.request.get(api + "/v1/english/scenarios")
        assert stranger.request.get(api + "/v1/english/sessions/" + sid).status == 404
        assert stranger.request.delete(api + "/v1/english/sessions/" + sid).status == 404
        stranger.request.delete(api + "/v1/english/sessions")
        assert context.request.get(api + "/v1/english/sessions/" + sid).status == 200
        stranger.close()
        page.get_by_role("button", name="Delete all practice data").click()
        expect(page.locator(".pr-turn")).to_have_count(0)
        assertions += 4
        # Keyboard access has a functional skip target, not an unlabeled focus trap.
        page.reload()
        page.keyboard.press("Tab")
        expect(page.get_by_role("link", name="Skip to your phrase")).to_be_focused()
        page.keyboard.press("Enter")
        expect(page.get_by_label("What would you like to say?")).to_be_focused()
        assertions += 2
        # Rapid project switches must not show delayed history from another project.
        first = context.request.post(
            api + "/v1/projects", data={"name": "Race first " + uuid4().hex[:6]}
        ).json()
        second = context.request.post(
            api + "/v1/projects", data={"name": "Race second " + uuid4().hex[:6]}
        ).json()
        page.goto(base + "/")
        page.get_by_role("button", name=first["name"]).click()
        page.get_by_label("Describe your idea").fill("Only in the first project")
        page.get_by_role("button", name="Run mock generation").click()
        expect(page.locator(".result-id b")).to_have_text("SUCCEEDED", timeout=15000)
        page.get_by_role("button", name=second["name"]).click()
        expect(page.locator(".history-item")).to_have_count(0)
        expect(page.locator(".topbar")).to_contain_text(second["name"])
        assertions += 2
        assert not errors, errors
        context.close()
        browser.close()
    print(
        f"BROWSER REGRESSION PASSED: {assertions} grouped assertions, 4 viewport widths, real and intercepted HTTP flows."
    )


if __name__ == "__main__":
    main()
