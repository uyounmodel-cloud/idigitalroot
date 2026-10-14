# iDigitalRoot High-Assurance Web Application Security Master Baseline

This file is mandatory for every iDigitalRoot application, API, Worker, CMS, Admin surface, client portal, client website CMS, public website and supporting service.

It preserves the owner's complete mandatory title list and extends it with additional modern classes that must be considered. A risk may be marked not applicable only with written architecture-specific rationale and evidence.

## External verification references

- OWASP ASVS **v5.0.0** — detailed web application verification requirements.
- OWASP Top 10 **2025**.
- OWASP API Security Top 10 **2023** until a later stable official version supersedes it.
- NIST SP 800-218 SSDF **v1.1** as the current final NIST secure-development baseline; later drafts may inform but do not silently replace final authority.
- Current official Cloudflare Workers/Access/D1/R2 security documentation for provider-specific configuration.

## Owner-mandated vulnerability titles — minimum required coverage

### 1. Access Control and Authorization Issues

- Broken Access Control (BAC)
- Insecure Direct Object References (IDOR)
- Privilege Escalation (Vertical and Horizontal)
- Missing Function-Level Access Control
- Forceful Browsing / Predictable Resource Location
- Insecure Redirects and Forwards
- Cross-Origin Resource Sharing (CORS) Misconfigurations

### 2. Authentication and Session Management Flaws

- Broken Authentication
- Session Fixation
- Session Hijacking
- Insufficient Session Expiration / Timeout
- Brute Force and Credential Stuffing Vulnerabilities
- Weak Password Policies and Storage Flaws
- Multi-Factor Authentication (MFA) Bypass
- Insecure JSON Web Token (JWT) Implementation
- Account Enumeration

### 3. Injection Flaws

- SQL Injection (In-band, Blind, Out-of-band)
- NoSQL Injection
- OS Command Injection
- Remote Code Execution (RCE)
- Cross-Site Scripting (Reflected, Stored, DOM-based)
- Server-Side Template Injection (SSTI)
- XML External Entity (XXE) Injection
- LDAP Injection
- XPath Injection
- HTTP Parameter Pollution (HPP)
- HTTP Verb Tampering

### 4. Cryptographic and Data Protection Failures

- Cryptographic Failures / Inadequate Encryption
- Weak or Deprecated Cryptographic Algorithms
- Poor Key Management
- Hardcoded Secrets and API Keys
- Sensitive Data Exposure / Excessive Data Exposure
- Unencrypted Data Storage and Transmission
- Missing Security Response Headers

### 5. Design, Architecture, and Business Logic Flaws

- Insecure Design
- Business Logic Vulnerabilities
- Race Conditions / Time-of-Check to Time-of-Use (TOCTOU)
- Lack of Rate Limiting and Abuse Prevention
- Order Processing and Price Manipulation Flaws
- Unsafe Asynchronous Operations

### 6. Configuration and Operational Vulnerabilities

- Security Misconfigurations
- Default Credentials and Unchanged Settings
- Directory Listing and Information Disclosure
- Verbose Error Messages and Stack Trace Exposure
- Unpatched Software and Components with Known Vulnerabilities
- Software Supply Chain Failures / Dependency Poisoning

### 7. Server-Side Request and File Handling Issues

- Server-Side Request Forgery (SSRF)
- Local File Inclusion (LFI)
- Remote File Inclusion (RFI)
- Insecure File Upload Handling
- Directory / Path Traversal

### 8. API-Specific Security Issues

- Broken Object Level Authorization (BOLA)
- Broken User Authentication (API context)
- Unrestricted Resource Consumption
- Unrestricted Access to Sensitive Business Flows
- Improper API Asset Management
- Unsafe Consumption of Third-Party APIs

### 9. Client-Side and Frontend Security Risks

- Clickjacking (UI Redress)
- Cross-Site Request Forgery (CSRF)
- Insecure Cross-Origin Communication
- Browser Cache Poisoning
- WebSocket Security Issues

