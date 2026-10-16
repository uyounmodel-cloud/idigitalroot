# Security Acceptance Gates

No application may be called release-ready until applicable gates pass on the exact sealed candidate.

## Gate S1 — Architecture/threat model

- system DFD/trust boundaries current;
- data classification current;
- auth/authz decisions identified;
- abuse cases and fail-closed behavior documented;
- external providers and secrets mapped.

## Gate S2 — Identity/session

- no shared privileged accounts;
- MFA policy tested for privileged roles;
- session fixation/rotation/expiry/revocation tested;
- recovery does not bypass security;
- brute-force/credential-stuffing/account-enumeration controls tested;
- cookies/token storage reviewed.

## Gate S3 — Authorization

Test vertical/horizontal privilege escalation, IDOR/BOLA, object-property access, function access, scope/tenant/site boundary, hidden endpoints, forceful browsing and stale permissions.

## Gate S4 — Injection/input/output

Test SQL/NoSQL/command/template/HTML/XSS/XXE/LDAP/XPath/HPP/verb tampering as applicable, plus output encoding, rich-text sanitization and safe URLs.

## Gate S5 — Files/media/SSRF/providers

Test upload type/content/size/path, malicious SVG/HTML/polyglot/archive, SSRF including redirects/DNS/private ranges, embed allowlists, provider disable behavior and unsafe external responses.

## Gate S6 — API/business abuse

Test rate limits, quotas, pagination/export limits, sensitive business-flow automation, replay/idempotency, race/TOCTOU, version/concurrency, mass assignment, excessive data exposure and unsafe third-party API consumption.

## Gate S7 — Browser/edge

Test CSRF, CORS, CSP, clickjacking, cache privacy, host/origin handling, redirects, postMessage, security headers, service worker/WebSocket if used.

## Gate S8 — Crypto/secrets/data

Check algorithms, TLS, secret/key storage, accidental client/log leakage, backup/export control, data minimization/retention and cross-client isolation.

## Gate S9 — Supply chain/configuration

Check pinned dependencies, lock integrity, known vulnerabilities, install scripts, default/debug settings, source maps, verbose errors, directory exposure, dangling preview routes, environment separation and least-privilege bindings.

## Gate S10 — Logging/monitoring/resilience

Verify security/audit events, no secret logging, alert coverage, fail-closed exception handling, resource exhaustion controls, DDoS/app-layer abuse posture, backup/restore evidence and rollback.

## Gate S11 — Independent release review

Security evidence must be reviewed independently from the feature implementation where practical. Self-tests are necessary but not sufficient for the final security verdict.

## Verdicts

Only: PASS / FAIL / BLOCKED / PASS-WITH-EXPLICIT-RISK-ACCEPTANCE. Never convert BLOCKED to PASS because a test could not run.
