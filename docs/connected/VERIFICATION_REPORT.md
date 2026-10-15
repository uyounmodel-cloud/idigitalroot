# Horizon 01 — structural public/CMS redesign

**Local exact-source gates PASS. Unaccepted candidate. Phase 1 OPEN; production release BLOCKED. Nothing deployed.**

Source `IDIGITALROOT_HORIZON_SOURCE_2026-10-15_rc3.zip` — SHA256 `b380a611a1f7af5d2784c213503d01c23806f658960e174b675d7f826e6b40bd`. 333 source files; 1,818,990 bytes. Root and component checksums checked after verification.

The owner rejected the preceding Clarity design as unchanged. This iteration replaces the public split opening with central typography above a wide connected-system graphic and changes the navigation/cover/card system. CMS desktop navigation is horizontal; page cards open a real saved-page canvas beside one editing card. Compact section selection and optional search replace the always-visible section rail. Phones prioritize editing above the saved canvas. Read HORIZON_CHANGE_REPORT, HORIZON_OWNER_GUIDE and HORIZON_SECURITY_REVIEW under docs. Page-card illustrations are explicitly labelled; they are not claimed as screenshots of current drafts. Screenshots in screenshots/ were captured from this exact operator on isolated synthetic copied data, with no publication for screenshot preparation.

| Gate | Observed result |
|---|---|
| Reproduction | Fresh ZIP extraction/CRC, pinned clean npm CI from integrity-checked offline cache; 34 runner steps PASS. No dependency or lock changes. |
| Build/runtime | Astro0 errors/0 warnings/7 hints; official Cloudflare adapter14.3.3 server build; actual local workerd/D1/R2/service bindings. |
| Content preservation | All134 EN/AR templates compare equal for every word, heading hierarchy, link destination order and CMS section order against sealed Clarity rc3. Unlike the archived exact-HTML gate, this permits the authorized markup redesign. |
| Domain/security contracts |12 frontend cases,6 integration-security cases; backend53; analytics47; CMS22 Node cases/files including17 Access JWT cases and inherited assertions. Existing object/property/function authorization, review/CAS and failure boundaries unchanged. |
| Connected flows |Native smoke6, native workflows11, integrated inquiry/outbox/analytics/publishing13, negative12, global configuration6: PASS. |
| CMS/design workflows |19 Studio and 24 Horizon checks PASS, including exact saved preview, canvas selection, unsaved guards, language isolation, stale publication refusal, section photos, protected thumbnails, text search, added supporting-page drafts, build identity and actual preview/header parity. Normal CSP retained. |
| Responsive/keyboard |46 critical checks plus12 additional home viewport/language views at360/390/768/1024/1280/1600px; no recorded exceptions in tested paths. |
| Broad inventory |134 localized public requests: 116 published200, 18 intentional private404; 54 CMS language/workspace views; 36 dialog probes; 90 public controls; 77 internal destinations. Six bilingual unapproved legal destinations remain404 and block production. |
| Automated accessibility |No reported violations in tested published routes/CMS views, 16 edit/preview desktop/phone views and 26 public mobile light/dark views. Axe injection alone bypasses CSP. Incomplete/manual rules and conformance remain open. |
| Controlled failure |Own backend paused:503/noindex/no internals, then200 recovery. Draft/private content invisible; public browser has no CMS or direct D1/R2 path. |
| Supply chain/boundaries |3 strict Worker local dry-run bundles, targeted fixture-hook/secret/CMS/raw-R2 output scan PASS. SBOM/advisory/provenance included. This is not exhaustive scanning, provider verification or a zero-vulnerability claim. |
| Launcher/data continuity |Actual cold/warm starts/stops with registry unreachable; Clarity copy-first inheritance; old/new private drafts retained; original byte inventory unchanged.10 synthetic copy/WAL/schema/symlink/priority/fallback checks PASS. Owner Windows run UNVERIFIED. |

All server-domain files, Core0001–0016, Analytics0001–0002 and dependency declarations/locks match the preceding sealed candidate. Changed presentation/private-preview bridge/tests are listed in CHANGESET.json. Existing self-hosted Inter/Noto Arabic font provenance/licenses are retained. The cloud runner's Wrangler identity is checked read-only; an unauthenticated cloud result does not establish the owner's PC connection state. No forced login, provider resource/secret/DNS/billing mutation, deployment or spend occurred.

## Limits and remaining gates

These are agent/self-verification results, not owner or independent/HQ acceptance. The design itself is not owner-approved. The151 owner security-title mappings and345 ASVS requirements retain their prior partial/external status; HORIZON_SECURITY_MATRIX adds the presentation evidence without promoting inherited coverage. ASVS5.0 strong L2/applicable L3, Top10:2025, API Top10:2023 and final SSDF1.1 remain authorities.

Real Access/MFA/recovery, legal entity/jurisdiction/age/retention/exact bilingual legal approval, providers/Drive/PDF scanner, full role/adversarial/manual accessibility and usability, load/performance/SEO, backup/restore/deletion/alerts/incident exercises and exact staging/action/credentials/spend authority remain open. Review-build markers must be removed and the release reverified before an authorized production release. All12 Toolbox tools and16 Workspace positions remain mandatory commercial scope and presentation demos; Admin/Client/future multi-edition dashboards are not operational. No public signup was added.

## Reproduction and provisional findings

Verify source SHA/CRC and SHA256SUMS.txt after a fresh extraction. Run scripts/run-native.py --frontend-node <Node22.19.0> --backend-node <Node22.16.0> --data-dir <NEW_EMPTY_DATA> --evidence-dir <NEW_EVIDENCE> --install --verify --full-browser. npm10.9.2, TypeScript5.8.3, Astro7.3.5, adapter14.3.3 and Wrangler4.151.0 are pinned; exact Chromium/Python/platform details are in evidence/fresh-extraction/PROVENANCE.json. Never run acceptance against owner review data. Outer OPEN_CONNECTED_PREVIEW.cmd uses native WSL and the checksum-bound Linux x64 dependency bundle. CHECK_REVIEW_DATA.py --source <fresh-source> exercises the ten isolated copy cases. Reopening the same candidate reuses its data and verified dependencies.

An initial acceptance start safely refused occupied own development ports; the development runner was then stopped. Provisional rc1/preflight found a hidden duplicate Home link, RTL mobile drawer specificity, obsolete layout/selector assertions, a horizontal tool menu covering newly opened settings, and contrast failures in the new light/dark canvases. Those were repaired before sealing rc3. Media preflight initially omitted the native R2 fixture step; the full ordered native workflow was restored. Final evidence above repeats the full suite from sealed rc3 with fresh data. No provisional FAIL is presented as final PASS. Owner Windows/manual/independent acceptance remains outstanding.
