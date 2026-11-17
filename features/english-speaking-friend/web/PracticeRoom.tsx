"use client";

import Link from "next/link";
import { useEffect, useRef, useState, useSyncExternalStore } from "react";
import { createSession, deleteAllSessions, deleteSession, listSavedSessions, loadScenarios, readSession, submitTurn } from "./api";
import type { PracticeSession, PracticeTurn, ScenarioCatalog } from "./types";
import "./practice.css";

const kindLabels: Record<PracticeTurn["kind"], string> = {
  correction: "A natural way to say it",
  translation: "Your meaning in English",
  accepted: "That phrase works here",
  clarification: "Let's check the meaning",
  unsupported: "Outside this practice set",
};

function subscribeToSpeechSupport() { return () => undefined; }
function speechSupported() {
  return typeof window !== "undefined" && "speechSynthesis" in window && "SpeechSynthesisUtterance" in window;
}

function Portrait({ character, speaking }: { character: "mira" | "arun"; speaking: boolean }) {
  return <svg viewBox="0 0 280 270" className={speaking ? "pr-portrait pr-speaking" : "pr-portrait"}
    role="img" aria-label={`${character === "mira" ? "Mira" : "Arun"}, an original illustrated practice character`}>
    <circle cx="140" cy="122" r="102" fill="#dce9dd" />
    <path d="M40 270c0-66 39-101 100-101s100 35 100 101" fill={character === "mira" ? "#406f64" : "#637e94"} />
    {character === "mira" && <path d="M75 116c-7-60 19-90 66-90 48 0 74 40 62 98l13 75H65z" fill="#3f3531" />}
    <path d="M121 161h38v34c-8 15-29 15-38 0z" fill="#bd8768" />
    <ellipse cx="140" cy="112" rx="56" ry="67" fill="#d9a17b" />
    {character === "mira" ? <path d="M83 104c-8-48 18-73 57-73 43 0 63 29 57 73-18-11-30-27-39-43-20 22-45 35-75 43" fill="#3f3531" />
      : <path d="M85 89c-8-46 26-65 64-61 38 4 55 26 48 64-17-8-28-17-34-29-24 16-49 23-78 26" fill="#42352e" />}
    <path d="M109 110q10-6 20 0m24 0q10-6 20 0" stroke="#4d3c34" strokeWidth="3" strokeLinecap="round" fill="none" />
    <circle cx="120" cy="119" r="3" fill="#3c332e" /><circle cx="162" cy="119" r="3" fill="#3c332e" />
    <path d="M141 124l-4 14h7" stroke="#ad7459" strokeWidth="2.5" strokeLinecap="round" fill="none" />
    <path className="pr-mouth" d="M124 151q17 16 34-1" stroke="#814f42" strokeWidth="3.5" strokeLinecap="round" fill="none" />
    <path d="M109 194l31 25 31-25" stroke="#f3eee2" strokeWidth="5" fill="none" />
  </svg>;
}

