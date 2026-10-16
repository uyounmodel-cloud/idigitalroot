# iDigitalRoot — Complete Master Architecture Handoff v1.0
**Snapshot:** 23 September 2026 (Asia/Beirut)  
**Lineage:** five original product blueprints/extensions + Full Solution Developer Blueprint Requirements v0.1 + original design releases Stages 1, 2, 3, 4, 5, 5B, 6, 7, 8, 9, 9B.  
**Exact current checkpoint:** **Stage 9B completed as a DESIGN RELEASE CANDIDATE. Stage 10 not started in this lineage.**  
**Authority:** The original provided source bytes and stage archives control details; this handoff explains and locates them, but does not replace them.

## A. Project origin, identity and customer promise

iDigitalRoot is a **managed, human-delivered digital-presence and website service**, not an unmanaged AI website builder. It supports businesses, professionals, institutions and other approved audiences through a public marketing/knowledge website, Root Check and a structured public inquiry; internal teams qualify, quote and convert inquiries into invited client accounts; a client can then manage multiple independently delivered websites and related services from one Client Account while each website retains its own secure CMS. The internal Admin & Operations system governs all appropriate commercial, editorial, project, support, identity, monitoring and release processes.

The public website should explain what iDigitalRoot does, help visitors choose services and website blueprint families, present case studies/knowledge, offer a bounded Root Check and move interested visitors to the public inquiry wizard. Content is Admin-managed, professionally localized, accessible, SEO-ready and safe. Search and AI-discovery readiness are engineering quality goals, **not guaranteed rankings or recommendations**.

**Client Zero** is iDigitalRoot itself (`C0000`), the first project against which the platform, public CMS, operations, content, localized inquiry, onboarding, support, deployment, backup and security methodology will be proven before generalized client rollout.

## B. Source documents: authoritative in their original form

1. Public Website Product & Technical Blueprint v1.0 Candidate — public structure, audiences, service/blueprint discovery, Root Check, Knowledge Center, editorial/SEO/WCAG and product purpose; candidate Next.js/PostgreSQL and Git guidance **superseded by later decisions**.
2. Public Website Lead / Inquiry Extension v1.1 — supersedes older public self-registration; visitor inquiry wizard, lead intake, consent, qualification, Admin-owned conversion, invitation and deferred detailed onboarding. No public file upload/password harvest; no required paid or AI API.
3. Client Account Dashboard Final Product & Technical Blueprint v1.0 — relationship management and multi-website portfolio; project/onboarding/approval; safe domains, mailbox-service and commercial views, support, notifications and separate CMS handoff. Does **not** become a generic website CMS, DNS editor, deployment tool or shared site-credential vault.
4. Admin & Operations Dashboard Final Technical Blueprint v1.0 — internal individual staff identities, contextual task-oriented dashboards, source-of-truth management through authorized domain APIs, rich public CMS, leads, projects, commercial/finance, customer operations, security, deployment/observability and safeguards.
5. Cross-Platform Admin Control, Localization and Rich Media Extension v1.0 — Admin-managed unlimited locales, Arabic/English launch with RTL/LTR/fallback, rich/WYSIWYG HTML-content editing under sanitization, media and approved external embeds with CSP and publishing/versioning controls.
6. Full Solution Technical Architecture & Developer Blueprint **Requirements** v0.1 — specification of required engineering handoff sections, complete domain/data/API/security/operations/testing/traceability coverage and a dependency-ordered build; it is **not itself** the final v1.0 architecture.

The source register and read-only duplicates are in `01_ORIGINAL_AUTHORITATIVE_SOURCES`. Latest explicit approved decisions take precedence for deliberately superseded engineering choices; domain-specific nonconflicting original content remains authoritative. The distinction between *source-frozen requirement*, *later technical proposal*, *open gate* and *future capability* must remain visible.

## C. Primary product architecture and user lifecycle

