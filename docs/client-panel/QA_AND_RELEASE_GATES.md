# Client Account QA, acceptance and release gates

Status: PLANNED / NOT EXECUTED. This document is not evidence of working Client code. New planning statuses are NOT_ASSESSED/NOT_RUN; execution verdicts are PASS / FAIL / BLOCKED, with risk exceptions separately signed and scoped. Prior public/CMS evidence cannot promote these gates.

| Gate | Required evidence | Not sufficient |
|---|---|---|
| Q0 Authority/discovery | Exact original master/current source integrity; complete reading checkpoint; answered blocking questions; explicit scope/migration/sequence approval | Filename summaries, recommendations treated as approval |
| Q1 Architecture | Per-feature DFD/threat model, account/site/role/entitlement ownership, data classification, staff/CMS contracts, privacy/minors/commercial decisions at their gate | Attractive screens without data/service ownership |
| Q2 Deterministic source | Pinned compatible toolchain/locks, safe install-script review, source/component manifest/checksums, fresh isolated extraction and frozen public migration equality | Reusing a dirty working directory or test data |
| Q3 Runtime | Official Workers-compatible build, actual local workerd/D1/privateR2, durable persistence/read-after-restart, server-side authorization | Dev server/SQLite-only/localStorage demo or a listening port |
| Q4 Core journeys | Invitation/verification/login/recovery/MFA/session; profile; many Roots; questionnaire save/resume/submit; real staff update; protected exact-version preview/approval; support | Canned success notices or manually changing DB records |
| Q5 Services/commercial | Versioned catalogue/entitlements/quotes/invoices/renewals; approved price/tax/cancel/upgrade/downgrade rules; payment reconciliation as applicable | Browser success URL as proof of payment; audience as entitlement |
| Q6 Workspaces | Every approved module has real save/edit/conflict/export/share/privacy/retention/output tests. Student12+16 fully working before first commercial student release | Menus/cards/tutorials presented as working tools; silent deferral |
| Q7 SSO/isolation | Two independent site consumers; one-time atomic redemption; wrong user/account/site/audience/issuer, replay/race/expiry/revocation/key-failure tests; independent sessions | A link to a CMS, shared passwords, one happy-path mock |
| Q8 Dedicated security | All151 title assessments and applicable345 ASVS mapping, adversarial/manual/independent gates and documented residual risks | Scanner score, unit tests or inherited public-site PASS |
| Q9 UX/localization | EN/LTR+native AR/RTL, keyboard/screen reader/manual tasks, WCAG2.2AA target, reduced motion, small/large phones/tablets/desktops; no clipping/hover-only action/runtime console error | Automated axe alone; mirrored English; screenshots alone |
| Q10 Reliability/privacy | Conflict/race/replay/idempotency; outage/timeouts/cost/queue abuse; job failure/recovery; consent/retention/export/deletion/minors/access decisions | Swallowed exceptions, stale healthy indicators, unbounded retries |
| Q11 Providers | Exact approved staging behavior for mail/identity/payment/domain/health/scan/SSO targets, secrets/bindings least privilege and costs | Local fake providers, credentials existing, undocumented new spend |
| Q12 Operations | Monitoring/alerting/redacted audit; actual backup/restore and RPO/RTO exercise; incident/revocation/rollback runbooks | Backup file exists; logs contain private payloads; no restore test |
| Q13 Sealed candidate | Source ZIP/SHA, manifest/checksums, toolchain/lock/SBOM/provenance, change/feature/test/security matrices, fresh-extraction reproduction, owner guide and explicit open gates | Self-declared production ready without evidence |
| Q14 Staging/release | Owner authorization for exact environment/action/credentials mechanism/spend/release; authorized deployment evidence, post-deploy checks and rollback | Authentication, a local build, positive design feedback or scope approval |

## Browser/integration coverage

Use at least2 isolated customers with2 Roots each, staff roles with and without scopes, an optional business collaborator only if approved, two independent CMS targets, changed/revoked entitlements and disabled identities. Verify every main route/button/link/form/empty/error/action state and its server effect. Record synthetic test accounts and permissions; never use owner private data. API deny tests must bypass UI and swap object/property IDs directly.

Exercise absent/expired sessions; interrupted recovery; two tabs/autosave conflicts; replaced versions after preview; failed/double submissions; worker restarts; persistence; dependency outage; partial job completion; wrong currencies/timezones; share revocation and export access; closures/retention; malformed multilingual text; accessible phone approval and support. Test actual produced PDF/vCard/QR/etc only after formats are agreed; compare outputs and import/scan in supported clients.

## Performance and resource budgets

Agree budgets for mobile network/load, page/JS/asset weight, interactivity/layout shift, D1 query/row/latency, R2 storage/egress, export/PDF/QR work, auth/email/notification fan-out and provider cost before production. Measure representative real devices/networks and workloads; loopback or headless observations are diagnostic, not a production gate. Define quota/circuit-breaker behavior and abuse tests without charging unapproved providers.

## Local reproduction and release boundaries

Use the owner's Windows+Ubuntu/WSL native staging, plus current cloud Linux where useful. Inspect existing tools and verify Cloudflare identity read-only. Use deterministic install, checks/tests, official Workers build, workerd/local D1/R2, real Chromium/browser regression and fresh sealed extraction. Do not change frozen Core0001–0016/Analytics0001–0002 or existing review datasets. Browser-tested Linux does not prove Windows launcher execution.

No implementation gate is currently claimed passed by this planning handoff. Integrated security/QA/release verdicts must be written against the exact future sealed Client/Admin candidate. An inaccessible provider/independent check remains BLOCKED; it is never waived by convenience.
