import { API_URL } from "../../../apps/web/lib/api";
import type { PracticeSession, PracticeTurn, SavedSessionCatalog, ScenarioCatalog } from "./types";

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

export function loadScenarios(signal?: AbortSignal): Promise<ScenarioCatalog> {
  return request("/scenarios", { signal });
}

export function createSession(scenarioId: string, saveHistory: boolean, signal?: AbortSignal): Promise<PracticeSession> {
  return request("/sessions", {
    method: "POST", body: JSON.stringify({ scenario_id: scenarioId, save_history: saveHistory }), signal,
  });
}

export function readSession(sessionId: string, signal?: AbortSignal): Promise<PracticeSession> {
  return request(`/sessions/${encodeURIComponent(sessionId)}`, { signal });
}

export function listSavedSessions(signal?: AbortSignal): Promise<SavedSessionCatalog> {
  return request("/sessions", { signal });
}

export function submitTurn(sessionId: string, text: string, idempotencyKey: string, signal?: AbortSignal): Promise<PracticeTurn> {
  return request(`/sessions/${encodeURIComponent(sessionId)}/turns`, {
    method: "POST", body: JSON.stringify({ text, idempotency_key: idempotencyKey }), signal,
  });
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