```text
UNAUTHENTICATED VISITOR
  -> PUBLIC ASTRO WEBSITE: published localized content, service/website blueprint exploration, Root Check
  -> PUBLIC INQUIRY WIZARD: minimal qualified intake, versioned questions, consent, attribution
  -> CRM LEAD: retained raw source/answers/status/contact/provenance
  -> STAFF ADMIN: qualified Sales review, proposals, decision and authorized conversion
  -> CLIENT ACCOUNT CREATED: controlled command, duplicate prevention, audit and invitation outbox
  -> CLIENT ACTIVATION: secure one-use time-bounded invitation, client auth/session
  -> CLIENT PORTAL: profile, multiple websites, project onboarding/approvals, contracted services,
     invoice/renewal and safe domain/mail service status, support, notifications
  -> SITE-SPECIFIC CMS SSO: single-use signed one-site ticket; separate local CMS user/session/content

INTERNAL ADMIN & OPERATIONS: scoped controls and authorized domain commands over the lifecycle;
                            does not erase independent site ownership or grant itself arbitrary secrets.
```

The platform has four separate front-facing responsibility domains: Public, Client Account, Staff Admin & Operations and **each independent client website CMS**. A distinct public Inquiry trust boundary and public read façade support these. External mailbox providers/registrars/payment systems remain authoritative for their own actual state; central platform records contain service metadata and verified status only, not mailbox contents.

## D. Permanent engineering baseline

- **Default UI:** Astro and TypeScript; optional React islands only for justified interactions. Public website server rendering or static/hybrid delivery selected per content/publishing need.
- **Server:** Cloudflare Workers with distinct public-facing ingress and protected platform business-command service. Private internal routes through appropriate protected service bindings where supported; never publicly route internal APIs.
- **Data:** Cloudflare D1 for core platform relational records and R2 for platform-owned objects; independent client website CMSs preserve separate local source-of-truth stores. A physical single D1 per environment is the initial *proposed* platform model, not approval to provision it.
- **Development:** WSL2 Ubuntu working target `/home/limitedream/websites/C0000-idigitalroot`, Node/npm and local Wrangler. Target npm-workspaces layout without Git; source organization does not imply a single coupled deployment.
- **Environment:** independent Development, Staging, Production databases, R2 bindings, service secrets and release authority; never test against live production as a shortcut.
- **Cost:** Cloudflare-first/$0-first; never weaken security to meet a free CPU limit, and never introduce paid providers without cost/authority approval. Email mailbox hosting can be separate from Cloudflare hosting/DNS; Bluehost was explored but **not selected/purchased/configured by this lineage**.
- **Release:** immutable versioned ZIP + manifest + SHA-256 + validation + staging + explicit production approval + verification/rollback. **No Git** and no inferred source-control permissions.
- **Security:** unique staff identities, mandatory privileged staff MFA, backend permission + scope + object checks, protected audit, site isolation, host-only secure client/admin cookies, specific signed one-use CMS SSO, verified encryption/key/retention and recovery architecture once later gates close.
- **Localization:** unrestricted Admin-managed locale registry from foundation; initial Arabic RTL and English LTR; French/future additions without schema redesign. Per-locale publication/fallback/version/outdated-translation handling.
- **Public CMS:** approved visual editor/source HTML for content only, server-side sanitization, safe iframe provider model, CSP, R2 media, versioned review/publish/schedule/rollback. Publishing content is not deploying code.

## E. Completed design work, canonical metrics and actual proof level

