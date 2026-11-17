import { afterEach, describe, expect, it, vi } from "vitest";
import { apiRequest, isTerminal } from "./api";

afterEach(() => vi.unstubAllGlobals());

describe("frontend-to-API contract", () => {
  it("requests backend models, not a static frontend fixture", async () => {
    const fetchMock = vi.fn().mockResolvedValue({
      ok: true,
      json: async () => [{ id: "mock-preview-v1", is_mock: true }],
    });
    vi.stubGlobal("fetch", fetchMock);
    const models = await apiRequest<Array<{ id: string; is_mock: boolean }>>("/v1/models");
    expect(models[0].is_mock).toBe(true);
    expect(fetchMock.mock.calls[0][0]).toMatch(/\/v1\/models$/);
  });

  it("passes backend errors to the UI", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue({
      ok: false, status: 409,
      json: async () => ({ detail: { code: "IDEMPOTENCY_CONFLICT", message: "Key conflict" } }),
    }));
    await expect(apiRequest("/v1/jobs")).rejects.toThrow("Key conflict");
  });

  it("only terminal states stop polling", () => {
    expect(isTerminal("RUNNING")).toBe(false);
    expect(isTerminal("QUEUED")).toBe(false);
    expect(isTerminal("SUCCEEDED")).toBe(true);
    expect(isTerminal("FAILED")).toBe(true);
  });
});
