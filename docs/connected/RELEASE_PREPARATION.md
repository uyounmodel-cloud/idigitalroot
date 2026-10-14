# P1-REL-01 — reviewable staging preparation, no deployment authority

Cloudflare Workers is frozen; Core D1 0001–0016 and Analytics D1 0001–0002 remain exact. The accepted Analytics component contains an older Core 0001–0014 test fixture, a byte-identical prefix; it is not the runtime bootstrap lineage. No 0017+ migration is added.

The three workers/wrangler.staging-*.template.json files are **unconfigured dry-run templates**. They contain placeholder hosts/resource IDs and strict production entrypoints. They are not commands to deploy. No local fixture identity, known local test secret or acceptance clock endpoint is permitted in a staging/production bundle. Website build uses the official Astro Cloudflare adapter. Workers deployment previews and workers.dev are disabled in these templates.

Before any provider mutation, record the exact account and staging environment, public/CMS/API hostnames and routes, existing D1/R2 binding IDs, Access application issuer/audience/individual users/MFA/fresh-auth policy, permission scopes, cron/rate-limit policy, storage/CPU/logging/billing limits, credentials mechanism and a spend cap. Choose managed secret bindings for PUBLIC_API_CONTEXT_SECRET (shared by frontend/API/analytics), PREVIEW_SECRET, RATE_LIMIT_HASH_SALT, VISITOR_HMAC_SECRET and SEARCH_HMAC_SECRET. Never paste their values into source, ordinary CMS fields or review artifacts. Verify the existing owner WSL Wrangler identity read-only before proposing changes; this cloud runner's unauthenticated status does not describe that PC.

The public API needs an owner-approved HTTPS API route reachable by the frontend Worker, or a separately reviewed service-binding transport. The current accepted HTTP transport is configured server-side with IDR_PUBLIC_API_BASE_URL and IDR_PUBLIC_SITE_ORIGIN. No route is silently provisioned by this package. Both internal and public sensitive intake boundaries require the signed abuse context.

Proposed staging sequence after explicit exact-action approval:
1. Verify selected source ZIP/hash and all checksums; reproduce clean installs/builds/browser gates.
2. Back up existing state; rehearse a restore and record RPO/RTO. Do not apply schema fixtures to owner data.
3. Verify exact Core16/Analytics2 lineage against existing databases read-only; stop on differences.
4. Provision/configure only approved isolated resources, keys, Access policies and routes. Enable scheduled publication only after permissions/clock/cancellation tests and an interruption-recovery runbook are accepted.
5. Publish a bounded review revision through real Access, test EN/AR, media, preview revocation, inquiry/outbox, consent and analytics, role revocation, exceptional paths and real provider interfaces.
6. Run integrated security/QA/operational gates and independent review. Record owner review and exact release decision; no self-test is independent acceptance.
7. Roll out only the approved environment/release, verify actual deployment IDs/traffic and be ready to roll back Worker version and publication pointer. Database rollback is a restore/recovery decision; never reverse frozen migrations casually.

No deploy, remote migration, bucket/DNS/Access/secret/billing change or production integration has been performed. Phase 1 release remains BLOCKED until its external decisions, provider tests and independent acceptance are evidenced. Phase 2 has not begun.
