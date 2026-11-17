import { afterEach, describe, expect, it, vi } from "vitest";
import { createSession, deleteSession, listSavedSessions, loadScenarios, readSession, submitTurn } from "./api";

afterEach(() => vi.unstubAllGlobals());

function reply(body: unknown, status = 200) {
  return { ok: status < 400, status, json: async () => body };
}

describe("English companion HTTP boundary", () => {
  it("loads actual server scenarios and sends the ownership cookie", async () => {
    const fetcher = vi.fn().mockResolvedValue(reply({ scenarios: [], provider: { mode: "offline_practice" } }));
    vi.stubGlobal("fetch", fetcher);
    const catalog = await loadScenarios();
    expect(catalog.provider.mode).toBe("offline_practice");
    expect(fetcher.mock.calls[0][0]).toMatch(/\/v1\/english\/scenarios$/);
    expect(fetcher.mock.calls[0][1]).toMatchObject({ credentials: "include", cache: "no-store" });
    expect(fetcher.mock.calls[0][1].headers).not.toHaveProperty("Content-Type");
  });

  it("keeps history storage explicitly false rather than enabling it implicitly", async () => {
    const fetcher = vi.fn().mockResolvedValue(reply({ id: "session1", save_history: false }));
    vi.stubGlobal("fetch", fetcher);
    await createSession("everyday", false);
    const init = fetcher.mock.calls[0][1];
    expect(init.method).toBe("POST");
    expect(JSON.parse(init.body)).toEqual({ scenario_id: "everyday", save_history: false });
    expect(init.headers["Content-Type"]).toBe("application/json");
  });

  it("preserves the provided retry key and edited original text", async () => {
    const fetcher = vi.fn().mockResolvedValue(reply({ id: "turn1" }));
    vi.stubGlobal("fetch", fetcher);
    await submitTurn("session1", "আমি ইংরেজিতে কথা বলতে চাই।", "retry-key-1");
    expect(fetcher.mock.calls[0][0]).toMatch(/\/sessions\/session1\/turns$/);
    expect(JSON.parse(fetcher.mock.calls[0][1].body)).toEqual({
      text: "আমি ইংরেজিতে কথা বলতে চাই।", idempotency_key: "retry-key-1",
    });
  });

  it("encodes session identifiers instead of creating another API path", async () => {
    const fetcher = vi.fn().mockResolvedValue(reply({ id: "unused" }));
    vi.stubGlobal("fetch", fetcher);
    await readSession("session/other?admin=1");
    expect(fetcher.mock.calls[0][0]).toMatch(/\/sessions\/session%2Fother%3Fadmin%3D1$/);
  });

  it("lists opt-in saved sessions from the server using the ownership cookie", async () => {
    const fetcher = vi.fn().mockResolvedValue(reply({ sessions: [{ id: "saved1", save_history: true, turns: [] }] }));
    vi.stubGlobal("fetch", fetcher);
    const saved = await listSavedSessions();
    expect(saved.sessions[0].id).toBe("saved1");
    expect(fetcher.mock.calls[0][0]).toMatch(/\/v1\/english\/sessions$/);
    expect(fetcher.mock.calls[0][1].credentials).toBe("include");
  });

  it("loads a chosen saved session and its stored turns only on request", async () => {
    const fetcher = vi.fn().mockResolvedValue(reply({ id: "saved1", save_history: true, turns: [{ original: "I agree." }] }));
    vi.stubGlobal("fetch", fetcher);
    const saved = await readSession("saved1");
    expect(fetcher.mock.calls[0][0]).toMatch(/\/sessions\/saved1$/);
    expect(saved.turns[0].original).toBe("I agree.");
  });

  it("accepts a successful empty deletion response", async () => {
    const readJson = vi.fn();
    const fetcher = vi.fn().mockResolvedValue({ ok: true, status: 204, json: readJson });
    vi.stubGlobal("fetch", fetcher);
    await expect(deleteSession("session1")).resolves.toBeUndefined();
    expect(fetcher.mock.calls[0][1].method).toBe("DELETE");
    expect(readJson).not.toHaveBeenCalled();
  });

  it("keeps server-side access errors visible to the interface", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue(reply({ detail: { code: "SESSION_NOT_FOUND", message: "Session not found" } }, 404)));
    await expect(readSession("someone-else")).rejects.toThrow("Session not found");
  });

  it("allows a stale session view to clear after another tab deleted it", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue(reply({ detail: { code: "SESSION_NOT_FOUND", message: "Session not found" } }, 404)));
    await expect(deleteSession("already-gone")).resolves.toBeUndefined();
  });

  it("does not turn a service failure into a successful deletion", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue(reply({ detail: { code: "UNAVAILABLE", message: "Try again" } }, 503)));
    await expect(deleteSession("still-here")).rejects.toThrow("Try again");
  });

  it("provides a useful error for a non-JSON gateway response", async () => {
    vi.stubGlobal("fetch", vi.fn().mockResolvedValue({ ok: false, status: 503, json: async () => { throw new SyntaxError("private upstream data"); } }));
    await expect(loadScenarios()).rejects.toThrow("The practice service returned an unreadable response");
  });

  it("passes cancellation to fetch instead of swallowing an aborted request", async () => {
    const controller = new AbortController();
    const fetcher = vi.fn().mockRejectedValue(new DOMException("Aborted", "AbortError"));
    vi.stubGlobal("fetch", fetcher);
    controller.abort();
    await expect(loadScenarios(controller.signal)).rejects.toMatchObject({ name: "AbortError" });
    expect(fetcher.mock.calls[0][1].signal).toBe(controller.signal);
  });
});
