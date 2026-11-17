import { API_URL } from "../../../apps/web/lib/api";
import type { PracticeSession, PracticeTurn, SavedSessionCatalog, ScenarioCatalog } from "./types";


function record(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}
function string(value: unknown, max: number, empty = true): value is string {
  return typeof value === "string" && value.length <= max && (empty || value.length > 0);
}
function array(value: unknown, max: number): value is unknown[] {
  return Array.isArray(value) && value.length <= max;
}
function validTurn(value: unknown): value is PracticeTurn {
  if (!record(value)) return false;
  const kind = value.kind;
  return string(value.id, 100, false) && string(value.session_id, 100, false)
    && string(value.original, 1000, false) && string(value.created_at, 100, false)
    && typeof kind === "string" && ["correction", "translation", "accepted", "clarification", "unsupported"].includes(kind)
    && array(value.suggestions, 3) && value.suggestions.every((s) => string(s, 500, false))
    && string(value.explanation, 1500) && string(value.reply, 1500, false)
    && string(value.next_question, 500) && ["offline_practice", "ollama"].includes(String(value.engine))
    && typeof value.supported === "boolean" && value.supported === (kind !== "unsupported")
    && (["correction", "translation"].includes(kind) ? value.suggestions.length > 0 : value.suggestions.length === 0);
}
function validSession(value: unknown): value is PracticeSession {
  return record(value) && string(value.id, 100, false) && string(value.scenario_id, 80, false)
    && typeof value.save_history === "boolean" && string(value.created_at, 100, false)
    && typeof value.turn_count === "number" && Number.isInteger(value.turn_count)
    && value.turn_count >= 0 && value.turn_count <= 50
    && array(value.turns, 50) && value.turns.every(validTurn);
}
function invalidResponse(): never {
  throw new PracticeApiError("The practice service returned an invalid response. Please reconnect or try again.", 502, "RESPONSE_INVALID");
}
function checkedSession(value: unknown): PracticeSession {
  if (!validSession(value)) return invalidResponse();
  return value;
}

async function request<T>(path: string, init: RequestInit = {}): Promise<T> {
  const response = await fetch(`${API_URL}/v1/english${path}`, {
    ...init,
    credentials: "include",
    cache: "no-store",
    headers: {
      ...(init.body ? { "Content-Type": "application/json" } : {}),
      ...init.headers,
    },
  });
  if (response.status === 204 && response.ok) return undefined as T;
  let data;
  try {
    data = await response.json();
  } catch {
    throw new Error("The practice service returned an unreadable response. Please try again.");
  }
  if (!response.ok) {
    const message = data?.error?.message || data?.detail?.message;
    const code = data?.error?.code || data?.detail?.code;
    throw new PracticeApiError(
      typeof message === "string" ? message : "The practice request could not be completed. Please try again.",
      response.status, typeof code === "string" ? code : undefined,
    );
  }
  return data as T;
}

export async function loadScenarios(signal?: AbortSignal): Promise<ScenarioCatalog> {
  const value = await request<unknown>("/scenarios", { signal });
  if (!record(value) || !array(value.scenarios, 20) || !value.scenarios.length
    || !value.scenarios.every((item) => record(item) && string(item.id, 80, false)
      && string(item.title, 200, false) && string(item.description, 2000)
      && string(item.starter, 2000) && array(item.example_inputs, 50)
      && item.example_inputs.every((entry) => string(entry, 1000, false)))
    || !record(value.provider) || !string(value.provider.mode, 80, false)
    || typeof value.provider.configured !== "boolean" || !string(value.provider.label, 300, false)
    || !(string(value.provider.limitations, 4000) || (array(value.provider.limitations, 20)
      && value.provider.limitations.every((entry) => string(entry, 1000))))) return invalidResponse();
  return value as unknown as ScenarioCatalog;
}

export async function createSession(scenarioId: string, saveHistory: boolean, signal?: AbortSignal): Promise<PracticeSession> {
  return checkedSession(await request("/sessions", {
    method: "POST", body: JSON.stringify({ scenario_id: scenarioId, save_history: saveHistory }), signal,
  }));
}

export async function readSession(sessionId: string, signal?: AbortSignal): Promise<PracticeSession> {
  return checkedSession(await request(`/sessions/${encodeURIComponent(sessionId)}`, { signal }));
}

export async function listSavedSessions(signal?: AbortSignal): Promise<SavedSessionCatalog> {
  const value = await request<unknown>("/sessions", { signal });
  if (!record(value) || !array(value.sessions, 10)
    || !value.sessions.every((item) => validSession(item) && item.save_history && item.turns.length === 0)) return invalidResponse();
  return value as unknown as SavedSessionCatalog;
}

export async function submitTurn(sessionId: string, text: string, idempotencyKey: string, signal?: AbortSignal): Promise<PracticeTurn> {
  const value = await request<unknown>(`/sessions/${encodeURIComponent(sessionId)}/turns`, {
    method: "POST", body: JSON.stringify({ text, idempotency_key: idempotencyKey }), signal,
  });
  if (!validTurn(value) || value.session_id !== sessionId || value.original !== text.trim()) return invalidResponse();
  return value;
}

export function deleteAllSessions(signal?: AbortSignal): Promise<void> {
  return request("/sessions", { method: "DELETE", signal });
}

export async function deleteSession(sessionId: string, signal?: AbortSignal): Promise<void> {
  try {
    return await request(`/sessions/${encodeURIComponent(sessionId)}`, { method: "DELETE", signal });
  } catch (error) {
    // Another tab or expiry may have removed it already. Clear the local view.
    if (error instanceof PracticeApiError && error.status === 404) return;
    throw error;
  }
}
export class PracticeApiError extends Error {
  constructor(message: string, public status: number, public code?: string) {
    super(message);
    this.name = "PracticeApiError";
  }
}
