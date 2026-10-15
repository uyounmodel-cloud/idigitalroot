# Enterprise website and simpler CMS — 15 October 2026 (Asia/Beirut)

**PASS on the exact sealed source for the local gates below. Candidate, not owner-approved. Phase 1 OPEN; production release BLOCKED. Nothing deployed.**

Source: `IDIGITALROOT_CLARITY_SOURCE_2026-10-15_rc3.zip`
SHA256: `3d6f8d50510dbe0502c677995f87cf074412a3524528bba07cc81036d3aeb463`
325 files, 1,748,751 bytes. Root and component checksums passed after verification. Previous rc4 source/UI approvals remain preserved and do not transfer to these changed bytes.

The owner requested an enterprise futuristic public design and a much simpler, richer CMS, preserving content and distribution. The new visual system covers the homepage, supporting/product/editorial/inquiry pages, consistent cards and controls, and responsive EN/AR/light/dark treatment. Inter and Noto Arabic are self-hosted with pinned official provenance and SIL-OFL licenses; no visitor font-provider calls. Read docs/CLARITY_CHANGE_REPORT.md, CLARITY_OWNER_GUIDE.md, CLARITY_SECURITY_REVIEW.md and CLARITY_READING_CHECKPOINT.md. The editor now uses separate Edit content and Preview & publish views, searchable sections/page text, a phone section picker, readable fields and protected approved-photo cards. All 27 CMS areas remain available. Save & preview writes only a private version-checked draft. Publication still requires an explicit named page/language confirmation and the existing server authorization/CAS/review rules.

Frontend repairs cover empty toast, sticky header wrapper, tablet/mobile navigation and preserved utility controls, hero overlap, search focus isolation, Personal-menu Escape, concept-tab focus/scroll, section-local image binding and added sections on supporting pages. The image fix preserves protected template content and refuses unreferenced media. New exact hashes confirm the code-owned markup for all134 localized routes is unchanged from rc4. This is scoped evidence, not a claim to have found every possible defect.

| Gate | Exact-source evidence |
|---|---|
| Integrity/reproduction | Fresh ZIP extraction; full root/component hashes/CRC; clean pinned npm CI from the integrity-checked cache in offline mode. No lock/dependency changes. |
| Build/runtime | Astro0 errors/0 warnings/7 hints; official Cloudflare adapter14.3.3 server build; actual local workerd, D1, R2 and service boundaries. |
| Contracts/security |12 frontend tests, including134 template comparisons and media isolation/supporting-page binding; integration security6; backend53; analytics47; CMS22 Node cases/files including17 Access JWT cases plus inherited assertion suites. |
| Native/connected workflows | Smoke6, data/media/CAS/cron11, integrated public/CMS/inquiry/outbox/analytics13, negative12, global settings6: PASS. |
| CMS workflows | Retained Studio19 plus focused/frontend23 checks: exact saved preview, dirty-input guard, stale publication refusal, EN/AR independence, RTL, section/text search, phone picker, protected thumbnails, section photos and supporting-page drafts. Functional checks use normal CSP. |
| Responsive/browser |46 critical checks,12 additional home viewport/language cases at360/390/768/1024/1280/1600px, plus keyboard/control probes. No recorded uncaught browser errors in tested paths. |
| Broad inventory |134 localized route requests: 116 published200 / 18 intentional private404. 54 CMS views, 34 dialog probes, 90 public control probes, 77 internal destinations. Six unapproved bilingual legal destinations remain404 and block production. |
| Automated accessibility |0 reported violations in all published route views,54 CMS screen/language views, 16 focused CMS edit/preview desktop/phone views and 26 public mobile light/dark views. Axe-only injection bypasses CSP; functional/security checks do not. Incomplete/manual rules and conformance remain open. |
| Failure boundaries | Own backend group paused/resumed: controlled503/noindex with no internal detail, then200 recovery. No anonymous browser CMS/direct D1/R2 access. |
| Supply chain/production boundaries |Three strict Worker entries bundled using local dry runs, no fixture secret/local hook/direct CMS/raw R2 findings in the targeted output scan; dated advisory output and SBOM/provenance included. Not an exhaustive scan or zero-vulnerability claim. |
| Launcher/data continuity |Verified Linux x64 dependency bundle, actual cold/warm start/stop with registry unreachable, rc4 copy-only inheritance, retained older/new private drafts and unchanged original byte inventory. Nine copy/WAL/schema/symlink/priority/fallback tests. Owner Windows run UNVERIFIED. |

Core0001–0016 and Analytics0001–0002, all server-domain implementation files and dependency declarations/locks match rc4 exactly. Changed runtime rendering/private-preview bridge and UI code are identified in CHANGESET.json. No remote resource/account/secret/DNS/billing/spend change occurred. The cloud runner's read-only Wrangler identity is unauthenticated; this does not establish the owner's PC connection state and does not require re-login for local review.

## Limits and release gates

These are agent/self-verification results, not owner or independent/HQ acceptance. No WCAG conformance, full ASVS strong L2/applicable L3 or production readiness claim is made. The original151-title and345-ASVS matrices remain partial/external evidence; CLARITY_SECURITY_MATRIX.csv retains all151 owner titles in this delta review. Real Access/MFA/recovery, legal entity/jurisdiction/age/retention/exact bilingual legal approval, provider/Drive/PDF scanning, backup/restore/deletion/incident/alerts, full role/state/adversarial/manual accessibility and usability, load/performance/SEO and exact staging/action/credentials/spend authority remain open.

All12 Toolbox tools and16 Workspace positions remain mandatory first commercial student scope and presentation demos here. Admin/Client dashboards and future multi-edition operations are not operational. Public inquiry has no signup. A saved draft is private; publishing this package changes the local site only.

## Reproduction and chronology

Use a NEW source extraction and NEW empty test-data directory. Verify SHA256SUMS and component checksums. Run scripts/run-native.py with --frontend-node <22.19.0node> --backend-node <22.16.0node> --data-dir <NEW_EMPTY_DATA> --evidence-dir <NEW_EVIDENCE> --install --verify --full-browser. npm10.9.2, TypeScript5.8.3, Astro7.3.5, Cloudflare adapter14.3.3, Wrangler4.151.0 and Chromium154.0.8037.57 were used. Generated caches/runtime databases are excluded. The included bundle is bound to the unchanged package/lock and verified per file by preview_dependencies.py.

Run python3 CHECK_REVIEW_DATA.py --source <fresh source> to reproduce nine isolated synthetic copy checks. Actual operator cold/warm startup was tested separately. Earlier Studio data is preferred; the known rc9 fallback is used only when Studio data is absent. Versions are never merged or overwritten, and the original SQLite files are never opened during copying. The operator snapshots only staged copies to preserve WAL/sidecar bytes.

Development preflight caught a parse5 namespace type mismatch and an overly textual attribute-escaping assertion; the implementation now uses the parsed HTML namespace and the test checks parsed attributes. A new headless harness needed foreground activation before viewport changes. An attempted acceptance start safely refused occupied local ports; the old own audit runner was stopped before the actual fresh-extraction run. None of those provisional results are claimed as final PASS. The first sealed draft also prompted final content-direction and empty-editor refinements; the later owner clarification expanded presentation into an enterprise futuristic redesign; final rc3 repeats the full suite. Final exact-source evidence is under evidence/fresh-extraction and evidence/browser-and-native.

Independent/manual/owner Windows acceptance remains outstanding. Read INSTALLATION_GUIDE.txt for the bounded review workflow. Earlier baseline docs remain historical; the current owner direction allows better frontend presentation while protecting content/distribution.
