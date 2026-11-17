"""Executable CPU-only local worker. Outputs are mock receipts, never AI-generated media."""
import asyncio
import logging
import sqlite3

from services.api import storage


async def execute_one(delay: float = 0.05) -> bool:
    task = storage.claim_job()
    if task is None:
        return False
    try:
        await asyncio.sleep(delay)
        storage.progress_job(task["id"], 70)
        if task["simulate_failure"]:
            raise RuntimeError("deliberate mock failure")
        await asyncio.sleep(delay)
        # Deliberately not HTML, SVG, PNG or MP4: nobody can confuse this with inference.
        body = (
            "MOCK ARTIFACT — NOT AI-GENERATED IMAGE OR VIDEO\n"
            f"Job: {task['id']}\n"
            f"Model: {task['model_id']}\n"
            f"Workflow: {storage.WORKFLOW_VERSION}\n"
            f"Prompt: {task['prompt']}\n"
        ).encode("utf-8")
        storage.complete_job(task, body)
    except asyncio.CancelledError:
        storage.fail_job(task["id"], "WORKER_LOST")
        raise
    except Exception:
        storage.fail_job(task["id"], "MOCK_EXECUTION_FAILED")
    return True


async def worker_loop() -> None:
    while True:
        try:
            worked = await execute_one()
        except (sqlite3.Error, OSError):
            # A temporary storage fault must not permanently kill the local worker.
            logging.getLogger(__name__).warning("Mock worker storage temporarily unavailable")
            worked = False
        if not worked:
            await asyncio.sleep(0.1)


if __name__ == "__main__":
    storage.initialize()
    storage.recover_interrupted()
    print("VideoGen MOCK worker; no inference and no GPU use.", flush=True)
    try:
        asyncio.run(worker_loop())
    except KeyboardInterrupt:
        pass