export default function PracticeRoom() {
  const [catalog, setCatalog] = useState<ScenarioCatalog | null>(null);
  const [scenarioId, setScenarioId] = useState("everyday");
  const [character, setCharacter] = useState<"mira" | "arun">("mira");
  const [session, setSession] = useState<PracticeSession | null>(null);
  const [turns, setTurns] = useState<PracticeTurn[]>([]);
  const [saveHistory, setSaveHistory] = useState(false);
  const [savedSessions, setSavedSessions] = useState<PracticeSession[]>([]);
  const [savedId, setSavedId] = useState("");
  const [savedError, setSavedError] = useState("");
  const [text, setText] = useState("");
  const [busy, setBusy] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [reload, setReload] = useState(0);
  const canSpeak = useSyncExternalStore(subscribeToSpeechSupport, speechSupported, () => false);
  const [speaking, setSpeaking] = useState(false);
  const inputRef = useRef<HTMLTextAreaElement>(null);
  const requestRef = useRef<AbortController | null>(null);
  const epoch = useRef(0);
  const replay = useRef<{ text: string; session: string; key: string } | null>(null);

  useEffect(() => {
    const controller = new AbortController();
    loadScenarios(controller.signal).then(async (data) => {
      setCatalog(data);
      setError("");
      try {
        // The scenario response initializes the ownership cookie before this request.
        const saved = await listSavedSessions(controller.signal);
        if (!controller.signal.aborted) {
          setSavedSessions(saved.sessions);
          setSavedId((current) => saved.sessions.some((item) => item.id === current) ? current : saved.sessions[0]?.id || "");
          setSavedError("");
        }
      } catch {
        if (!controller.signal.aborted) setSavedError("Saved sessions could not be listed. You can still practise without saving.");
      }
      if (!controller.signal.aborted) setLoading(false);
    }).catch((e: Error) => {
      if (!controller.signal.aborted) {
        setError(e.message || "The local practice API is unavailable.");
        setLoading(false);
      }
    });
    return () => controller.abort();
  }, [reload]);

  useEffect(() => {
    return () => {
      epoch.current += 1;
      requestRef.current?.abort();
      if ("speechSynthesis" in window) window.speechSynthesis.cancel();
    };
  }, []);

  const scenario = catalog?.scenarios.find((item) => item.id === scenarioId);
  const lastTurn = turns[turns.length - 1];
  const isLocalModel = catalog?.provider.mode === "ollama";

  function stopSpeaking() {
    if (canSpeak) window.speechSynthesis.cancel();
    setSpeaking(false);
  }

  function speak(phrase: string) {
    if (!canSpeak) return;
    stopSpeaking();
    const utterance = new SpeechSynthesisUtterance(phrase);
    utterance.lang = "en-US";
    utterance.rate = 0.9;
    utterance.onstart = () => setSpeaking(true);
    utterance.onend = () => setSpeaking(false);
    utterance.onerror = () => { setSpeaking(false); setError("Speech playback is unavailable on this device. You can keep practising with text."); };
    window.speechSynthesis.speak(utterance);
  }

  function choosePhrase(phrase: string) {
    setText(phrase);
    inputRef.current?.focus();
  }

  function changeScenario(value: string) {
    if (session || busy) return;
    epoch.current += 1;
    requestRef.current?.abort();
    stopSpeaking();
    setScenarioId(value);
    setText("");
    setTurns([]);
    setError("");
    replay.current = null;
  }

  async function send(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const original = text.trim();
    if (busy || !original || !scenario) return;
    const currentEpoch = epoch.current;
    const controller = new AbortController();
    requestRef.current?.abort();
    requestRef.current = controller;
    setBusy(true);
    setError("");
    stopSpeaking();
    try {
      let active = session;
      if (!active) {
        active = await createSession(scenarioId, saveHistory, controller.signal);
        if (controller.signal.aborted || currentEpoch !== epoch.current) return;
        setSession(active);
        if (active.save_history) {
          const created = active;
          setSavedSessions((items) => [created, ...items.filter((item) => item.id !== created.id)]);
          setSavedId(created.id);
        }
      }
      const activeId = active.id;
      const prior = replay.current;
      const idempotencyKey = prior?.text === original && prior.session === activeId ? prior.key : crypto.randomUUID();
      replay.current = { text: original, session: activeId, key: idempotencyKey };
      const turn = await submitTurn(activeId, original, idempotencyKey, controller.signal);
      if (controller.signal.aborted || currentEpoch !== epoch.current) return;
      setTurns((items) => items.some((item) => item.id === turn.id) ? items : [...items, turn]);
      setSession((item) => item ? { ...item, turn_count: item.turn_count + 1 } : item);
      setSavedSessions((items) => items.map((item) => item.id === activeId ? { ...item, turn_count: item.turn_count + 1 } : item));
      setText("");
      replay.current = null;
      inputRef.current?.focus();
    } catch (e) {
      if (!controller.signal.aborted && currentEpoch === epoch.current) {
        setError((e as Error).message || "Your phrase could not be sent. Please try again.");
      }
    } finally {
      if (currentEpoch === epoch.current) setBusy(false);
    }
  }

  async function forgetSession() {
    if (!session || busy) return;
    const currentEpoch = ++epoch.current;
    requestRef.current?.abort();
    const controller = new AbortController();
    requestRef.current = controller;
    setBusy(true);
    setError("");
    stopSpeaking();
    try {
      await deleteSession(session.id, controller.signal);
      if (controller.signal.aborted || currentEpoch !== epoch.current) return;
      setSession(null);
      setSavedSessions((items) => items.filter((item) => item.id !== session.id));
      setSavedId((current) => current === session.id ? "" : current);
      setTurns([]);
      setText("");
      replay.current = null;
    } catch (e) {
      if (!controller.signal.aborted && currentEpoch === epoch.current) setError((e as Error).message || "Deletion could not be confirmed. Please try again.");
    } finally {
      if (currentEpoch === epoch.current) setBusy(false);
    }
  }

  async function forgetAllSessions() {
    if (busy || !catalog || !window.confirm("Delete all your saved and unsaved practice sessions on this server? This cannot be undone.")) return;
    const currentEpoch = ++epoch.current;
    requestRef.current?.abort();
    const controller = new AbortController();
    requestRef.current = controller;
    stopSpeaking(); setBusy(true); setError("");
    try {
      await deleteAllSessions(controller.signal);
      if (controller.signal.aborted || currentEpoch !== epoch.current) return;
      setSession(null); setTurns([]); setSavedSessions([]); setSavedId("");
      setText(""); setSaveHistory(false); replay.current = null;
    } catch (error) {
      if (!controller.signal.aborted && currentEpoch === epoch.current) setError((error as Error).message);
    } finally {
      if (currentEpoch === epoch.current) setBusy(false);
    }
  }

  async function resumeSession() {
    if (!savedId || busy) return;
    const currentEpoch = ++epoch.current;
    requestRef.current?.abort();
    const controller = new AbortController();
    requestRef.current = controller;
    setBusy(true);
    setError("");
    stopSpeaking();
    try {
      const restored = await readSession(savedId, controller.signal);
      if (controller.signal.aborted || currentEpoch !== epoch.current) return;
      if (!restored.save_history) throw new Error("Only sessions you opted to save can be resumed here.");
      setSession(restored);
      setScenarioId(restored.scenario_id);
      setSaveHistory(true);
      setTurns(restored.turns);
      setText("");
      replay.current = null;
    } catch (e) {
      if (!controller.signal.aborted && currentEpoch === epoch.current) setError((e as Error).message || "This saved session could not be resumed.");
    } finally {
      if (currentEpoch === epoch.current) setBusy(false);
    }
  }

  return <div className="practice-room">
    <a className="pr-skip" href="#practice-input">Skip to your phrase</a>
    <aside className="pr-sidebar">
      <Link href="/" className="pr-brand"><span aria-hidden="true">✳</span> VideoGen<span className="pr-brand-light"> / learn</span></Link>
      <div className="pr-nav-heading">YOUR WORKSPACE</div>
      <Link href="/" className="pr-nav-link"><span aria-hidden="true">▦</span> Creative studio <span aria-hidden="true">↗</span></Link>
      <div className="pr-nav-current" aria-current="page"><span aria-hidden="true">◌</span> English friend <span className="pr-tiny-tag">T0</span></div>
      <section className="pr-scenario-panel" aria-labelledby="pr-scenario-title">
        <h2 id="pr-scenario-title">A little practice, every day.</h2>
        <p>Choose a situation you would like to try.</p>
        <label htmlFor="pr-scenario">Practice scenario</label>
        <select id="pr-scenario" value={scenarioId} onChange={(e) => changeScenario(e.target.value)} disabled={loading || busy || !!session}>
          {!catalog && <option value="everyday">Loading scenarios…</option>}
          {catalog?.scenarios.map((item) => <option value={item.id} key={item.id}>{item.title}</option>)}
        </select>
        {session && <p className="pr-small">Delete this session to change your scenario or storage preference.</p>}
        <div className="pr-scenario-description">{scenario?.description}</div>
      </section>
      <div className="pr-sidebar-bottom"><span className="pr-dot" /> PRIVATE LOCAL PROTOTYPE
        <p>Your camera and microphone are off. No recording is collected by this screen.</p>
      </div>
    </aside>

    <main className="pr-main">
      <header className="pr-topbar"><span>Learning space <span aria-hidden="true">/</span> <strong>English friend</strong></span>
        <span className="pr-mode">{isLocalModel ? (catalog?.provider.configured ? "Local model configured" : "Local model not configured") : catalog?.provider.mode === "unavailable" ? "Provider unavailable" : "Offline phrase practice"}</span>
      </header>
      <div className="pr-page">
        <div className="pr-intro"><p className="pr-eyebrow">A SPACE TO FIND YOUR WORDS</p>
          <h1>Say it your way.<br /><span>Let’s practise together.</span></h1>
          <p>Try English or a listed Bangla phrase. Get a gentle suggestion, then give it another go.</p>
        </div>
        <div className="pr-honesty"><span aria-hidden="true">ⓘ</span><div>
          <strong>{catalog?.provider.label || "A small first step toward your AI speaking friend"}</strong>
          <p>{isLocalModel ? (catalog?.provider.configured ? "Configuration does not guarantee the model is available. Responses are AI suggestions and can be wrong." : "A local model is selected but needs server configuration before it can respond.") : "This mode matches a small set of authored phrases. It is not general AI conversation, grammar assessment or translation."} Examples still need independent educator review.</p>
        </div></div>

        <div className="pr-workspace">
          <section className="pr-partner" aria-labelledby="pr-partner-title">
            <div className="pr-partner-top"><span className="pr-tiny-tag">ILLUSTRATED CHARACTER</span><span className="pr-camera-off">Camera off</span></div>
            <div className="pr-portrait-wrap"><Portrait character={character} speaking={speaking} /></div>
            <h2 id="pr-partner-title">{character === "mira" ? "Mira" : "Arun"}</h2>
            <p className="pr-partner-caption">Your practice character, not a live person.</p>
            <div className="pr-character-options" aria-label="Choose an illustrated character">
              <button type="button" aria-pressed={character === "mira"} onClick={() => setCharacter("mira")}>Mira</button>
              <button type="button" aria-pressed={character === "arun"} onClick={() => setCharacter("arun")}>Arun</button>
            </div>
            <div className="pr-partner-note"><span aria-hidden="true">✧</span><p>You can pause, edit, or try again.<br />There’s no rush here.</p></div>
            <button type="button" className="pr-mic" disabled title="Microphone integration is planned for a later milestone">◉ &nbsp; Microphone coming later</button>
            <p className="pr-small pr-center">Text practice is available now. Live video is not implemented.</p>
          </section>

          <section className="pr-conversation" aria-labelledby="pr-conversation-title">
            <div className="pr-conversation-heading"><div><p className="pr-eyebrow">01 / PRACTISE</p><h2 id="pr-conversation-title">{scenario?.title || "Your conversation"}</h2></div><span>{turns.length} {turns.length === 1 ? "turn" : "turns"}</span></div>
            {!turns.length && <div className="pr-welcome"><span className="pr-welcome-mark" aria-hidden="true">“</span>
              <p>{scenario?.starter || "The local practice service will load your scenarios here."}</p>
              <span>Choose a phrase below, or type a sentence to try.</span>
            </div>}
            <div className="pr-turns" role="log" aria-label="Practice responses" aria-live="polite" aria-relevant="additions">
              {turns.map((turn) => <article key={turn.id} className={`pr-turn pr-turn-${turn.kind}`}>
                <div className="pr-your-words"><span>YOUR WORDS</span><p>{turn.original}</p></div>
                <div className="pr-feedback"><div className="pr-feedback-title"><span aria-hidden="true">{turn.kind === "accepted" ? "✓" : turn.kind === "unsupported" ? "↪" : "✧"}</span><strong>{kindLabels[turn.kind]}</strong><small>{turn.engine === "ollama" ? "LOCAL AI" : "PHRASE SET"}</small></div>
                  <p>{turn.reply}</p>
                  {turn.suggestions.map((suggestion) => <div className="pr-suggestion" key={suggestion}><blockquote>{suggestion}</blockquote><button type="button" disabled={busy} onClick={() => choosePhrase(suggestion)} aria-label={`Try: ${suggestion}`}>Try this phrase <span aria-hidden="true">↗</span></button></div>)}
                  {turn.explanation && <details><summary>Why this wording?</summary><p>{turn.explanation}</p></details>}
                  {turn.next_question && <p className="pr-next-question">{turn.next_question}</p>}
                  <div className="pr-feedback-actions"><button type="button" className="pr-text-button" disabled={!canSpeak} onClick={() => speak(turn.suggestions[0] || turn.reply)}>▷ Play English</button>
                    {speaking && <button type="button" className="pr-text-button" onClick={stopSpeaking}>Stop playback</button>}
                  </div>
                </div>
              </article>)}
            </div>
            {error && <div role="alert" className="pr-error"><strong>We couldn’t complete that.</strong><p>{error}</p>
              {!catalog && <button type="button" onClick={() => { setLoading(true); setReload((n) => n + 1); }}>Reconnect to practice service</button>}
            </div>}
            {busy && <p role="status" className="pr-working">Working on your phrase…</p>}
            <form onSubmit={send} className="pr-composer">
              <label htmlFor="practice-input">What would you like to say?</label>
              <textarea id="practice-input" ref={inputRef} value={text} maxLength={1000} rows={3} disabled={loading || busy || !catalog}
                onChange={(e) => setText(e.target.value)} placeholder="Try: Yesterday I go market. Or choose a Bangla example below." />
              <div className="pr-compose-bottom"><span>{text.length}/1000 · edit before sending</span><button className="pr-send" disabled={!text.trim() || busy || loading || !catalog} type="submit">{busy ? "Sending…" : "Send phrase"} <span aria-hidden="true">→</span></button></div>
            </form>
            <div className="pr-audio-note">{canSpeak ? "Optional playback uses your browser’s speech service; voices and processing depend on your device. Nothing plays automatically." : "Speech playback is unavailable in this browser. All practice feedback is readable as text."}</div>
            {lastTurn?.kind === "unsupported" && <p className="pr-fallback">Try one of the listed examples. Unknown text has not been assessed or marked wrong.</p>}
          </section>
        </div>

        <section className="pr-examples" aria-labelledby="pr-examples-title"><div><p className="pr-eyebrow">02 / EXPLORE A PHRASE</p><h2 id="pr-examples-title">A little inspiration</h2><p>These examples are supported in this scenario. Click one to edit it before sending.</p></div>
          <div className="pr-example-buttons">{scenario?.example_inputs.map((phrase) => <button type="button" key={phrase} disabled={busy} onClick={() => choosePhrase(phrase)}>{phrase}<span aria-hidden="true">↗</span></button>)}</div>
        </section>
        <section className="pr-privacy" aria-labelledby="pr-privacy-title"><div><h2 id="pr-privacy-title">Your practice, your choice.</h2>
          <label className="pr-checkbox"><input type="checkbox" checked={saveHistory} disabled={!!session || busy} onChange={(e) => setSaveHistory(e.target.checked)} /><span>Save this session’s phrases in the local database</span></label>
          <p>{saveHistory ? "Saving is opt-in. Your phrases and replies are saved on this server. Sessions expire after 7 days; expired records are removed on the next service startup or session request." : "By default, the service processes your phrase without saving a transcript. Session metadata expires after 24 hours; reloading loses on-page text."} This is a local prototype, not a private production account.</p>
          {session && <span className="pr-session-id">Session: {session.id}</span>}
        </div><button type="button" className="pr-delete" onClick={() => void forgetSession()} disabled={!session || busy}>Delete this session</button></section>
        <section className="pr-saved" aria-labelledby="pr-saved-title"><div><h2 id="pr-saved-title">Pick up where you left off</h2><p>Only sessions you chose to save are listed for this browser. Resuming replaces unsaved on-page practice; it does not delete other saved sessions.</p></div>
          {savedSessions.length > 0 ? <div className="pr-saved-controls"><label htmlFor="pr-saved-session">Saved session</label><select id="pr-saved-session" value={savedId} disabled={busy} onChange={(e) => setSavedId(e.target.value)}>
            <option value="">Choose a saved session</option>
            {savedSessions.map((item) => <option value={item.id} key={item.id}>{catalog?.scenarios.find((entry) => entry.id === item.scenario_id)?.title || item.scenario_id} · {new Date(item.created_at).toLocaleString()} · {item.turn_count} {item.turn_count === 1 ? "turn" : "turns"}</option>)}
          </select><button type="button" onClick={() => void resumeSession()} disabled={!savedId || busy}>Resume session</button></div> : <p className="pr-small">No saved sessions in this browser yet.</p>}
          {savedError && <p role="status" className="pr-small">{savedError}</p>}
          <div><button type="button" className="pr-delete" disabled={busy || !catalog} onClick={() => void forgetAllSessions()}>Delete all practice data</button>
            <p className="pr-small">Also clears default-session metadata left after closing a page. Only this browser’s practice data is affected.</p></div>
        </section>
        <footer className="pr-footer"><span>Small steps. Clearer conversations.</span><span>English + listed Bangla examples · T0 prototype</span></footer>
      </div>
    </main>
  </div>;
}