### 10. Resilience, Monitoring, and Integrity Failures

- Security Logging and Monitoring Failures
- Insufficient Alerting and Audit Tracking
- Software or Data Integrity Failures
- Insecure Deserialization
- Distributed Denial of Service (DDoS) / Application Layer DoS
- Mishandling of Exceptional Conditions (Failing Open)

## Additional mandatory modern classes to assess

### Authorization/data binding

- Broken Object Property Level Authorization / mass assignment
- Over-posting / unsafe automatic binding
- Tenant/site/account scope confusion
- Confused deputy and cross-service authorization mistakes
- Authorization cache incoherence
- Stale permission/session/token continuation after role revocation

### OAuth/OIDC/token/federation

- OAuth/OIDC redirect URI validation flaws
- Authorization code interception/replay
- PKCE omission where applicable
- Token audience/issuer confusion
- Token substitution / algorithm confusion
- Refresh token theft/reuse
- SSO ticket replay/cross-audience use
- Trusting unverified proxy/Access identity headers

### HTTP/proxy/cache

- HTTP request smuggling/desynchronization
- Host header injection
- Cache poisoning / cache deception
- Web cache privacy leaks
- Improper Vary/cache key behavior
- CRLF/header injection
- Response splitting
- Origin confusion and scheme/host trust errors
- DNS rebinding where relevant

### Browser/client

- Content Security Policy bypass/misconfiguration
- DOM clobbering
- Prototype pollution with security impact
- postMessage origin validation failures
- XS-Leaks/cross-origin information leaks
- unsafe URL schemes/open new-window opener attacks
- service-worker scope/cache abuse where applicable

### Input/resource exhaustion

- Regular-expression denial of service (ReDoS)
- zip/decompression bombs
- image/document parser bombs
- oversized JSON/form/multipart payloads
- algorithmic complexity attacks
- pagination/export/report amplification
- unbounded queue/job fan-out

### File/media/import/embed

- MIME confusion/content sniffing
- polyglot files
- malicious SVG/HTML upload
- metadata-based injection
- unsafe archive extraction / zip slip
- filename/path collisions
- executable file placement
- unrestricted iframe/embed origins
- malicious oEmbed/provider response
- external URL import SSRF and redirect-chain bypass

### Secrets/infrastructure/cloud

- overly broad Worker/service bindings
- D1/R2/environment binding exposure
- public bucket/object ACL mistakes
- secret leakage through logs, source maps, builds, screenshots or CI artifacts
- environment mixing (dev/staging/prod)
- orphaned preview/deployment URLs
- subdomain takeover / dangling DNS
- privilege escalation through deployment tooling
- CI/CD credential theft and artifact substitution

### Supply chain

- dependency confusion
- typosquatting
- compromised maintainer/package
- unpinned dependencies/toolchains
- lockfile tampering
- malicious install scripts
- build provenance gaps
- unsigned/unverified release artifacts
- vulnerable transitive dependencies
- stale/abandoned critical packages

### Data/privacy

- excessive collection/retention
- purpose/consent mismatch
- insecure backups/exports
- sensitive data in analytics/logs
- data residency/retention policy violations where applicable
- improper deletion/anonymization
- cross-client data leakage
- inference from metadata/identifiers

### Business/process abuse

- inquiry spam/automation
- email/SMS/provider cost amplification
- workflow state skipping
- approval/version tampering
- replaying stale approvals
- schedule/publish race abuse
- support/social engineering escalation
- abuse of exports/reports/bulk actions
- billing/payment/renewal manipulation when those modules exist

## Security completion rule

A release cannot state “security complete” from a generic scanner alone. Every applicable item must map to one or more of:

- architecture prevention/control;
- unit/integration negative test;
- browser/E2E abuse test;
- dependency/SCA result;
- configuration review;
- manual code review;
- dynamic security test;
- operational control/monitoring;
- documented not-applicable rationale.
