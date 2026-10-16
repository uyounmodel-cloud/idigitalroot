# Client Account blueprint and question-first AI handoff

**Version 1.2 · 16 October 2026 · PROPOSED — OWNER DISCOVERY / SCOPE APPROVAL REQUIRED.** This package defines the next discussion and implementation contract; it does not contain a built Client Panel or authorize deployment.

The owner requested a complete blueprint and a reusable prompt that makes the next AI ask questions before creating the solution. Original product/security authorities are preserved alongside the new proposal. Existing decisions must not be asked again as if unknown.

## Use in another conversation

1. Download the small **IDIGITALROOT_CLIENT_PANEL_BLUEPRINT_AND_AI_HANDOFF_2026-10-16_v1.2.zip** from the repository's `downloads` folder and attach it to the new conversation. It includes the documents, original security authorities and exact current public/CMS source ZIP, but no live databases or credentials.
2. Copy **START_NEW_CONVERSATION_PROMPT.txt** in full and paste it as your message. The first response must be a reading checkpoint and a short batch of unresolved questions. No application creation before discovery and explicit scope approval.
3. Answer the questions over manageable rounds. The AI records decisions, shows the final agreed scope and asks once for permission to start that local implementation. Routine fixes within the approved scope do not need repeated approval.
4. Before application changes, the AI also verifies the original master companion and follows its mandatory read order. The exact original master is now separately preserved at `downloads/IDIGITALROOT_CODEX_MASTER_HANDOFF_2026-10-14_v1.1.zip`; its SHA256 is in SOURCES_AND_AUTHORITY.json. The AI should retrieve it using the connected repository where possible, without making you shuttle old context. If retrieval is unavailable, it can continue discovery using the included authorities, but must report the full pre-implementation authority check as blocked.

## Main documents

- [Blueprint](CLIENT_PANEL_BLUEPRINT.md): full product, architecture, workflows, data ownership, security and delivery plan.
- [Copy-ready prompt](START_NEW_CONVERSATION_PROMPT.txt): question-first instructions for a new AI conversation.
- [Decision/question register](DISCOVERY_QUESTIONS.csv): proposed defaults, blocking stage and unanswered decisions.
- [Feature inventory](FEATURE_INVENTORY.csv): shared account features, all 12 Toolbox tools,16 Student Workspace positions and proposed audience extensions.
- [Security requirements](SECURITY/CLIENT_PANEL_SECURITY_REQUIREMENTS.md) and [threat model](SECURITY/CLIENT_PANEL_THREAT_MODEL.md).
- [151-title risk register](SECURITY/CLIENT_PANEL_SECURITY_RISK_REGISTER.csv), [345-requirement ASVS register](SECURITY/CLIENT_PANEL_ASVS_5_0_0_REGISTER.csv), and [adversarial test plan](SECURITY/CLIENT_PANEL_SECURITY_TEST_PLAN.csv). Every new Client Panel assessment starts NOT_ASSESSED.
- [QA and release gates](QA_AND_RELEASE_GATES.md).
- [Reading order](READ_ORDER.md) and [source authority](SOURCES_AND_AUTHORITY.json).

`authority/master/04_SECURITY/` contains every original security file **verbatim**. The 151-title list includes the original vulnerability groups and additional mandatory modern classes. None is replaced by a shorter generic checklist. Applicable risks must have real controls/tests; N/A requires architecture-specific rationale. Public-site test results are historical evidence only, never Client Panel acceptance.

## What is already fixed

One account can own many Digital Roots. Public site/CMS, Client Account, internal Admin and every client website CMS remain distinct. Website content and detailed website analytics stay in each website CMS. Four public audiences are Students, Employees & Professionals, Entrepreneurs & Startups, Businesses & Organizations. The full 12 Toolbox and16 Student Workspace positions are mandatory for the first commercial student release, with Career Kit shared between both entry points.

Cloudflare Workers + D1 + private R2 and the owner's Windows+Ubuntu/WSL environment remain fixed. Existing Cloudflare identity is checked read-only; no forced login/raw token request. No provider mutation, migration of the frozen public schemas, new spend or deployment is authorized by this handoff. Student academic/budget/career data is private by default. Additional audience packs, pricing/providers, team seats and Client/Admin implementation sequence still need discovery/approval.

## Current delivery state and backup limits

MOTION01 public/CMS review source: `a3a11293559b72dac65973184412b38fbbf76b61cf89e4acec845db812dfbd2b`. Its exact-source local32-step verification passed; Phase1 production/legal/provider/independent/manual gates remain OPEN. Positive owner feedback does not establish independent security acceptance or an actual deployment. Client/Admin/Toolbox/Workspace implementations have not been delivered.

This handoff preserves project documents, the original master companion and source references on GitHub. **It does not back up live CMS drafts/databases/uploads, machine credentials, all investigation files or chat history.** Preserve those separately and verify restoration. A new clone or saved setup draft alone does not prove full recovery.
