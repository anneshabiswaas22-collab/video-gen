"""Typed future ComfyUI boundary. Not connected to API until M1 license/GPU gate."""
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
        self.allowed_workflows = dict(allowed_workflows)

    def capabilities(self) -> list[str]:
        return ["workflow_submission"] if self.allowed_workflows else []

    async def health(self) -> bool:
        try:
            result = await self.client.get("/queue")
            return result.status_code == 200
        except httpx.HTTPError:
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
            response = await self.client.post("/prompt", json={
                "prompt": graph,
                "client_id": client_id,
            })
            response.raise_for_status()
            data = response.json()
        except (httpx.HTTPError, ValueError) as exc:
            raise AdapterError(AdapterErrorCode.UNAVAILABLE, "ComfyUI API error") from exc
        if not isinstance(data, dict) or not isinstance(data.get("prompt_id"), str):
            raise AdapterError(AdapterErrorCode.REMOTE_REJECTED, "ComfyUI refused workflow")
        return data["prompt_id"]

    async def cancel(self, _prompt_id: str) -> None:
        # /interrupt is global on some engines. Never interrupt unrelated tenants.
        raise AdapterError(AdapterErrorCode.CANCEL_UNSUPPORTED, "Safe targeted cancel pending")
