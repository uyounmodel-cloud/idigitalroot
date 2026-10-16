# Client Panel mandatory security requirements

**Status: DESIGN REQUIREMENTS / NOT IMPLEMENTED OR VERIFIED.** The complete original security authority is copied verbatim under authority/master/04_SECURITY/. This extension applies to the proposed Client Account, staff operations needed to operate it, private tools, APIs, background jobs and site SSO. It supplements and does not replace any original title or control.

## Detailed authority and evidence rules

- OWASP ASVS v5.0.0 is the detailed verification authority: strong L2 baseline for Internet-facing application functionality, applicable L3 for privileged/high-value/high-impact flows. All345 preserved requirement rows require applicability/target/evidence review, not automatic full compliance.
- OWASP Top10:2025; OWASP API Security Top10:2023 until a later stable official release; final NIST SP800-218 SSDFv1.1. Monitor newer standards without silently substituting drafts. Current official Cloudflare Access/Workers/D1/R2 security guidance applies to actual provider configuration.
- The complete151-title risk inventory is mandatory minimum coverage. The new CLIENT_PANEL_SECURITY_RISK_REGISTER and CLIENT_PANEL_ASVS_5_0_0_REGISTER start NOT_ASSESSED_CLIENT_PANEL. Existing Phase1 evidence/status is context, not Client acceptance.
- Record per-feature applicability, architectural rationale, prevention/control, unit/integration/abuse/browser/manual/config/operations evidence, review owner, residual risk and actual outcome. N/A requires a concrete architecture-specific rationale; any deviation/risk exception requires explicit informed acceptance. An unrun test is NOT_RUN or BLOCKED, never PASS.

## The owner's mandatory19 obligations — preserved in full

For EVERY system and major feature:
1. create/update a threat model and data-flow diagram;
2. enumerate assets, actors, trust boundaries, entry points, abuse cases and failure modes;
3. map every applicable risk in SECURITY_MASTER_BASELINE.md;
4. implement server-side authorization at object, property and function levels;
5. design fail-closed behavior and explicit exceptional-condition handling;
6. protect sessions, tokens, cookies and SSO against fixation, replay, theft and confused-deputy failures;
7. enforce validation/encoding/sanitization and contextual output handling;
8. prevent SQL/NoSQL/command/template/XML/LDAP/XPath and other injection classes;
9. prevent SSRF, path traversal, unsafe file upload/import/embed behavior and unsafe URL fetching;
10. rate-limit and abuse-protect sensitive business flows;
11. use least privilege for Workers/D1/R2/provider/service bindings;
12. keep secrets out of source, browser bundles, logs, screenshots and artifacts;
13. use strong cryptography and key rotation/secret lifecycle appropriate to the platform;
14. enforce security headers/CSP/referrer/frame/cache behavior;
15. implement structured security logging, auditability, alerting and incident evidence without leaking secrets;
16. maintain dependency pinning, lock integrity, provenance, SBOM and vulnerability review;
17. test negative paths, race/concurrency, replay, stale versions, malformed inputs, authorization bypasses and failure-open behavior;
18. never mark a security item N/A without a written rationale tied to architecture/evidence;
19. do not claim “secure” merely because unit tests pass; run dedicated adversarial/security gates.

The owner's mandatory vulnerability-title list is preserved verbatim in SECURITY_MASTER_BASELINE.md and is a minimum, not a maximum. Never claim zero vulnerabilities or100% security. Independent/HQ acceptance cannot be inferred from the implementing AI's tests.

## Client-specific security contract

**Customer/staff identity:** distinct identity classes and session/auth boundaries. No shared privileged/customer accounts, default production users or client-controlled role assignment. Mandatory privileged MFA; secure customer MFA/recovery design. Re-auth/verify high-impact identity, membership, ownership, billing, domain-transfer, MFA and export operations. Invite/verification/reset tokens are random, hashed at rest where suitable, short-lived, purpose/account/user-bound and atomically one-time. Unknown/disabled/revoked state fails closed. Enumeration/credential-stuffing/email cost controls are layered and tested.

**Scope and entitlement:** every object/property/function access, link, attachment, history, search, bulk action, job and export checks authenticated user -> account/membership -> site/owner -> capability/entitlement -> action/state/version. Never trust the browser's accountId, siteId, role, price, paid flag or audience. D1 bindings are not row security. Cross-object foreign references must belong to the authorized scope; deny unscoped queries and stale authorization caches after revocation. Determine whether personal workspace material is user-private or account-shared before implementing roles.

