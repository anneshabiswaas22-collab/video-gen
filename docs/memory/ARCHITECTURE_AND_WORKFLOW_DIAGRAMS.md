# VideoGen — editable architecture and process charts

**Format:** GitHub-native Mermaid diagrams (text in version control). These represent **planned boundaries** unless specifically identified as PR #8 implemented. Rendering requires a Mermaid-compatible GitHub Markdown viewer; all diagrams are also explained in captions so agents can read their text.

## Chart 1 — Product architecture (target; M0 highlighted)

```mermaid
flowchart TD
    C["Creator / browser"] --> W["Owned Next.js / React VideoGen UI"]
    W --> API["Owned FastAPI / Pydantic / OpenAPI"]
    API --> P["Projects + access policy"]
    API --> J["Durable job / idempotency / history"]
    J --> DB[("SQLite M0 / PostgreSQL later")]
    J --> M0["CPU mock executor — IMPLEMENTED in PR #8"]
    M0 --> R["text/plain MOCK receipt — NOT AI media"]
    J -. "M1+ after license/GPU checks" .-> Q["Private GPU scheduling"]
    Q --> A["Versioned ComfyUI adapter"]
    A --> G["External ComfyUI GPU inference service"]
    G --> IM["Licensed image/video checkpoints"]
    G --> V["Validate, hash and store generated artifacts"]
    V --> S[("Durable private media storage")]
    S --> E["FFmpeg media + editable shot timeline (future)"]
    E --> W
```

**Explanation:** The browser never runs arbitrary ComfyUI workflows or owns private engine tokens. At M0 the API and mock worker use SQLite and a text artifact. Future real inference is **inside a separate private boundary**, not an exposed Colab service.

## Chart 2 — CPU mock job sequence (implemented in PR #8)

```mermaid
sequenceDiagram
    participant U as Creator
    participant UI as Next.js UI
    participant API as FastAPI
    participant DB as SQLite
    participant WK as CPU mock worker
    U->>UI: Create project and write prompt
    UI->>API: POST /v1/projects
    API->>DB: Insert project
    DB-->>API: New project ID
    API-->>UI: Project
    U->>UI: Generate (mock model)
    UI->>API: POST /v1/jobs + idempotency_key
    API->>DB: Verify project and reuse-or-insert job
    DB-->>API: Stable job ID
    API-->>UI: Job QUEUED / RUNNING
    WK->>DB: Atomically claim queued job
    WK->>DB: State RUNNING and progress events
    WK->>DB: Save synthetic text receipt and SHA-256
    WK->>DB: State SUCCEEDED or FAILED
    loop While not terminal
      UI->>API: GET /v1/jobs/{id}
      API-->>UI: State, progress, artifact/error
    end
    UI->>API: GET /v1/artifacts/{id}
    API-->>UI: text/plain provenance and download link
    UI-->>U: Download clearly labeled MOCK receipt
```

**M0 guards:** same idempotency key/payload returns same job; conflicting payload returns 409. Invalid model or missing project rejected. Failure recorded; no GPU execution, paid calls or "AI image" preview.

## Chart 3 — Job state transitions by milestone

```mermaid
stateDiagram-v2
    [*] --> QUEUED
    QUEUED --> RUNNING: Mock worker claims job
    RUNNING --> SUCCEEDED: Verified mock receipt
    RUNNING --> FAILED: Execution error
    QUEUED --> FAILED: Explicit durable failure (future)
    FAILED --> [*]
    SUCCEEDED --> [*]
    state "Future GPU extension" as G {
      [*] --> RESERVING
      RESERVING --> MODEL_LOADING
      MODEL_LOADING --> INFERENCING
      INFERENCING --> OUTPUT_VALIDATING
      OUTPUT_VALIDATING --> [*]
    }
```

**Future-only extension:** use typed terminal states for timeout/cancel/lost worker and isolated retries; never claim M0 cancellation or reliable distributed exactly-once semantics.

## Chart 4 — Human-approved movie/character continuity pipeline

```mermaid
flowchart LR
    SCRIPT["Concept + versioned script"] --> DIRECTOR["AI director proposes shots"]
    DIRECTOR --> APPROVAL{"Human approves?"}
    APPROVAL -- No --> SCRIPT
    APPROVAL -- Yes --> BIBLE["Character + environment bibles"]
    BIBLE --> SHOTS["Scene graph -> versioned shots"]
    SHOTS --> KEYFRAME["Approved appearance + references"]
    KEYFRAME --> GENERATE["Licensed model generates short takes"]
    GENERATE --> QA{"Continuity / quality QA"}
    QA -- "Rejected take" --> RETAKE["Reshoot only the affected shot"]
    RETAKE --> GENERATE
    QA -- "Approved" --> TIMELINE["Editable timeline / clips / audio / subtitles"]
    TIMELINE --> RENDER["FFmpeg assemble and render"]
    RENDER --> CHECK["Decodability / sync / hashes / provenance"]
    CHECK --> MOVIE["60s measured proof -> eventually full episode/movie"]
```