| Stage | Exact major result | Proof and status |
|---|---|---|
| 1 | Source precedence, supersessions, permanent product/stack/no-Git rules | Original Markdown candidate; owner-final freeze not recorded in artifact. |
| 2 | 60 data/capability ownership families, 17 conceptual cross-system contracts, 16 trust boundaries and 18 invariants | Original Markdown candidate; logical, not physical deployment. |
| 3 | Proposed no-Git npm workspaces: three Astro apps, protected/public APIs, shared packages, environment and release layout | Original full ZIP; target layout, **not** present owner-folder inventory/mutation. |
| 4 | 216 logical entities across 19 domains; relationship/state/historical requirements; Developer Requirements alias coverage | Original full ZIP, CSVs and static coverage checks. |
| 5 | Physical D1 proposal and first 65-table reference SQL; 216-entity storage mapping | Original full ZIP; isolated SQLite reference checks, **not D1 runtime proof**. |
| 5B | 135 more proposed central table definitions: 200 platform tables total; 11 independent site CMS entities outside central; 4 projections and 1 archive separate | Original full ZIP; isolated SQLite syntax/FK/negative checks; field and migration audit gates remain. |
| 6 | Client/staff authentication, invitations, sessions, recovery, privileged MFA, proposed IAM field overlay | Original full ZIP; offline architectural SQL checks, **password hash CPU benchmark OPEN**. |
| 7 | 256 proposed granular permissions, 15 candidate role bundles, scopes/action matrix | Original full ZIP; offline policy reference; real permission runtime tests and owner business-role assignment pending. |
| 8 | Threat model (34 cases), proposed event/audit matrix (71), incident playbooks and protected audit reconciliation | Original full ZIP; offline audit integrity only; independent evidence custody/production alert/retention OPEN. |
| 9 | 135 proposed endpoints with auth/audit/error semantics, 17/17 contract and 60/60 ownership trace | Original full ZIP; 142 of 155 DTO types required field closure, which led to 9B. |
| 9B | All 155 endpoint DTO types field-modeled; 187 schema definitions; 135 typed OpenAPI operations; positive/negative synthetic fixtures; permission delta and interface review | Original full ZIP; separate offline verifier PASS. **797 + 30 runtime test obligations NOT EXECUTED.** |

**Explicit warning:** The exact per-stage verification records are inside each original ZIP; this summary does not transform candidate decisions into final freeze or pretend that synthetic fixtures are live integration tests. Overall architecture **continues at Stage 10**, not production implementation.

## F. Latest engineering control: Stage 9B

Stage 9B's authoritative detailed design artifacts are under its ZIP's `02_CONTRACTS/` directory: `API_DTO_JSON_SCHEMA_2020_12_v1.0.json`, `DTO_FIELD_CATALOG_v1.0.csv`, `ENDPOINT_TYPED_BINDINGS_v1.0.json`, `OPENAPI_3_1_DESIGN_CANDIDATE_v1.0.json`; its `03_FIXTURES/` and `04_TESTS/` document actual offline results and **unexecuted** runtime obligations. It preserves exact previous ZIP snapshots. Read the Stage 9B `00_READ_FIRST/README_FIRST.md` and main Markdown *before* Stage 10 work.

Known mandatory reconciliation: Stage 9B proposes two client permissions, `services.read` and `root_health.read`, which still need controlled Stage 7 integration with account/site scopes. Also explicitly review three inherited interfaces before launch: token-in-URL invitation preview (`API-0029`), sensitive GET Lead export (`API-0065`) and JSON-body DELETE role assignment (`API-0076`). The `API-0127` PUT Root Check configuration requires full replacement semantics or a separately approved API change. Never silently change the old endpoint IDs or client-facing contract during Stage 10.

## G. Current blocking/open gates (no invented approvals)

