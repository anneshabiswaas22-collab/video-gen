"use client";

import { useCallback, useEffect, useState } from "react";
import { apiRequest, API_URL, isTerminal } from "../lib/api";
import type {
  GenerationArtifact, GenerationJob, ModelDefinition, Project,
} from "../../../packages/schemas/src/types";

export default function Studio() {
  const [projects, setProjects] = useState<Project[]>([]);
  const [projectId, setProjectId] = useState("");
  const [projectName, setProjectName] = useState("");
  const [models, setModels] = useState<ModelDefinition[]>([]);
  const [modelId, setModelId] = useState("");
  const [prompt, setPrompt] = useState("");
  const [history, setHistory] = useState<GenerationJob[]>([]);
  const [activeId, setActiveId] = useState("");
  const [activeJob, setActiveJob] = useState<GenerationJob | null>(null);
  const [artifact, setArtifact] = useState<GenerationArtifact | null>(null);
  const [artifactText, setArtifactText] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");
  const [apiOnline, setApiOnline] = useState(false);

  useEffect(() => {
    let live = true;
    Promise.all([
      apiRequest<{ status: string; mode: string }>("/v1/health"),
      apiRequest<ModelDefinition[]>("/v1/models"),
      apiRequest<Project[]>("/v1/projects"),
    ]).then(([, m, p]) => {
      if (!live) return;
      setApiOnline(true);
      setModels(m);
      setModelId(m[0]?.id || "");
      setProjects(p);
      setProjectId(p[0]?.id || "");
    }).catch(() => {
      if (live) setError("Local API unavailable. Start the backend on port 8000.");
    });
    return () => { live = false; };
  }, []);

  const refresh = useCallback(async (id: string) => {
    if (!id) { setHistory([]); return; }
    const list = await apiRequest<GenerationJob[]>(`/v1/projects/${id}/jobs`);
    setHistory(list);
  }, []);

  useEffect(() => {
    if (!projectId) return;
    let live = true;
    apiRequest<GenerationJob[]>(`/v1/projects/${projectId}/jobs`)
      .then((items) => { if (live) setHistory(items); })
      .catch((e: Error) => { if (live) setError(e.message); });
    return () => { live = false; };
  }, [projectId]);

  useEffect(() => {
    if (!activeId) return;
    let live = true;
    const read = async () => {
      try {
        const job = await apiRequest<GenerationJob>(`/v1/jobs/${activeId}`);
        if (!live) return;
        setActiveJob(job);
        if (isTerminal(job.state)) await refresh(job.project_id);
      } catch (err) {
        if (live) setError((err as Error).message);
      }
    };
    void read();
    const timer = window.setInterval(() => { void read(); }, 700);
    return () => { live = false; window.clearInterval(timer); };
  }, [activeId, refresh]);

  useEffect(() => {
    const id = activeJob?.artifact_id;
    if (!id) return;
    let live = true;
    async function load() {
      try {
        const result = await apiRequest<GenerationArtifact>(`/v1/artifacts/${id}`);
        const text = await fetch(`${API_URL}${result.download_url}`).then((r) => {
          if (!r.ok) throw new Error("Unable to load artifact");
          return r.text();
        });
        if (live) { setArtifact(result); setArtifactText(text); }
      } catch (e) {
        if (live) setError((e as Error).message);
      }
    }
    void load();
    return () => { live = false; };
  }, [activeJob?.artifact_id]);

  async function createProject(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!projectName.trim()) return;
    setError("");
    setBusy(true);
    try {
      const created = await apiRequest<Project>("/v1/projects", {
        method: "POST", body: JSON.stringify({ name: projectName.trim() }),
      });
      setProjects((list) => [created, ...list]);
      setProjectId(created.id);
      setHistory([]);
      setActiveJob(null);
      setActiveId("");
      setArtifact(null);
      setArtifactText("");
      setProjectName("");
    } catch (e) { setError((e as Error).message); }
    finally { setBusy(false); }
  }

  async function generate(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!projectId || !modelId || !prompt.trim()) return;
    setError("");
    setBusy(true);
    try {
      const job = await apiRequest<GenerationJob>("/v1/jobs", {
        method: "POST",
        body: JSON.stringify({
          project_id: projectId, model_id: modelId, prompt: prompt.trim(),
          idempotency_key: crypto.randomUUID(),
        }),
      });
      setArtifact(null);
      setArtifactText("");
      setActiveJob(job);
      setActiveId(job.id);
      await refresh(projectId);
    } catch (e) { setError((e as Error).message); }
    finally { setBusy(false); }
  }

  const visibleArtifact = artifact?.id === activeJob?.artifact_id ? artifact : null;
  const currentProject = projects.find((p) => p.id === projectId);
  const completed = history.filter((j) => j.state === "SUCCEEDED").length;

  return (
    <div className="studio">
      <aside className="sidebar">
        <div className="brand"><span className="brand-mark">✦</span> VIDEO<span>GEN</span></div>
        <div className="version">CREATIVE STUDIO <b>M0.2</b></div>
        <div className="nav-title">WORKSPACE</div>
        <div className="nav-active">▦ <span>Generation Studio</span><small>LOCAL</small></div>
        <div className="nav-muted">◧ <span>Media Library</span><small>SOON</small></div>
        <div className="nav-muted">◫ <span>Movie Timeline</span><small>SOON</small></div>
        <div className="nav-title project-heading">PROJECTS</div>
        <form onSubmit={createProject} className="project-create">
          <input aria-label="New project name" placeholder="New project name" value={projectName}
            maxLength={100} onChange={(e) => setProjectName(e.target.value)} />
          <button disabled={busy || !projectName.trim()} title="Create project" aria-label="Create project">+</button>
        </form>
        <div className="project-list">
          {projects.map((p) => (
            <button key={p.id} className={p.id === projectId ? "project selected" : "project"}
              onClick={() => {
                setProjectId(p.id); setHistory([]); setActiveId(""); setActiveJob(null);
                setArtifact(null); setArtifactText("");
              }}><span>▣</span>{p.name}</button>
          ))}
          {!projects.length && <p className="sidebar-help">Create a project to begin.</p>}
        </div>
        <div className="sidebar-foot"><span className="status-dot" /> LOCAL DEVELOPMENT ONLY
          <p>No paid API. No real AI inference. No public deployment.</p>
        </div>
      </aside>
      <main className="content">
        <header className="topbar">
          <span>Workspace <span className="crumb">/</span> {currentProject?.name || "New project"}</span>
          <div className="top-right"><span className="mode-pill">CPU MOCK MODE</span>
            <span className={apiOnline ? "api-status good" : "api-status"}>{apiOnline ? "● API connected" : "○ API offline"}</span></div>
        </header>
        <div className="body">
          <div className="intro"><p className="eyebrow">YOUR CREATIVE WORKSPACE</p>
            <h1>Bring ideas <em>into focus.</em></h1>
            <p>Build your workflow here. This milestone validates job creation and history using mock receipts, not generated media.</p>
          </div>
          <div className="notice"><strong>DEMO ENGINE</strong> The only model available is a CPU mock. Results are plain-text verification receipts, never AI images or videos.</div>
          {error && <div role="alert" className="error"><b>Request error</b><span>{error}</span>
            <button onClick={() => setError("")}>Dismiss</button></div>}
          <div className="work-grid">
            <section className="panel generator">
              <div className="section-top"><div><p className="eyebrow">01 / CREATE</p><h2>New generation</h2></div><span className="panel-chip">MOCK</span></div>
              <form onSubmit={generate}>
                <label htmlFor="model">Execution model</label>
                <select id="model" value={modelId} onChange={(e) => setModelId(e.target.value)} disabled={!models.length}>
                  {models.length ? models.map((m) => <option key={m.id} value={m.id}>{m.name}</option>) :
                    <option value="">No model available</option>}
                </select>
                <label htmlFor="prompt">Describe your idea</label>
                <textarea id="prompt" value={prompt} maxLength={2000}
                  onChange={(e) => setPrompt(e.target.value)}
                  placeholder="For example: A quiet mountain village at sunrise, cinematic wide shot..." rows={7} />
                <div className="input-meta"><span>Prompt text is stored locally for mock execution.</span><span>{prompt.length}/2000</span></div>
                <button className="primary" type="submit" disabled={busy || !projectId || !prompt.trim() || !modelId}>
                  {busy ? "Submitting…" : "Run mock generation"} <span>→</span>
                </button>
              </form>
              <p className="helper">No video or GPU processing occurs. Create a project first if generation is disabled.</p>
            </section>
            <section className="panel output">
              <div className="section-top"><div><p className="eyebrow">02 / INSPECT</p><h2>Output &amp; progress</h2></div></div>
              {!activeJob && <div className="empty"><div className="empty-symbol">✳</div>
                <h3>Ready when you are</h3><p>Submit a mock generation to see verified status transitions, metadata and an artifact.</p></div>}
              {activeJob && <div className="result">
                <div className="result-id"><span>{activeJob.id}</span><b className={activeJob.state === "FAILED" ? "failed" : "state"}>{activeJob.state}</b></div>
                <div className="progress-wrap"><div className="progress-text"><span>Job progress</span><b>{activeJob.progress}%</b></div>
                  <div className="progress-track"><div style={{ width: `${activeJob.progress}%` }} /></div></div>
                {activeJob.error_code && <p role="alert" className="error-detail">Error: {activeJob.error_code}</p>}
                <div className="preview">
                  {visibleArtifact ? <><div className="mock-stamp">MOCK RESULT — NOT GENERATED MEDIA</div>
                    <pre>{artifactText}</pre></> :
                    <div className="pending">{isTerminal(activeJob.state) ? "No artifact for this job" : "Mock worker is processing…"}</div>}
                </div>
                {visibleArtifact && <><div className="artifact-meta"><span>text/plain · {visibleArtifact.bytes} bytes</span>
                    <span>SHA-256: {visibleArtifact.sha256.slice(0, 16)}…</span></div>
                  <a className="download" href={`${API_URL}${visibleArtifact.download_url}`}>Download mock receipt ↓</a></>}
              </div>}
            </section>
          </div>
          <section className="history-panel">
            <div className="history-heading"><div><p className="eyebrow">03 / HISTORY</p><h2>Recent jobs</h2></div>
              <div className="history-stats"><span>{history.length} total</span><span>{completed} completed</span></div></div>
            {!history.length ? <p className="empty-history">No jobs in this project yet.</p> :
              <div className="history-list">{history.map((j) =>
                <button key={j.id} className={j.id === activeId ? "history-item active" : "history-item"} onClick={() => { setArtifact(null); setArtifactText(""); setActiveId(j.id); setActiveJob(j); }}>
                  <span className="history-prompt">{j.prompt}</span><span className="history-state">{j.state}</span>
                  <span className="history-date">{new Date(j.created_at).toLocaleString()}</span><span className="history-arrow">↗</span>
                </button>)}</div>}
          </section>
        </div>
      </main>
    </div>
  );
}
