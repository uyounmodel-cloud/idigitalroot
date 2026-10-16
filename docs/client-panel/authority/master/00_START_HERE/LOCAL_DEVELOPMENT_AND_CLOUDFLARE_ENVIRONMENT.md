# Local Development + Cloudflare Hosting Environment — Owner-Frozen Baseline

**Recorded:** 2026-10-14  
**Authority:** explicit owner environment/hosting decision for continuation in Codex.

## 1. Hosting/runtime choice is already decided

iDigitalRoot is **Cloudflare-first**. Unless the owner explicitly approves an architecture change, Codex must preserve the following production target:

- **Application/server runtime and hosting:** Cloudflare Workers.
- **Public Website rendering:** Astro + TypeScript using the official Cloudflare adapter and Workers/workerd-compatible server output.
- **Relational persistence:** Cloudflare D1.
- **Object/media storage:** Cloudflare R2.
- **Edge delivery/security:** Cloudflare CDN/WAF/rate limiting/bot/security controls where appropriate.
- **Privileged perimeter protection:** Cloudflare Access / Zero Trust where accepted, in addition to—not instead of—application authentication and authorization.
- **DNS/domain/provider configuration:** Cloudflare where the accepted architecture assigns it.

Do **not** migrate the project to Vercel, Netlify, AWS, Azure, Firebase, a VPS, Docker hosting, or another production platform merely because it is convenient for Codex. Such a change requires explicit owner approval and a documented architecture/security migration decision.

## 2. Owner workstation is the normal local test environment

The owner has already prepared a Windows workstation with **Ubuntu under WSL/WSL2** for this project. Previous accepted/local runs were performed in WSL. Treat this as the primary local development/test environment rather than asking the owner to install a new stack by default.

Recent observed toolchain during the latest owner-run FE closure work:

- Ubuntu/WSL available;
- Node.js **v24.21.0** observed;
- npm **11.19.0** observed;
- Windows can launch bounded `.cmd`/PowerShell wrappers which hand off to WSL;
- browser-driven acceptance can run using a WSL-compatible Chrome/Chromium/Chrome-for-Testing path when required.

Codex must inspect the actual current machine/tool versions before relying on them. Do not unnecessarily reinstall or replace a working toolchain.

## 3. Cloudflare account connection already exists

The owner states that this PC/WSL environment has already been connected/authenticated to the relevant Cloudflare account.

Codex must therefore:

1. **verify the existing connection read-only first** (for example with the current Wrangler identity/account inspection command such as `wrangler whoami`, using the project-pinned Wrangler where practical);
2. do **not** force a new login if the existing authenticated session is valid;
3. do **not** print, export, copy or request long-lived Cloudflare API secrets if the existing secure Wrangler session is sufficient;
4. treat successful account authentication as **connectivity only**, never as deployment/provisioning authority.

If the existing session is unavailable or expired, explain the exact bounded authentication step needed. Do not ask for raw API tokens in chat unless a provider workflow genuinely requires one and a safer interactive/session method is unavailable.

## 4. Local testing is required and should precede Cloudflare deployment

The project is specifically intended to be buildable and testable on the owner's PC before any deployment.

The default engineering loop is:

1. work in native Linux/WSL storage where runtime/tooling reliability requires it (prefer `/home/...` or a temporary native WSL staging directory over `/mnt/c/...` for execution-sensitive runs);
2. perform deterministic dependency installation from the pinned lockfile;
3. run type/static/schema/security checks;
4. run unit/integration tests;
5. run local D1/R2/provider-shaped fixtures or supported Wrangler local bindings where appropriate;
6. build the exact Cloudflare Workers target;
7. run the built Cloudflare application locally under **workerd** / the official Cloudflare-compatible preview path;
8. execute real browser regression against localhost, including EN/AR, RTL/LTR, accessibility, responsive behavior, auth/authorization negative paths, content publishing behavior and console/runtime-error checks;
9. perform fresh-extraction reproduction on the exact sealed source;
10. only after local acceptance and explicit owner authorization may staging/provider mutation/deployment occur.

For the current Astro public frontend, the Phase 1 closure specifically requires the official Cloudflare adapter, built application execution under Cloudflare workerd, and real-browser verification of that built result.

## 5. Local testing must not silently become production mutation

The following are distinct states:

- **local test** — allowed as part of engineering;
- **read-only Cloudflare identity/config inspection** — allowed when needed to understand the connected environment;
- **remote staging mutation/deployment** — requires explicit owner authorization for the bounded action/environment;
- **production mutation/deployment/DNS/secret/spend changes** — requires explicit owner authorization and release gate evidence.

Never interpret “the Cloudflare account is already connected” as permission to deploy, create/delete Workers, alter D1/R2, modify DNS, change Access policies, rotate secrets, enable paid services, or mutate production.

## 6. Expected Cloudflare development model

Codex should preserve a workflow in which the same application can be validated locally using Cloudflare-compatible runtime semantics and later deployed to Workers with environment-specific bindings/configuration. Provider-specific behavior that cannot be proven locally must be called out and tested in an explicitly authorized staging environment before production release.

No browser may receive direct D1 or R2 credentials. Browser/public applications talk to bounded server/API seams; Workers own privileged bindings.

## 7. Owner workflow constraints

- No plugins are required for project continuation.
- Do not require Git as an owner-facing release workflow unless the owner explicitly changes that decision.
- Keep immutable ZIP + SHA-256 handoffs/releases where used by the project.
- The owner should review bounded builds and approve decisions, not debug infrastructure/tooling failures.
- If a local launcher/test fails, Codex should diagnose and repair it rather than sending the owner through trial-and-error setup steps.

## Required Codex checkpoint statement

Before making source changes, Codex must explicitly acknowledge in its reading checkpoint:

> **Hosting target: Cloudflare Workers. Data/storage: D1 + R2. Local development/test target: owner's existing Windows + Ubuntu/WSL environment, with local workerd/Cloudflare-compatible runtime and browser verification before deployment. Existing Cloudflare account authentication should be verified read-only and reused if valid. Existing account connection does not grant deployment or production-mutation authority.**
