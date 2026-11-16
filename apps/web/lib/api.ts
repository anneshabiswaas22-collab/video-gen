import type { ApiFailure } from "../../../packages/schemas/src/types";

export const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

export async function apiRequest<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_URL}${path}`, {
    ...init,
    headers: { "Content-Type": "application/json", ...(init?.headers || {}) },
    cache: "no-store",
  });
  const data = (await response.json()) as T & ApiFailure;
  if (!response.ok) {
    throw new Error(data.error?.message || data.detail?.message || `HTTP ${response.status}`);
  }
  return data;
}

export function isTerminal(state: string): boolean {
  return state === "SUCCEEDED" || state === "FAILED";
}
