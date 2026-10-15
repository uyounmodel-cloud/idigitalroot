# Website Studio connected review — 15 October 2026

**Local technical verification: PASS on the exact sealed source. Owner approval/Windows acceptance: not recorded. Phase 1 remains OPEN; production release BLOCKED. Nothing deployed.**

Source: `IDIGITALROOT_WEBSITE_STUDIO_SOURCE_2026-10-15_rc4.zip`
SHA256: `f3d374b3e2922ffa355d21b0bbb3432302221d0481415be82cf4a2d0a4b46bdf`
311 declared files, 896,782 bytes. Source ZIP CRC, root and all four component checksums passed after the exact-source run. CMS2.0.0-rc.1. Previous rc9 source and original approved transfer remain untouched; approvals do not transfer to changed bytes.

The owner authorized rebuilding CMS UI/UX while keeping capabilities and restoring the approved v4.3 public visual baseline. Read docs/CMS_STUDIO_CHANGE_REPORT.md, docs/CMS_STUDIO_OWNER_GUIDE.md and docs/CMS_STUDIO_SECURITY_REVIEW.md. The root layout, artwork and content direction return to approved v4.3. Narrow readable-text contrast repairs remain; added header blur/hero decoration/card elevation are removed.

| Gate | Exact-source result |
|---|---|
| Fresh extraction + deterministic install | PASS; npm10.9.2 clean CI from the integrity-checked cache with offline registry mode, all lock/engine checks retained. No dependency changes. |
| Build/runtime | Astro check:0 errors/0 warnings/7 informational hints; official Cloudflare adapter14.3.3 server build; real local workerd/D1/R2/service bindings; EN/AR. |
| Contract/security suites | Frontend9; HMAC/scanner/component-registry parity6; backend53; analytics47; CMS22 Node cases/files including17 Access JWT cases and inherited assertion suites. |
| Native smoke / data workflows | 6 / 11 PASS; draft/privacy, media quarantine/reference delivery, translation, concurrency/replay and scheduling. |
| Integrated website/CMS | 13 PASS; actual editor save/private preview/review/publish/rollback, inquiry receipt/storage/outbox and consented analytics/CMS reports. |
| Dedicated settings UI | 6 PASS; target-bound settings, English/Arabic independence, typography and publication. |
| New Studio workflows | 19 PASS; search/filter, actual saved-design canvas, unsaved guard, same-screen publication/settings, stale review, independent languages/RTL, section shortcuts/limits/text/buttons, rich-text addition, cross-origin framing refusal and capability revocation. |
| Native negative paths | 12 PASS; origin/CSRF/method/size/property/writer/route/version/legal gates. |
| Responsive functional browser | 46 PASS; keyboard/menu/focus, EN/AR,360/1440px, theme and reduced motion; no runtime exceptions in tested paths. |
| Failure behavior | Own backend process paused: controlled503/noindex without internal detail; recovered200. |
| Automated accessibility |0 reported violations across 54 CMS screen/language views, 12 Studio desktop/phone views, 26 public mobile light/dark views and all116 published public route views. Axe injection alone uses CSP bypass/reduced motion; functional/security checks use normal CSP. Incomplete rules/manual assistive technology still open. |
| Broad route/control review | 134 localized requests:116 published200/18 intentional private404; 34 CMS dialog probes, 90 public control probes and 77 internal destinations; no recorded browser/click errors. Six unapproved bilingual legal destinations intentionally404 and block production. |
| Production boundary/supply chain |3 strict Worker entries bundled with local dry runs only; known local fixture secrets/hooks excluded from strict bundles/public client. Dated advisory output and SBOM included; not a zero-vulnerability claim. |
| Installer/data continuity | Sealed Linux x64 dependencies; real cold/warm launcher tests with registry unreachable; compatible older review copied into separate new folder, older byte inventory unchanged, inherited/new private drafts retained on restart; seven copy/rejection tests. Windows owner run unverified. |

Core0001–0016 and Analytics0001–0002 match the previous source exactly. Backend/CMS/analytics server implementation and authorization are unchanged; the preview response only permits same-origin framing with script/form-free sandboxing. See CHANGESET.json. New safe hero CTA renderer uses escaped text and the existing URL policy; code-owned action/layout keys are not editable.

## Evidence limits and open gates

Technical testing is self-verification, not independent/HQ or owner acceptance. No usability claim for a specific age group, WCAG conformance, full ASVS strong L2/applicable L3, production integration or security completion is made. Existing151-title/345-ASVS matrices retain partial/external evidence. Real Access/MFA/recovery, legal/age/retention/deletion decisions and exact bilingual approval, provider credentials/Drive/PDF scanning, backup/restore/incident/alerts, full role/state/adversarial/manual accessibility, load/performance/SEO and exact staging/provider action/spend authority remain open. No remote resource, DNS, Access, secret or billing change occurred.

The frozen locale-review rule still protects restoring an earlier publication: explicitly review the current language first. No draft is silently approved to bypass that rule. Template text is edited as text while code owns its presentation; rich-content sections provide safe formatting. Saved preview updates after saving and disables interactive forms/menu actions; full public behavior is tested on the connected public website.

All12 Toolbox tools and16 Workspace feature positions remain mandatory for the first commercial student release and presentation demos in this Phase1 candidate. Admin/Client dashboards and future multi-edition operations are not operational. No replacement commercial scope or fake edition selector was introduced.

## Reproduction

Extract the immutable source ZIP into a new directory. Verify SHA256SUMS and component checksums. Use pinned frontend Node22.19.0/server22.16.0/npm10.9.2 and Chromium154.0.8037.57, then run `scripts/run-native.py --frontend-node <pinned22.19node> --backend-node <pinned22.16node> --data-dir <NEW_EMPTY_DATA> --evidence-dir <NEW_EVIDENCE> --install --verify --full-browser`. The runner creates its evidence directory. The delivered Linux x64 bundle is bound to the unchanged frontend package/lock and verified per file by preview_dependencies.py. Start/stop/restart of OPEN_CONNECTED_PREVIEW.py was separately tested. Reproduce the seven local copy/WAL/rejection cases with `python3 CHECK_REVIEW_DATA.py --source <FRESH_EXTRACTED_SOURCE>`; it uses temporary synthetic data and prints its results without overwriting packaged proof. No owner review data is used for acceptance.

Provisional candidates were retained outside the download: rc1 exposed an inherited missing empty evidence-directory assumption; rc2 exposed old browser helpers not opening the new phone navigation; rc3 functional gates passed but new section numbering contrast failed. Preflight also confirmed the need for the prior narrow public text/brand contrast repairs and corrected page-editor context/section shortcuts. The initial outer-operator proof additionally caught SQLite read-only WAL connections updating sidecar bytes; the helper now snapshots only the already-copied database, and a committed-WAL preservation case plus cold/warm runtime proof were repeated. Final rc4 repeats all required gates from a fresh extraction; no assertion was disabled to obtain PASS.

Current evidence is in this report/VERIFICATION_SUMMARY.json/evidence. Older scope/phase documents are retained baseline authority; their previous rc9 references are not claims about the new source. Read INSTALLATION_GUIDE.txt to review on the existing Windows/Ubuntu WSL setup.
