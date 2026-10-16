# Owner Decisions Consolidated Through 2026-10-14

This file contains the decisions Codex must treat as product authority unless superseded by a later explicit owner instruction.

## Product order and boundaries

- Personal iDigitalRoot first; university students are the first commercial audience.
- Business iDigitalRoot is a separate future product.
- Execution order remains: Public Website + dedicated Public Website CMS → Admin & Operations → Personal Client Panel → reusable Client Website CMS → client Public Website factory/template system.
- The dedicated Public Website CMS remains separate from the future Admin Dashboard.
- The Client Panel remains separate from every client website CMS.
- Each client website/CMS must be independently isolated in deployment/data/media/security/config rather than implemented as unsafe shared multitenancy.

## Owner-approved UI decisions

- Public Website v4.3 UI/content direction approved; no redesign without owner request.
- Public CMS v4.1 UI/UX approved; no redesign without owner request.
- Connected CMS v1.5.3 approved after the professional-editor repair.
- Normal CMS users must never be forced to edit JSON, stable internal keys, raw API payloads, DB identifiers or developer representations.
- Human-readable editors, WYSIWYG, media pickers, visual navigation/footer controls, translation UI, charts, tables and readable revision history are mandatory.
- Technical diagnostics may exist only in restricted Advanced/Diagnostics surfaces where genuinely useful.

## Language and localization

- English is LTR.
- Arabic is a complete RTL mirror, not partial direction flipping.
- CMS Arabic sidebar is on the right.
- Arabic Visual Editor: page tree right / canvas center / inspector left.
- CMS UI language and public-preview language are independent.
- Architecture supports Admin-managed additional locales later.

## Public website and lead rules

- No public self-signup in Phase 1.
- Inquiry is human-reviewed Lead intake.
- Keep a non-student inquiry path open without advertising internal roadmap language.
- Do not promise jobs, scholarships, rankings or guaranteed outcomes.
- Do not attack LinkedIn or similar services in marketing copy.

## Engineering and release rules

- Cloudflare-first unless a later explicit decision supersedes it.
- Astro + TypeScript public frontend; Workers; D1; R2.
- Ubuntu/WSL is the owner's local technical environment.
- No plugins.
- No Git workflow imposed on the owner for release review.
- Use immutable ZIP/SHA-256 release artifacts with fail-closed verification.
- Owner should not be required to debug engineering mistakes.
- Never fake acceptance, deployment, provider integration, analytics numbers, credentials or successful mutations.
- Production/provider/resource/credential/spend mutations require explicit owner authority.

## Content/security rules

- No arbitrary executable JS/CSS/SQL or unrestricted iframe content in CMS content.
- Rich content must be sanitized server-side.
- Embeds/providers are allowlisted and CSP-aligned.
- Media lifecycle requires validation/quarantine/finalization where applicable.
- Permissions and publication checks are server-side authority, never browser-only.
- Stable IDs are internal authority; visible labels and slugs are not authorization keys.
- Preview and publication must preserve version/concurrency/audit rules.

## Reusable client CMS rule

The future Client Website CMS is derived from the approved professional Public Website CMS core, but not by cloning iDigitalRoot-specific business content. Reuse the generic engine: content model, localization, media, publishing, revisions, preview, analytics presentation, SEO, roles/permissions and professional editor UX. Replace the site profile and blueprint-specific modules per client deployment.
