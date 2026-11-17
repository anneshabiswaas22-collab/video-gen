"""Real browser -> Next.js -> FastAPI -> SQLite/worker integration.

Run against an isolated local data directory, never a shared/user database.
Browser speech availability is inspected, not an assertion that audio was heard.
"""
import os
from pathlib import Path
from uuid import uuid4

from playwright.sync_api import expect, sync_playwright


def main():
    base = os.environ.get("VIDEOGEN_TEST_WEB_URL", "http://127.0.0.1:3000")
    api = os.environ.get("VIDEOGEN_TEST_API_URL", "http://127.0.0.1:8001")
    executable = os.environ.get("VIDEOGEN_BROWSER_EXECUTABLE")
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True, executable_path=executable, args=["--no-sandbox"]
        )
        context = browser.new_context(viewport={"width": 1440, "height": 1000})
        page = context.new_page()
        page_errors = []
        page.on("pageerror", lambda error: page_errors.append(str(error)))
        page.goto(base + "/practice")
        send = page.get_by_role("button", name="Send phrase")
        phrase = page.get_by_label("What would you like to say?")
        expect(page.get_by_role("button", name="Yesterday I go market.")).to_be_enabled()
        expect(send).to_be_disabled()
        phrase.fill("Yesterday I go market.")
        send.click()
        expect(page.locator(".pr-turn-correction")).to_have_count(1)
        expect(page.locator(".pr-suggestion blockquote")).to_have_text("I went to the market yesterday.")
        page.get_by_role("button", name="Try: I went to the market yesterday.").click()
        send.click()
        expect(page.locator(".pr-turn-accepted")).to_have_count(1)
        phrase.fill("আমি ইংরেজিতে কথা বলতে চাই।")
        send.click()
        expect(page.locator(".pr-turn-translation")).to_have_count(1)
        phrase.fill('<img src=x onerror="alert(1)">')
        send.click()
        expect(page.locator(".pr-turn-unsupported")).to_have_count(1)
        expect(page.locator(".pr-your-words img")).to_have_count(0)
        expect(page.locator(".pr-fallback")).to_contain_text("has not been assessed")
        session_id = page.locator(".pr-session-id").inner_text().split(": ")[1]
        removed = context.request.delete(api + "/v1/english/sessions/" + session_id)
        assert removed.status == 204
        # Clearing an already deleted session must unlock the practice room.
        page.get_by_role("button", name="Delete this session", exact=True).click()
        expect(page.locator(".pr-turn")).to_have_count(0)
        expect(page.get_by_label("Practice scenario")).to_be_enabled()
        page.get_by_label("Practice scenario").select_option("work")
        page.get_by_label("Save this session’s phrases in the local database").check()
        phrase.fill("I have a meeting in Monday.")
        send.click()
        expect(page.locator(".pr-turn-correction")).to_have_count(1)
        page.reload()
        expect(page.get_by_role("button", name="Resume session", exact=True)).to_be_enabled()
        page.get_by_role("button", name="Resume session", exact=True).click()
        expect(page.locator(".pr-turn-correction")).to_have_count(1)
        expect(page.get_by_label("What would you like to say?")).to_have_value("")
        page.get_by_role("button", name="Delete this session", exact=True).click()
        page.reload()
        expect(page.get_by_text("No saved sessions in this browser yet.", exact=True)).to_be_visible()
        # No camera/microphone permissions or raw transcript storage in the browser.
        assert page.evaluate("Object.keys(localStorage)") == []
        page.set_viewport_size({"width": 390, "height": 844})
        assert page.evaluate("document.documentElement.scrollWidth <= window.innerWidth")
        output = Path(os.environ.get("VIDEOGEN_BROWSER_OUTPUT", ".local/browser"))
        output.mkdir(parents=True, exist_ok=True)
        page.screenshot(path=str(output / "practice-mobile.png"), full_page=True)
        # Recovered creative pipeline is real HTTP/SQLite, with an explicit mock artifact.
        page.set_viewport_size({"width": 1440, "height": 1000})
        page.goto(base + "/")
        page.get_by_label("New project name").fill("Browser proof " + uuid4().hex[:8])
        page.get_by_role("button", name="Create project", exact=True).click()
        page.get_by_label("Describe your idea").fill("A mountain sunrise — browser smoke")
        page.get_by_role("button", name="Run mock generation").click()
        expect(page.locator(".result-id b")).to_have_text("SUCCEEDED", timeout=15000)
        expect(page.locator(".preview pre")).to_contain_text("NOT AI-GENERATED")
        with page.expect_download() as download_event:
            page.get_by_role("link", name="Download mock receipt").click()
        download = download_event.value
        download.save_as(str(output / "mock-receipt.txt"))
        assert (output / "mock-receipt.txt").read_text().startswith("MOCK ARTIFACT")
        page.get_by_role("link", name="English friend").click()
        expect(page.get_by_role("heading", name="Say it your way.")).to_be_visible()
        page.screenshot(path=str(output / "practice-desktop.png"), full_page=True)
        assert not page_errors, page_errors
        print("BROWSER SMOKE PASSED: correction/retry/Bangla/unknown text/saved resume/delete/mobile/mock receipt/navigation.")
        print("Screenshots:", output)
        context.close()
        browser.close()


if __name__ == "__main__":
    main()
