"""HTTP transport simulation without a running ComfyUI or any model downloads."""
import asyncio
import json

import httpx
import pytest

from integrations.comfyui.adapter import (
    AdapterError,
    AdapterErrorCode,
    ComfyUIAdapter,
)


def test_comfyui_contract_and_workflow_allowlist():
    seen = []

    def handler(request):
        seen.append((request.method, request.url.path))
        if request.url.path == "/queue":
            return httpx.Response(200, json={"queue_running": [], "queue_pending": []})
        payload = json.loads(request.content)
        assert payload["prompt"] == {"12": {"class_type": "MockTest", "inputs": {}}}
        return httpx.Response(200, json={"prompt_id": "comfy-id-01", "number": 0})

    async def run():
        client = httpx.AsyncClient(
            base_url="http://comfy.internal", transport=httpx.MockTransport(handler)
        )
        async with client:
            adapter = ComfyUIAdapter(
                client, {"approved-test": {"12": {"class_type": "MockTest", "inputs": {}}}}
            )
            assert adapter.capabilities() == ["workflow_submission"]
            assert await adapter.health() is True
            estimate = await adapter.estimate("approved-test")
            assert estimate.peak_vram_gib is None
            with pytest.raises(AdapterError) as forbidden:
                await adapter.generate("untrusted-workflow", "client01")
            assert forbidden.value.code == AdapterErrorCode.INVALID_WORKFLOW
            assert await adapter.generate("approved-test", "client01") == "comfy-id-01"
            with pytest.raises(AdapterError) as cancelled:
                await adapter.cancel("comfy-id-01")
            assert cancelled.value.code == AdapterErrorCode.CANCEL_UNSUPPORTED

    asyncio.run(run())
    assert seen == [("GET", "/queue"), ("POST", "/prompt")]


def test_comfyui_failure_does_not_report_success():
    async def run():
        async with httpx.AsyncClient(
            base_url="http://comfy.internal",
            transport=httpx.MockTransport(lambda _req: httpx.Response(503)),
        ) as client:
            adapter = ComfyUIAdapter(client, {"known": {"1": {"class_type": "A"}}})
            assert await adapter.health() is False
            with pytest.raises(AdapterError) as failure:
                await adapter.generate("known", "test")
            assert failure.value.code == AdapterErrorCode.UNAVAILABLE

    asyncio.run(run())