1. **Authority:** Stage 1–9B files still label themselves candidates; owner has approved continuation of design, not a final architecture/product/deployment freeze. Integrate all drafts into one final v1.0 only after Stages 10–22 and explicit owner approval.
2. **Data:** Stage 5B full SQL must be reviewed against actual product semantics and tested in **isolated local Wrangler/D1**; Stage 6 IAM, Stage 7 authorization and Stage 8 audit deltas need one reviewed, named migration lineage, not independent competing migrations. Determine real D1 query/index/cost/retention/tenant enforcement.
3. **Security:** Benchmark a genuinely secure Workers-compatible password hashing scheme under the actual allowed CPU/runtime before locking a Free launch; no weaker password scheme to remain free. Final MFA/session/SSO key rotation, audit export custody, recovery and incident notification require implementation evidence.
4. **Policy/business:** Client MFA mandatory vs optional; refund/action thresholds, financial approval roles, actual staff assignments, paid transactional email/mailbox provider, acceptable legal/consent versions, privacy/retention periods and emergency Root recovery need owner decisions at their proper gates.
5. **Provider/production:** No claim that Bluehost email, payment gateways, external monitoring or any paid dependency was activated. Real provider status must never be inferred from accepted API requests. DNS/production/cloud changes need exact independent authorization.
6. **API/UI:** Close proposed permissions and interface review findings; Stage 10 must prove each approved UI action has adequate contracts and identify/approve missing interfaces. 797+30 runtime tests remain unexecuted.
7. **Ops/DR:** Concrete queue/outbox, R2 isolation, independent client CMS runtime/database design, deployment staging/rollback, recovery point/time objectives, independent audit/backup custody and actual restore tests remain later design and execution gates.

## H. Remaining exact architecture plan and implementation strategy

Stage 10 Screen/Form/Button Matrix (next); 11 Public CMS/Publishing; 12 Localization/Translation; 13 Media/R2; 14 Background Jobs/Events; 15 independent CMS/SSO; 16 Services/Billing/Domains/Email/Support; 17 Infrastructure/Deployment; 18 Monitoring/Backup/DR; 19 Testing/Release Gates; 20 exact dependency-driven implementation; 21 Client Zero execution; 22 full requirements→UI/API/entity/test traceability. Then **cross-stage reconciliation and Master Architecture v1.0 owner freeze**. The full per-stage inputs, deliverables, acceptance and implementation phases are in `04_FORWARD_PLAN/ROADMAP_STAGES10_TO_LAUNCH.md`.

After architecture freeze, execute local read-only inventory and isolated engineering POCs, then approved bounded workspace setup/migrations/implementation. Build the central engineering foundation and protected admin API before feature UI; deliver minimal real vertical slices that execute E2E through D1 and permission/audit, then expand Public CMS/Website, Inquiry/Leads, invited Client Account, multi-site/project/SSO, commercial, operations and Client Zero. Never claim business buttons are complete until their backend/DB/error/audit/notification/permissions and negative tests are wired and pass in staging. Human approval gates guard production and spend.

## I. Owner involvement and no-error operating discipline

The owner's role is business authority and approval of actual mutation, expenditure, contractual policy and high-impact product tradeoffs—not a test runner for developer mistakes. Assistant should re-read exact source archive and predecessor evidence for each affected stage, design independently, validate offline/no-spend before proposing owner action, document cost and risk, obtain explicit permission before changing real infrastructure, and fail closed while preserving evidence. Absolute zero defects cannot be promised; the enforceable standard is **no unproven claim, no hidden assumptions, negative-path tests, staged evidence and controlled rollback**.

## J. Files whose authority must not be confused

`90_OPTIONAL_HISTORICAL_CONTEXT/` contains the **earlier Cloudflare client-site A-to-Z handoff v2.0** as background for setup and no-Git operating history. It does not supersede later iDigitalRoot Stage 1–9B specs on conflict. A separate v2 website-factory/working-solution family is detectable in the working container but was **not added to this architecture source lineage**; consult `05_TRACEABILITY/UNRECONCILED_PARALLEL_MATERIAL.md` before importing it. Presence of code ZIPs elsewhere is neither authorization to alter live infrastructure nor proof of this architecture's implementation.

**Restart sentence:** The next assistant should start **Stage 10**, based on exact Stage 9B endpoints and original source blueprints, generate a standalone verified Stage 10 design release, and preserve all unresolved Stage 5B–9B gates for the future Master Architecture freeze.
