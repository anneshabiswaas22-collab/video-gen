/**
 * Real cross-stack integration: Node browser-compatible fetch -> running FastAPI.
 * NO mocked responses and NO inference; tests UI client job/receipt expectations.
 * Run while Python API is listening on loopback.
 */
import assert from "node:assert/strict";
import { randomUUID, createHash } from "node:crypto";

const origin = process.env.VIDEOGEN_TEST_API_URL ?? "http://127.0.0.1:8000";

async function request(path, init) {
  const response = await fetch(origin + path, {
    ...init,
    headers: { "Content-Type": "application/json", ...init?.headers },
  });
  const data = await response.json();
  assert.ok(response.ok, `${path}: HTTP ${response.status}: ${JSON.stringify(data)}`);
  return data;
}

const health = await request("/v1/health");
assert.equal(health.mode, "mock");
assert.equal(health.inference_enabled, false);

const models = await request("/v1/models");
assert.equal(models.length, 1);
assert.equal(models[0].is_mock, true);

const project = await request("/v1/projects", {
  method: "POST",
  body: JSON.stringify({ name: "HTTP integration test " + randomUUID() }),
});
const payload = {
  project_id: project.id,
  model_id: models[0].id,
  prompt: "An amber sky over a mountain ridge",
  idempotency_key: randomUUID(),
};
const job = await request("/v1/jobs", { method: "POST", body: JSON.stringify(payload) });
const replay = await request("/v1/jobs", { method: "POST", body: JSON.stringify(payload) });
assert.equal(job.id, replay.id, "same idempotency key must return same job");

let terminal;
for (let i = 0; i < 60; ++i) {
  const status = await request(`/v1/jobs/${job.id}`);
  if (status.state === "SUCCEEDED" || status.state === "FAILED") {
    terminal = status;
    break;
  }
  await new Promise((resolve) => setTimeout(resolve, 60));
}
assert.ok(terminal, "job must terminate");
assert.equal(terminal.state, "SUCCEEDED");
assert.equal(terminal.is_mock, true);
const artifact = await request(`/v1/artifacts/${terminal.artifact_id}`);
const download = await fetch(origin + artifact.download_url);
assert.equal(download.status, 200);
const body = Buffer.from(await download.arrayBuffer());
assert.match(body.toString("utf8"), /MOCK ARTIFACT — NOT AI-GENERATED/);
assert.equal(createHash("sha256").update(body).digest("hex"), artifact.sha256);
const history = await request(`/v1/projects/${project.id}/jobs`);
assert.equal(history.length, 1);
assert.equal(history[0].id, job.id);
console.log("PASS: JS client -> FastAPI -> SQLite -> CPU worker -> verified mock artifact");
