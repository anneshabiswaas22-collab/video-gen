/** Public v1 mock-mode API types. Keep aligned with services/api/contracts.py. */
export type JobState = "QUEUED" | "RUNNING" | "SUCCEEDED" | "FAILED";
export interface Project { id: string; name: string; created_at: string }
export interface ModelDefinition {
  id: string; name: string; version: string; engine: "mock";
  capabilities: string[]; is_mock: true; requires_gpu: false;
}
export interface GenerationJob {
  id: string; project_id: string; model_id: string; prompt: string;
  state: JobState; progress: number; workflow_version: string;
  is_mock: true; artifact_id: string | null; error_code: string | null;
  created_at: string; updated_at: string;
}
export interface GenerationArtifact {
  id: string; job_id: string; project_id: string; model_id: string;
  mime_type: string; bytes: number; sha256: string;
  workflow_version: string; created_at: string;
  is_mock: true; download_url: string;
}
export interface ApiFailure {
  error?: { code: string; message: string };
  detail?: { code: string; message: string };
}
