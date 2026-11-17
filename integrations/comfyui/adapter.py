"""Typed future ComfyUI boundary. Not connected to API until M1 license/GPU gate."""
import json
from dataclasses import dataclass
from enum import StrEnum
from typing import Mapping

import httpx


class AdapterErrorCode(StrEnum):
    UNAVAILABLE = "ENGINE_UNAVAILABLE"
    INVALID_WORKFLOW = "WORKFLOW_NOT_ALLOWED"
    REMOTE_REJECTED = "WORKFLOW_REJECTED"
    CANCEL_UNSUPPORTED = "CANCEL_UNSUPPORTED"


@dataclass(frozen=True)
class AdapterError(Exception):
    code: AdapterErrorCode
    message: str


@dataclass(frozen=True)
class Estimate:
    gpu_seconds: float | None
    peak_vram_gib: float | None


class ComfyUIAdapter:
    """Only allow operator-reviewed graph IDs. Never accept arbitrary public workflow JSON."""

    def __init__(self, client: httpx.AsyncClient, allowed_workflows: Mapping[str, dict]):
        self.client = client
        try:
            self.allowed_workflows = json.loads(json.dumps(dict(allowed_workflows), allow_nan=False))
            if any(not isinstance(graph, dict) or not graph for graph in self.allowed_workflows.values()):
                raise ValueError("Invalid graph")
        except (ValueError, TypeError):
            raise AdapterError(AdapterErrorCode.INVALID_WORKFLOW, "Invalid approved graph") from None

    def capabilities(self) -> list[str]:
        return ["workflow_submission"] if self.allowed_workflows else []

    async def _request(self, method: str, path: str, **kwargs):
        async with self.client.stream(method, path, follow_redirects=False, **kwargs) as response:
            response.raise_for_status()
            body = bytearray()
            async for chunk in response.aiter_bytes():
                body.extend(chunk)
                if len(body) > 256 * 1024:
                    raise ValueError("Engine response exceeded limit")
        return json.loads(body)

    async def health(self) -> bool:
        try:
            result = await self._request("GET", "/queue")
            return (isinstance(result, dict) and isinstance(result.get("queue_running"), list)
                    and isinstance(result.get("queue_pending"), list))
        except (httpx.HTTPError, ValueError, TypeError):
            return False

    async def estimate(self, workflow_id: str) -> Estimate:
        if workflow_id not in self.allowed_workflows:
            raise AdapterError(AdapterErrorCode.INVALID_WORKFLOW, "Unapproved workflow")
        return Estimate(gpu_seconds=None, peak_vram_gib=None)

    async def generate(self, workflow_id: str, client_id: str) -> str:
        graph = self.allowed_workflows.get(workflow_id)
        if graph is None:
            raise AdapterError(AdapterErrorCode.INVALID_WORKFLOW, "Unapproved workflow")
        try:
            data = await self._request("POST", "/prompt", json={
                "prompt": graph, "client_id": client_id,
            })
        except httpx.HTTPError:
            raise AdapterError(AdapterErrorCode.UNAVAILABLE, "ComfyUI API error") from None
        except (ValueError, TypeError):
            raise AdapterError(AdapterErrorCode.REMOTE_REJECTED, "Invalid engine response") from None
        prompt_id = data.get("prompt_id") if isinstance(data, dict) else None
        if (not isinstance(prompt_id, str) or not 1 <= len(prompt_id) <= 256
                or any(ord(char) <= 32 or ord(char) == 127 for char in prompt_id)
                or data.get("error") or data.get("node_errors")):
            raise AdapterError(AdapterErrorCode.REMOTE_REJECTED, "ComfyUI refused workflow")
        return prompt_id

    async def cancel(self, _prompt_id: str) -> None:
        # /interrupt is global on some engines. Never interrupt unrelated tenants.
        raise AdapterError(AdapterErrorCode.CANCEL_UNSUPPORTED, "Safe targeted cancel pending")
