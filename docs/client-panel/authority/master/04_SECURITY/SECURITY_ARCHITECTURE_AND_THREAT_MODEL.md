# Security Architecture and Threat-Model Requirements

## Threat-model method

For each system and material feature maintain:

1. data-flow diagram;
2. trust boundaries;
3. actors and workload identities;
4. assets/data classification;
5. entry points and egress points;
6. authentication and authorization decisions;
7. abuse cases;
8. STRIDE-style or equivalent threat enumeration;
9. risk rating and mitigation owner;
10. security test/evidence mapping;
11. residual risk and explicit acceptance if non-zero.

## Platform-wide security architecture

### Edge

- HTTPS only; modern TLS;
- Cloudflare WAF/rate limits/bot controls where appropriate;
- strict host/origin handling;
- Access/Zero Trust for privileged internal applications where approved;
- DDoS/application abuse controls;
- no security-by-obscurity path assumptions.

### Application

- server-side identity and permission checks;
- object/property/function authorization;
- input validation + contextual encoding;
- CSRF for cookie-authenticated state change;
- safe CORS deny-by-default;
- security headers and CSP;
- deterministic failure behavior;
- bounded resource use;
- version/concurrency checks for sensitive mutations.

### Data

- least-privilege DB/object access;
- no browser credentials;
- parameterized SQL only;
- data minimization;
- encryption in transit and provider-supported at rest;
- secrets separated from content data;
- backup/export access control;
- retention and deletion policies.

### Identity/session

- separate privilege domains;
- MFA for privileged roles;
- secure session cookie attributes;
- rotation/revocation;
- anti-replay;
- login/recovery abuse protection;
- sensitive action re-auth.

### CMS/content

- schema-driven safe capabilities;
- server sanitization;
- provider/embed allowlists;
- media quarantine/validation;
- no arbitrary application code;
- preview/publish exact-version security.

### Operations

- immutable/tamper-resistant release hashes;
- environment separation;
- secrets in provider secret stores;
- least privilege CI/deployment identities;
- audit privileged changes;
- break-glass procedure;
- alerting on auth/authorization/admin/security anomalies.

## Fail-closed expectations

Examples that must fail closed:

- invalid/missing authorization;
- stale row/version on protected mutation;
- unknown CMS component;
- disabled provider/embed;
- invalid media state;
- SSO wrong audience/replay/expiry;
- missing required publication readiness;
- malformed signed token;
- backend dependency failure where unsafe fallback would expose draft/private content;
- security configuration not loaded.
