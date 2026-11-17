export type CoachKind = "correction" | "translation" | "accepted" | "clarification" | "unsupported";

export interface Scenario {
  id: string;
  title: string;
  description: string;
  starter: string;
  example_inputs: string[];
}

export interface ProviderInfo {
  mode: string;
  configured: boolean;
  label: string;
  limitations: string | string[];
}

export interface PracticeTurn {
  id: string;
  session_id: string;
  original: string;
  kind: CoachKind;
  suggestions: string[];
  explanation: string;
  reply: string;
  next_question: string;
  engine: "offline_practice" | "ollama";
  supported: boolean;
  created_at: string;
}

export interface PracticeSession {
  id: string;
  scenario_id: string;
  save_history: boolean;
  created_at: string;
  turn_count: number;
  turns: PracticeTurn[];
}

export interface ScenarioCatalog {
  scenarios: Scenario[];
  provider: ProviderInfo;
}

export interface SavedSessionCatalog {
  sessions: PracticeSession[];
}
