# Cross-System Identity, SSO and Authorization

## Identity classes

1. Anonymous public visitor.
2. Public lead/contact identity (not an account by default).
3. Public CMS staff/editor identity.
4. Internal Admin staff identity.
5. Client Account customer identity.
6. Client Website CMS identity/role.
7. Service-to-service/workload identity.
8. Break-glass/emergency privileged identity where formally approved.

Do not conflate these classes.

## Authentication principles

- MFA mandatory for privileged staff; strong phishing-resistant methods/passkeys preferred where supported.
- Passwords, if used, follow current secure hashing and breached/common-password controls.
- No shared accounts.
- Recovery cannot bypass core authorization/security checks.
- Session rotation after login/elevation; idle and absolute expirations appropriate to risk.
- Secure cookies: HttpOnly, Secure, appropriate SameSite, minimal domain/path scope.
- No auth/session secrets in localStorage when avoidable; do not design around browser-readable bearer tokens without a compelling reviewed reason.
- Revoke sessions on security-sensitive account changes.
- Rate-limit login/recovery/MFA challenges and protect against credential stuffing/account enumeration.

## Authorization principles

Check authorization on the server at:

- object level (BOLA/IDOR);
- property level (mass assignment/excessive exposure);
- function/action level;
- tenant/site/account scope;
- publication/workflow state;
- role/permission/scope;
- current version/concurrency when required.

Never authorize by hidden UI controls, slug/domain, client-supplied role, or predictable IDs.

## Client Panel → Client CMS SSO

- signed, tamper-evident;
- unique nonce/jti;
- single use;
- very short TTL;
- explicit issuer and audience;
- exact website/site ID;
- exact client user ID;
- minimal permission/scope;
- replay registry or equivalent one-time consumption;
- issuance and redemption audit;
- fail closed on expiry/replay/wrong audience/wrong site/signature/disabled user;
- no reusable password or long-lived bearer credential in URL.

## Public CMS / Admin network access

Where Cloudflare Access/Zero Trust is used, treat it as an additional perimeter policy, not a substitute for application authorization. The application must still validate identity/session/permission and must not trust arbitrary spoofable headers outside the verified Access boundary.