**Cookie/browser/edge:** secure HttpOnly cookies, session rotation/expiry/revocation, CSRF tokens/origin checks, strict allowed hosts/redirects/CORS, CSP and frame/referrer policies, private no-store/cache partitioning, no service-worker private-cache leaks, no sensitive analytics/referrers/history. Validate actual Cloudflare Access assertions at the approved perimeter; never trust spoofable identity headers or treat Access as application authorization. Public traffic does not get D1/R2/CMS API credentials.

**Business invariants:** server-owned plan/price/tax/currency; immutable quote/approval versions and acceptance evidence; permissioned state transitions; atomic CAS/idempotency for submission/approval/billing/entitlements/SSO. Payment webhook signature/clock/replay and reconciliation; no Paid from a browser redirect. Plan/audience/theme changes do not grant access. Downgrade/expiry/closure follows agreed retention/access policies; no accidental erasure or stale entitlement continuation.

**SSO:** signed/tamper-evident minimal ticket, issuer/audience/site/user/purpose/nonce/expiry binding, fixed algorithm policy, approved key storage/rotation and atomic one-time consumption. Validate revocation/disabled identities at issue and redemption. Bind target CMS/site in a vetted registry and prevent open redirects/confused deputy. Minimize ticket exposure in URLs/logs/referrers/analytics. Prove one winner for simultaneous redemption and A-to-B cross-site denial. A fake broker button is not integration.

**Private tool outputs and links:** protected drafts and controlled explicit sharing; deny public reads/search/indexes of private records. Define whether exports/shares include PII/third-party contacts. Apply bounded jobs, authorization at start and download, retention/expiry/revocation and safe filename/MIME/content-disposition/origin. Prevent HTML/SVG/script and CSV/formula/document/QR/URL injection. Avoid arbitrary server URL fetching or rendering untrusted external HTML. Scanner, PDF/export engine and approved integrations are explicit failure/abuse boundaries.

**Files/media:** no general file vault. Approved project intake only: type/content/extension/size/quantity constraints, random object keys, quarantine/scan, non-executable private objects, safe separate-origin delivery, scoped download authorization, retention/deletion and audit. No arbitrary archive extraction, direct raw R2 access, path traversal or trusted upload metadata. Safety-provider unavailability means pending/quarantine, not clean.

**Cloud/data/jobs:** private least-privilege Workers/D1/R2/service bindings, isolated environments, no raw browser DB/storage secrets, parameterized SQL, consistent scoped DAL patterns, bounded CPU/memory/DB/storage/export/email/queue limits and cost observability. Jobs carry server-created scope, idempotency keys, version checks and bounded retries; revalidate authorization where appropriate. Public frozen migration lineages remain unchanged. New domain migration and provider resource creation need explicit authority.

**Secrets/cryptography/supply chain:** vetted algorithms/libraries, random capabilities, strong password hashing where used, appropriate transport/at-rest/key handling and rotation. No custom unaudited crypto or permanent sample keys in a release. Exact locks/toolchain, install-script review, SCA/license/secret scanning, SBOM and source/build provenance. Review all deployable components, not only the frontend package. A clean dependency audit is not proof of no vulnerabilities.

**Privacy/legal:** purpose/minimization/classification, operator access, residency, minors/age/guardian policy where relevant, export/share/retention/deletion and financial/audit legal holds need owner/legal decisions at their release gate. Study, application, reflection, skills and budget entries are private by default; organization membership does not expose them automatically. No PII or workspace content in analytics/security logs by default.

**Operations/recovery:** meaningful redacted audit, tamper-evidence/access separation, security alerts and incident/revocation/evidence runbooks. Define real backup/restore of authoritative D1, R2, configuration and key dependencies, with RPO/RTO and actual restore exercises. Source/repo/environment config snapshots do not restore all live records automatically. Unknown/stale Health and job/provider failures are explicit, never green defaults.

## Required adversarial review

Run CLIENT_PANEL_SECURITY_TEST_PLAN against the exact built/sealed source with multiple isolated customers/sites, scoped and unscoped staff, changed entitlements and separate CMS consumers. Expand it when the architecture creates new risks; it is not exhaustive. Map outcomes to all applicable original risks and ASVS requirements. Review negative APIs independently of UI; perform races/replays/resource abuse and dedicated manual/config/provider gates. Preserve original S1–S11 gates and independent release review. Final verdict depends on actual integrated evidence, not this document or generated matrices.
