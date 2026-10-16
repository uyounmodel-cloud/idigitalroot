# iDigitalRoot — Codex Master Handoff

**Transfer date:** 2026-10-14  
**Package purpose:** move the full iDigitalRoot Personal/Student platform work from ChatGPT to a fresh Codex account without losing the implemented code, approved product decisions, security requirements, historical evidence, future-system plans, or release boundaries.

## What this package contains

This is not only a prompt. It contains:

1. the exact owner-approved Public Website UI authority;
2. the latest Public Website frontend candidate and the latest local closure operator;
3. the exact owner-approved connected Public Website CMS source and its owner-review package;
4. the latest shared Public Backend authority used by the current frontend work;
5. the accepted architecture/auth/data/analytics/CMS technical authorities carried forward from the prior handoff;
6. the original full 2026-10-06 handoff, both immutable ZIP and extracted form;
7. the previously approved/frozen blueprints for the Public Website, Admin & Operations Dashboard, Client Account Dashboard, localization/rich-media extension and full-solution engineering scope;
8. new consolidated system definitions for every product now in scope;
9. a high-assurance security baseline covering the owner's entire mandatory issue list plus additional modern web/API/cloud/supply-chain classes;
10. a phased development roadmap and Definition of Done;
11. ready-to-use Codex prompts for continuation of the current phase and future phases.

## The six product systems in scope

The product inventory is:

1. **iDigitalRoot Public Website — Personal / Student version**
2. **iDigitalRoot Public Website CMS** — a dedicated application, separate from Admin
3. **iDigitalRoot Admin & Operations Dashboard**
4. **iDigitalRoot Personal Client Panel / Client Account**
5. **Reusable Client Website CMS** — derived from the proven Public Website CMS core but deployed/isolated per client website
6. **Client Public Website Factory / Prompt System** — the controlled architecture and prompt set used to create future client public websites that connect to the reusable Client Website CMS

The inventory order above is not the execution order. The frozen execution order remains:

> Phase 1 Public Website + dedicated Public Website CMS → Phase 2 Admin & Operations → Phase 3 Personal Client Panel → Phase 4 reusable Client Website CMS → Phase 5 client Public Website factory/templates.

## Frozen hosting and local-development environment

- **Hosting/runtime choice: Cloudflare Workers.** This is an accepted project decision, not an open platform-selection question.
- **Data/storage targets: Cloudflare D1 + R2**, behind Worker/server boundaries.
- The owner already has **Ubuntu under WSL/WSL2 on the Windows PC** and intends the solution to be built/tested locally there before deployment.
- The owner states the workstation/WSL environment is already **connected/authenticated to the relevant Cloudflare account**. Codex should verify that connection read-only and reuse it if valid rather than asking the owner to reconnect by default.
- Local verification should include the built Workers target under **workerd/Cloudflare-compatible local preview** plus real browser tests.
- Existing Cloudflare authentication does **not** authorize provider mutation or deployment. Explicit owner approval remains mandatory for staging/production changes, DNS, Workers/D1/R2 mutation, secrets, Access policy, paid services or release.
- Read `00_START_HERE/LOCAL_DEVELOPMENT_AND_CLOUDFLARE_ENVIRONMENT.md` before engineering work.

## Critical current state

- The Public Website presentation/content authority is **owner approved** at v4.3.
- The Public Website CMS presentation authority is **owner approved** at v4.1.
- The real connected professional Public Website CMS source **v1.5.3 is owner approved** in this conversation.
- Phase 1 is **not yet closed** because the Public Website frontend binding/Cloudflare workerd/browser closure is still in progress.
- The current FE candidate is v1.1.1. The latest local closure operator is v1.7, prepared after fixing the Chrome cache executable-permission defect. **It has not yet been proven PASS by the owner after that repair.** Codex must independently verify rather than assume it passes.
- FE-03 live inquiry submission/browser analytics is not closed.
- P1-SEC-01, P1-QA-01 and P1-REL-01 are not closed.
- Nothing in this package grants production deployment, provider mutation, production-secret use, paid-plan/spend authority, or final release authority.

## How Codex must begin

1. Verify `SHA256SUMS.txt` and `RELEASE_MANIFEST.json` before modifying anything.
2. Read `00_START_HERE/READ_ORDER.md` in full and follow it.
3. Read `00_START_HERE/CODEX_MASTER_START_PROMPT.txt` and use it as the governing instruction.
4. Classify every artifact as **OWNER-APPROVED**, **ACCEPTED TECHNICAL AUTHORITY**, **CURRENT CANDIDATE**, **PLANNED/FUTURE**, or **HISTORICAL EVIDENCE**. Never promote one class into another without evidence.
5. Finish current Phase 1 before beginning Admin, Client Panel or Client Website CMS implementation unless the owner explicitly changes the execution order.
6. Ask the owner only questions that remain genuinely unresolved after reading the entire package. Do not ask the owner to repeat anything already specified here.

## Owner workflow preference

The owner does not want to be used as a debugger. Codex/engineering should perform the technical work, run the tests, repair failures, and provide bounded owner review packages only when human approval is actually needed.

## Security posture

Treat iDigitalRoot as a **high-assurance Internet-facing platform**. Security is a design constraint, not a final checklist. Every system and every release must be threat-modeled, authorization-tested, abuse-tested, supply-chain checked, dependency-pinned, fail-closed, audited and independently verified against the security files in `04_SECURITY/`.
