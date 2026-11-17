"""Provider contracts use local mocked HTTP; no AI model or external service runs."""

import json
import os
import unittest
from unittest.mock import patch

import httpx
from english_friend.providers import ProviderUnavailable, provider_info, respond

_LOCAL = {
    "VIDEOGEN_COACH_PROVIDER": "ollama",
    "OLLAMA_MODEL": "owner-selected-model:example",
    "OLLAMA_BASE_URL": "http://127.0.0.1:11434",
}
_CORRECTION = {
    "kind": "correction", "suggestions": ["I went to the market yesterday."],
    "explanation": "Use a past-tense verb for yesterday.",
    "reply": "What did you buy?", "next_question": "Would you like to try again?",
    "supported": True,
}


def _envelope(value=None):
    return {"done": True, "message": {"role": "assistant", "content": json.dumps(value or _CORRECTION)}}


class ProviderTests(unittest.IsolatedAsyncioTestCase):
    async def test_default_is_honest_offline_practice_and_makes_no_http_request(self):
        def unexpected(request):
            self.fail("Offline mode must not contact a provider")
        with patch.dict(os.environ, {}, clear=True):
            async with httpx.AsyncClient(transport=httpx.MockTransport(unexpected), trust_env=False) as client:
                reply = await respond("unknown private phrase", client=client)
            self.assertEqual(reply["engine"], "offline_practice")
            self.assertEqual(reply["kind"], "unsupported")
            self.assertEqual(reply["suggestions"], [])
            self.assertIn("finite authored", " ".join(provider_info()["limitations"]))

    async def test_actual_ollama_request_separates_user_input_and_validates_output(self):
        seen = []
        def handler(request):
            seen.append(request)
            self.assertEqual(str(request.url), "http://127.0.0.1:11434/api/chat")
            payload = json.loads(request.content)
            self.assertEqual(payload["model"], _LOCAL["OLLAMA_MODEL"])
            self.assertIs(payload["stream"], False)
            self.assertEqual(payload["messages"][1], {"role": "user", "content": "Yesterday I go market."})
            self.assertNotIn("Yesterday I go market.", payload["messages"][0]["content"])
            self.assertIn("additionalProperties", payload["format"])
            self.assertIs(payload["format"]["additionalProperties"], False)
            self.assertNotIn("tools", payload)
            return httpx.Response(200, json=_envelope())
        with patch.dict(os.environ, _LOCAL, clear=True):
            async with httpx.AsyncClient(transport=httpx.MockTransport(handler), trust_env=False) as client:
                result = await respond("Yesterday I go market.", client=client)
        self.assertEqual(len(seen), 1)
        self.assertEqual(result, {**_CORRECTION, "engine": "ollama"})

    async def test_configuration_status_does_not_claim_model_readiness(self):
        with patch.dict(os.environ, _LOCAL, clear=True):
            result = provider_info()
        self.assertEqual(result["mode"], "ollama")
        self.assertTrue(result["configured"])
        self.assertIn("not verified", " ".join(result["limitations"]))
        self.assertNotIn("ready", result)

    async def test_no_missing_model_or_unknown_provider_fallback(self):
        for config in [{"VIDEOGEN_COACH_PROVIDER": "ollama"}, {"VIDEOGEN_COACH_PROVIDER": "typo"}]:
            with self.subTest(config=config), patch.dict(os.environ, config, clear=True):
                with self.assertRaises(ProviderUnavailable) as caught:
                    await respond("Yesterday I go market.")
                self.assertEqual(caught.exception.code, "PROVIDER_CONFIG_INVALID")
                self.assertFalse(provider_info()["configured"])

    async def test_rejects_remote_or_ambiguous_url_configuration_before_http(self):
        invalid = [
            "http://example.com:11434", "http://192.168.0.1:11434", "https://localhost:11434",
            "http://localhost.evil.test:11434", "http://user:password@127.0.0.1:11434",
            "http://127.0.0.1:11434/path", "http://127.0.0.1:11434?api_key=secret",
            "http://127.0.0.1:11434/#fragment", "http://127.0.0.1:0",
            "http://127.0.0.1:65536", "http://[::1%25eth0]:11434", " http://127.0.0.1:11434",
        ]
        for url in invalid:
            with self.subTest(url=url), patch.dict(os.environ, {**_LOCAL, "OLLAMA_BASE_URL": url}, clear=True):
                with self.assertRaises(ProviderUnavailable) as caught:
                    await respond("private learner sentence")
                self.assertEqual(caught.exception.code, "PROVIDER_CONFIG_INVALID")
                self.assertNotIn("secret", str(caught.exception))
                self.assertNotIn("private learner sentence", str(caught.exception))

    async def test_localhost_and_ipv6_loopback_are_supported(self):
        for url in ["http://localhost:11434/", "http://[::1]:11434"]:
            seen = []
            def handler(request):
                seen.append(request.url)
                return httpx.Response(200, json=_envelope())
            with self.subTest(url=url), patch.dict(os.environ, {**_LOCAL, "OLLAMA_BASE_URL": url}, clear=True):
                async with httpx.AsyncClient(transport=httpx.MockTransport(handler), trust_env=False) as client:
                    result = await respond("Yesterday I go market.", client=client)
                self.assertEqual(result["engine"], "ollama")
                self.assertEqual(seen[0].path, "/api/chat")

    async def test_redirects_are_never_followed_even_if_client_default_follows(self):
        seen = []
        def handler(request):
            seen.append(str(request.url))
            return httpx.Response(302, headers={"Location": "https://untrusted.example/private"})
        with patch.dict(os.environ, _LOCAL, clear=True):
            async with httpx.AsyncClient(transport=httpx.MockTransport(handler), trust_env=False, follow_redirects=True) as client:
                with self.assertRaises(ProviderUnavailable) as caught:
                    await respond("private learner phrase", client=client)
            self.assertEqual(caught.exception.code, "PROVIDER_REDIRECT_REFUSED")
            self.assertEqual(seen, ["http://127.0.0.1:11434/api/chat"])

    async def test_environment_proxy_clients_are_refused(self):
        with patch.dict(os.environ, _LOCAL, clear=True):
            async with httpx.AsyncClient(transport=httpx.MockTransport(lambda r: httpx.Response(200)), trust_env=True) as client:
                with self.assertRaises(ProviderUnavailable) as caught:
                    await respond("private learner phrase", client=client)
            self.assertEqual(caught.exception.code, "PROVIDER_CLIENT_UNSAFE")

    async def test_transport_errors_are_safe_and_never_become_offline_results(self):
        for error_type, code in [(httpx.ReadTimeout, "PROVIDER_TIMEOUT"), (httpx.ConnectError, "PROVIDER_CONNECTION_FAILED")]:
            def handler(request):
                raise error_type("private infrastructure detail", request=request)
            with self.subTest(code=code), patch.dict(os.environ, _LOCAL, clear=True):
                async with httpx.AsyncClient(transport=httpx.MockTransport(handler), trust_env=False) as client:
                    with self.assertRaises(ProviderUnavailable) as caught:
                        await respond("private learner phrase", client=client)
                self.assertEqual(caught.exception.code, code)
                self.assertNotIn("private", str(caught.exception))

    async def test_unsuccessful_http_status_does_not_expose_provider_body(self):
        with patch.dict(os.environ, _LOCAL, clear=True):
            async with httpx.AsyncClient(transport=httpx.MockTransport(lambda r: httpx.Response(500, text="private server body")), trust_env=False) as client:
                with self.assertRaises(ProviderUnavailable) as caught:
                    await respond("Yesterday I go market.", client=client)
            self.assertEqual(caught.exception.code, "PROVIDER_HTTP_ERROR")
            self.assertNotIn("private", str(caught.exception))

    async def test_untrusted_structured_output_is_rejected(self):
        invalid = [
            {**_CORRECTION, "extra": "not permitted"},
            {**_CORRECTION, "engine": "pretend_verified"},
            {**_CORRECTION, "kind": ["correction"]},
            {**_CORRECTION, "supported": 1},
            {**_CORRECTION, "suggestions": ["one"] * 4},
            {**_CORRECTION, "suggestions": [" "]},
            {**_CORRECTION, "suggestions": ["x" * 501]},
            {**_CORRECTION, "reply": "x" * 1501},
            {**_CORRECTION, "reply": "<script>alert('x')</script>"},
            {**_CORRECTION, "kind": "clarification"},
            {**_CORRECTION, "kind": "unsupported", "suggestions": [], "supported": True},
            {**_CORRECTION, "suggestions": []},
        ]
        for output in invalid:
            with self.subTest(output=output), patch.dict(os.environ, _LOCAL, clear=True):
                async with httpx.AsyncClient(transport=httpx.MockTransport(lambda r: httpx.Response(200, json=_envelope(output))), trust_env=False) as client:
                    with self.assertRaises(ProviderUnavailable) as caught:
                        await respond("Yesterday I go market.", client=client)
                self.assertEqual(caught.exception.code, "PROVIDER_OUTPUT_INVALID")

    async def test_malformed_or_oversized_envelopes_are_rejected(self):
        responses = [
            {"json": {"done": False, "message": {"content": json.dumps(_CORRECTION)}}},
            {"json": {"message": {"content": "not JSON"}}},
            {"json": {"message": {"content": json.dumps(_CORRECTION), "tool_calls": [{"function": "bad"}]}}},
            {"json": {"message": {"content": 1}}},
            {"content": b"not JSON"},
            {"content": b"x" * 65537},
        ]
        for response in responses:
            with self.subTest(response=response.keys()), patch.dict(os.environ, _LOCAL, clear=True):
                async with httpx.AsyncClient(transport=httpx.MockTransport(lambda r: httpx.Response(200, **response)), trust_env=False) as client:
                    with self.assertRaises(ProviderUnavailable) as caught:
                        await respond("Yesterday I go market.", client=client)
                self.assertEqual(caught.exception.code, "PROVIDER_OUTPUT_INVALID")

    async def test_valid_clarification_and_unsupported_do_not_invent_corrections(self):
        for kind in ["clarification", "unsupported", "accepted"]:
            output = {**_CORRECTION, "kind": kind, "suggestions": [], "supported": kind != "unsupported"}
            with self.subTest(kind=kind), patch.dict(os.environ, _LOCAL, clear=True):
                async with httpx.AsyncClient(transport=httpx.MockTransport(lambda r: httpx.Response(200, json=_envelope(output))), trust_env=False) as client:
                    result = await respond("My intended meaning is unclear", client=client)
            self.assertEqual(result["kind"], kind)
            self.assertEqual(result["suggestions"], [])

    async def test_input_and_scenario_are_bounded_before_any_provider_request(self):
        with patch.dict(os.environ, _LOCAL, clear=True):
            for text in [None, "", "  ", "x" * 2001]:
                with self.subTest(text_type=type(text).__name__), self.assertRaises(ValueError):
                    await respond(text)
            with self.assertRaises(ValueError):
                await respond("a sentence", "not-a-scenario")


if __name__ == "__main__":
    unittest.main()
