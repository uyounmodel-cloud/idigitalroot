> Current owner-directed UI successor: see CMS_REBUILD_AUTHORITY.md, CMS_STUDIO_CHANGE_REPORT.md and CMS_STUDIO_OWNER_GUIDE.md. New CMS2.0.0-rc.1 is a candidate, not owner-approved. Original hashes/approvals below are preserved.

# Connected Phase 1 candidate — feature status

This is a bounded successor for owner review. The original approvals remain authoritative. Opening this build does not approve it or close Phase 1. Final exact-source evidence is delivered alongside the source ZIP.

| Area | Candidate behavior | Release boundary |
|---|---|---|
| Public design | Approved v4.3 layout/artwork/content direction retained; additive glass/mesh/card/focus/responsive/reduced-motion refinements; light-surface contrast repaired | Owner visual acceptance and manual assistive-technology review required |
| CMS authoring | Human names, page/article title/introduction/body, rich editor, full editorial-text fields, visual sections, repeatable fields, ordering, visibility, translations | EN and AR remain separate; no automatic English publication into Arabic |
| Publishing | Save draft → immutable review-ready version → publish, unpublish, retained rollback, pointer conflict handling and audit | Drafts remain private; legal content also requires an explicit recorded owner decision |
| Scheduled publishing | Fresh authorized publisher schedules an exact ready revision; cron rechecks active creator permissions and the publication baseline; single claim; cancellation and conflicts are explicit | Production cron disabled in templates until authorized. Interrupted EXECUTING work requires reconciliation; never blindly retry a publication |
| Shared website/CMS | Website reads published records from the same local D1 data and media boundary used by CMS | The older separate preview packages remain historical and do not become connected automatically |
| Navigation/footer | Published menu/group content, order, safe destinations and independent translations bind to the website | Edition-wide routing and authorization are future architecture, not a working edition chooser |
| Brand/services/product presentation | Code-projected public fields and reviewed presentation records; shared appearance uses approved numeric presets | Product presentation cannot grant entitlements. New functional capabilities need reviewed code |
| Knowledge/search | Published articles and categories, body rendering, published-only search and localized destinations | Seed prototype articles are intentionally unpublished |
| Inquiry | Accepted eight-step contract, validation, contact permission, real lead/answer/outbox writes, stable retries and truthful receipt; CMS wording/options drafts and version publishing | No signup. Lead operations belong in later Admin; this CMS is not a CRM. Email/SMS notifications are not configured |
| Analytics | Explicit per-page opt-in, cookieless events, no persistent visitor/session ID, DNT/GPC honored, public API → local D1 → authorized CMS reports/export; scheduled outbox replay | Production privacy/retention/collection decision remains open. Aggregate windows close on cron; current-hour data is not falsely shown as completed rollups |
| Local media | Real local R2 quarantine, PNG/JPEG structural validation, separate approval/finalization, published-reference-only delivery, metadata, private draft previews | PDF stays quarantined without the approved scanner service. Production R2 permissions and real provider behavior need staging verification |
| Drive/PDF/YouTube | Managed server authorization/scanner interfaces fail closed; editor never enters raw Drive tokens. YouTube references are validated; public rendering uses safe external links | Real Drive authorization, scanning service and inline third-party playback/privacy are not verified/enabled. These are explicit release gates, not simulated successes |
| Identity/roles | Production entry verifies Access JWT signature/issuer/audience/time and current CMS actor/session/permissions; local entry is a separate fixture-only loopback boundary | Real Access/MFA, recovery and account policies require provider verification. The local “Sign in” is not production authentication |
| Legal/operations | Exact legal-approval manifest is empty, publishing is gated; failures are explicit; source/lock/manifests and local reproduction are provided | Legal approval, retention/deletion, alerts, backup/restore, load/abuse and independent security acceptance remain required |

## Product and edition boundaries

This candidate implements the Public Website/CMS phase. Admin and the Client Account are not operational here. All 12 Toolbox tools and all 16 Student Workspace feature positions remain mandatory for the first **commercial student release** and are currently public presentation demos. A career kit is shared between those two navigation areas. This candidate must not be sold or described as that completed commercial product.

Future employee, entrepreneur and business editions should use a common scoped CMS entry, shared account model and per-edition content/service profiles. The architecture in AUDIENCE_EDITION_ARCHITECTURE.md is preserved. A cosmetic edition dropdown without data/permission/route isolation is not enabled. Phase 2–5 remain in the frozen order.

## Owner review

Use the connected launcher, save a small page-text draft, verify the website does not change, choose “Review complete — ready to publish”, publish, then refresh the website. Test EN and AR separately. See INSTALLATION_GUIDE.txt in the outer package. This review is local and does not authorize any deployment.
