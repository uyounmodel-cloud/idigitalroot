# Security Standards Reference — checked 2026-10-14

This file records the external standards baseline that Codex should consult from official sources when implementing/security-reviewing iDigitalRoot.

## OWASP ASVS

- Current stable referenced by this package: **OWASP ASVS 5.0.0**.
- Purpose: detailed verification requirements for web application technical security controls and secure development.
- Official project: https://owasp.org/www-project-application-security-verification-standard/

## OWASP Top 10

- Current released version referenced by this package: **OWASP Top 10:2025**.
- Categories: Broken Access Control; Security Misconfiguration; Software Supply Chain Failures; Cryptographic Failures; Injection; Insecure Design; Authentication Failures; Software or Data Integrity Failures; Security Logging & Alerting Failures; Mishandling of Exceptional Conditions.
- Official: https://top10.owasp.org/2025/

## OWASP API Security Top 10

- Stable edition referenced: **2023**.
- Official: https://api-security.owasp.org/editions/2023/en/0x11-t10/

## NIST SSDF

- Final baseline used by this package: **NIST SP 800-218 SSDF v1.1**.
- NIST also lists **SP 800-218 Rev.1 / SSDF v1.2** as draft (released 2025-12-17). Treat it as informative until final unless the project explicitly adopts the draft.
- Official: https://csrc.nist.gov/projects/ssdf

## Cloudflare

Use current official Cloudflare documentation for Workers, Access/Zero Trust, D1, R2, WAF, secrets and deployment configuration at implementation time. Access is an additional access-control layer and does not replace application-level authentication/authorization.

- Workers + Access: https://developers.cloudflare.com/workers/configuration/cloudflare-access/
- Cloudflare docs root: https://developers.cloudflare.com/