**Core differentiation:** character IDs, reference versions, wardrobe/voice/environment continuity and approved-take history. Reusing a seed/prompt alone does not guarantee identity. Full movies are **shot assemblies**, not one huge model call.

## Chart 5 — Dependency-ordered work graph

```mermaid
flowchart TD
    AUDIT["Inspect actual main, open PRs and CI"] --> M02["M0.2 mock app + testable API (PR #8)"]
    AUDIT --> LICENSE["M0.1 source and model license register"]
    M02 --> REVIEW["Review and merge CPU mock PR when authorized"]
    LICENSE --> GATE{"Licenses/commercial rights acceptable?"}
    REVIEW --> GPU["M0.3 actual Colab GPU/VRAM/disk preflight"]
    GPU --> FIT{"Checkpoint fits real hardware?"}
    GATE -- Yes --> FIT
    FIT -- Yes --> M1["M1 genuine validated PNG"]
    M1 --> M2["M2 genuine validated Wan-compatible MP4"]
    M2 --> M3["M3 audio / voice / subtitles / FFmpeg"]
    M3 --> M4["M4 full creative studio UX"]
    M4 --> M5["M5 recurring-character editable 60s film"]
    M5 --> M6["M6 optimization / measured benchmarks"]
    M6 --> M7["M7 production security + commercial operations"]
    GATE -- No --> RESEARCH["Find licensed alternate checkpoint"]
    RESEARCH --> GATE
    FIT -- No --> SIZE["Smaller/quantized/offload version if supported"]
    SIZE --> FIT
```

**Important:** M0.2 and license study can happen concurrently; genuine M1 cannot start until both licensing and actual GPU fit are known.

## Chart 6 — Threat, trust and deployment boundaries

```mermaid
flowchart LR
    USER["Untrusted browser/user input"] --> VALIDATE["VideoGen validation / auth later"]
    VALIDATE --> ALLOW["Approved model + workflow registry"]
    ALLOW --> JOBS["Persistent job queue"]
    JOBS --> PRIVATE["Private authenticated worker boundary (future)"]
    PRIVATE --> ENGINE["Pinned ComfyUI + reviewed custom nodes"]
    ENGINE --> ARTIFACTS["Validated output bytes"]
    ARTIFACTS --> STORE["Private storage + project permissions"]
    STORE --> USER
    BAD["Arbitrary graph, shell, URL, secret, filesystem path"] -. "Reject" .-> VALIDATE
```

**M0 security warning:** API has **no login, tenant isolation, public rate limit or quota**. CORS is not authentication. Bind only 127.0.0.1; never deploy M0 directly on the public internet or tunnel a Colab instance to serve strangers.

## Chart 7 — Domain relationships for movie system (target model)

```mermaid
erDiagram
    PROJECT ||--o{ GENERATION_JOB : owns
    PROJECT ||--o{ ASSET : owns
    MODEL_DEFINITION ||--o{ GENERATION_JOB : executes
    WORKFLOW_DEFINITION ||--o{ GENERATION_JOB : configures
    GENERATION_JOB ||--o{ GENERATION_ARTIFACT : yields
    GENERATION_ARTIFACT }o--|| ASSET : references
    PROJECT ||--o{ CHARACTER_REFERENCE : contains
    PROJECT ||--o{ ENVIRONMENT_REFERENCE : contains
    PROJECT ||--o{ SCENE : contains
    SCENE ||--o{ SHOT : contains
    SHOT ||--o{ TAKE : contains
    TAKE }o--o| GENERATION_ARTIFACT : uses
    PROJECT ||--o{ TIMELINE_TRACK : contains
    TIMELINE_TRACK ||--o{ CLIP : contains
    CLIP }o--o| GENERATION_ARTIFACT : uses
```

**Scope:** only project, job, mock artifact, events and lightweight model/workflow contracts are currently in PR #8. Character/scene/clip entities are future milestones.

## Chart 8 — Source-of-truth continuity workflow

```mermaid
flowchart TD
    START["New ChatGPT/Codex session"] --> MEMORY["Read docs/memory/PROJECT_MEMORY.md"]
    MEMORY --> GUIDES["Read docs/memory index + AGENTS.md"]
    GUIDES --> LIVE["Check live GitHub main/PRs/issues/CI"]
    LIVE --> TASK["Pick smallest unblocked issue"]
    TASK --> STUDY["Reuse/license/GPU gate for that issue"]
    STUDY --> IMPLEMENT["Feature branch / tests / code"]
    IMPLEMENT --> EVIDENCE["Record exact commit/CI/artifacts"]
    EVIDENCE --> UPDATE["Update PROJECT_MEMORY + status/history + decisions"]
    UPDATE --> PR["PR review and approved merge"]
    PR --> START
```

**Maintenance rule:** diagrams describe *intended* architecture, not proof it exists; edit their captions and state ledger whenever a milestone changes. Avoid diagrams that promise automatic production inference before corresponding tests.
