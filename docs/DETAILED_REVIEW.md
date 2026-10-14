# iDigitalRoot public website and CMS: detailed revision

**Review status: completed with the coverage and limitations below. Release status: BLOCKED.** The approved design direction is preserved. This review found real functional defects; the existing previews must not be treated as the finished student product.

## Owner notes recorded as current requirements

1. One public-CMS entry point must eventually manage distinct audience editions, with an explicit edition choice and complete context scoping. Similar headings/templates should be reused while content, services and approved presentation differ.
2. The customer account keeps a common structure, with audience-specific presentation and services. A student becoming an employee must retain their account, history and purchased services. One account may own sites for different audiences.
3. The owner explicitly chose **all 12 Toolbox tools and all 16 Student Workspace features as required for the first commercial student release**. These are not later add-ons and are not currently implemented by the public presentation previews.
4. Authorized central Admin manages all editions and the service catalogue. Individual staff identities and scoped permissions remain mandatory; “Admin sees everything” does not grant every staff member unrestricted access.

Read [AUDIENCE_EDITION_ARCHITECTURE.md](AUDIENCE_EDITION_ARCHITECTURE.md) for the scope/architecture and [STUDENT_LAUNCH_SCOPE.md](STUDENT_LAUNCH_SCOPE.md) for every service/tool/feature and its minimum acceptance requirements. The proposed architecture has not been presented as implemented or owner-approved in all technical details.

## Review baseline and authority

- Approved public v4.3 UI: `d10b1cff47d5912fecb49d88579971f3e21bb19a33b179e29356ea0eac5646fd`.
- Approved CMS v4.1 UX: `7f7e099e3c525b27dd8ee285410ad0a9ce71c5055d845219c40a8501f8ee60cf`.
- Approved connected CMS v1.5.3: `62f9e7441372b825d4e8535febdf7679d09d9a39464a8f63843f1eadd5c6d257`.
- Website review baseline: sealed v1.1.2r6 CANDIDATE, `677ea259a49364c3f4e8db976c7fa4ac60b8f86c5ba48c7e825184f15e79facd`, with the existing bounded backend successor carried in its test authority.
- Current repair candidates: frontend v1.1.2r9 and CMS v1.5.4-r1. **Neither is owner-approved or independently accepted.** Exact ZIP hashes are in INTEGRITY_AND_LINEAGE.json and release checksums.
- Original transfer and approved ZIPs remain intact. No source authority was silently replaced.

Cloudflare Workers/D1/R2 and the owner's Windows + Ubuntu/WSL environment remain the frozen targets. Tests here use local workerd and synthetic SQLite/R2-compatible/provider fixtures. The owner confirmed the Windows previews opened; that is startup evidence, not full workstation acceptance or verification of the owner's Cloudflare identity. No Cloudflare/provider mutation or deployment occurred.

## Coverage and what the evidence means

| Review activity | Actual coverage |
|---|---|
| Public route registry | All 67 registered paths, in EN and AR: 134 browser requests |
| Route availability in the supplied preview fixture | 106 HTTP 200; 28 controlled HTTP 404 |
| Public link destinations | All 98 unique internal hrefs observed: 88 available, 10 unavailable |
| Public controls | 144 distinct locale/control-parameter cases clicked; no click-operation failures; two original Root Check runtime exceptions reproduced |
| CMS workspace surface | All 27 workspaces in both UI languages: 54 views inventoried |
| CMS dialogs/actions | 35 representative dialog/action probes, including page/navigation/footer/translation/service/SEO/media/provider/publishing/analytics/user controls |
| Source declarations | 156 control declarations, 130 distinct declarations, with source/binding traceability |
| Automated accessibility | axe-core 4.14.0, WCAG A/AA tags through WCAG 2.2, on available public pages and all CMS workspace views |
| CMS repair regressions | Successful translation-section preservation, replacement-dialog visibility and product-editor opening on fresh extracted candidate source |
| Frontend repair acceptance | Fresh ZIP extraction, clean pinned install, Astro check, official adapter build, workerd, 53 backend checks, seven renderer tests and 87 real browser checks |
| Existing CMS verification | Core/service/schema/parity suites passed; updated UI static, integration and browser suites passed; native CMS workspace/repair checks supplement the inherited browser harness |

This is a complete inventory/source review and a broad functional sweep. It is **not** evidence that every confirmation, role, malformed input, concurrency case, provider state and browser/device combination passed. Dialog opening does not establish mutation success. Conditional controls and unexecuted states are explicitly distinguished in CONTROL_TRACEABILITY.csv. Full integrated QA and adversarial security acceptance remain open.

Accessibility injection used Chrome's test-only CSP bypass to load the auditing library; this is recorded as instrumentation, not evidence that production CSP can be bypassed. Normal frontend workerd acceptance runs preserved the application CSP. Automated accessibility results do not replace keyboard, screen-reader, contrast/theme and visual review.

## Confirmed repairs in separate candidates

| Finding | Repair and verification |
|---|---|
| Successful Arabic translation could discard page sections | Original UI sent `sections: []`. Reproduced a successful 201 save changing one section to zero. Candidate obtains the exact revision through the existing protected-preview contract and preserves target sections; fresh candidate save retained one section |
| Successful YouTube normalization closed its new result dialog | The old dialog's confirmation callback cleared the replacement dialog. Candidate closes only its own dialog; the actual successful result remains visible |
| Content lists silently stopped at 50 records | Candidate follows the existing paginated API, with a bound and explicit incomplete-list failure instead of silent truncation; product initialization refreshes the list |
| Several editors referenced undefined `selectedLanguage` | Candidate consistently uses the defined editing locale while retaining independent CMS UI and preview language state |
| Chapter component choice could fall back to the first section | Candidate resolves a matching component or instance identifier when it exists; missing sections are still a content/profile gap, not proof every chapter is editable |
| Dialog confirmation ignored normal form validity and could leave rejection disabled | Candidate checks form validity, re-enables rejected confirmation and preserves the replacement-dialog lifecycle |
| Root Check “See example” raised `sampleReport is not defined` in EN and AR | Added a clearly illustrative methodology panel. Browser tests prove open/close, no fetched domain and no fabricated score. The live scanner remains gated |
| Dynamic Arabic search links returned English URLs; Escape lost trigger focus | Candidate localizes generated links, traps Tab in the search dialog and restores trigger focus; real workerd checks passed |
| Service buttons used unsupported selected semantics; some names omitted visible labels | Candidate uses pressed semantics and includes visible card/brand/language text in accessible names; Arabic skip text is localized |
| CMS labels, target sizes, focusable scrolling and contrast failed automated checks | Bounded label associations and a separate accessibility stylesheet preserve the original layout. Baseline had 126 violation-category occurrences across 54 views; the final candidate sweep had zero. This is not a full WCAG conformance claim |
| CMS date formatting called an undefined method | Candidate uses locale-aware `toLocaleString` |

Backend TypeScript, compiled backend/schema authorities and migrations are unchanged in the CMS candidate (86 checked files). The frontend's approved CSS, frozen fixtures and dependency lock remain byte-identical to r6. The original approved packages remain available.

A first internal frontend repair ZIP failed its source gate because the packaging script omitted nested backend checksum manifests. That ZIP was not published. The corrected ZIP preserves those manifests and passed fresh-source verification. No expected checksum or assertion was weakened to hide that failure. The CMS main-focus static assertion was updated for the intended keyboard-focusable main landmark.

## Release blockers and remaining functional gaps

| Priority / area | Finding and required closure |
|---|---|
| High — edition scope | Current CMS binds one site/profile. There is no safe multi-edition selector, authorization, publication/media/analytics/cache partition or cross-edition acceptance. A cosmetic dropdown would be insufficient. Implement the documented gateway/profile contracts before enabling future editions |
| High — component binding | CMS exposes 46 active families; frontend accepts 30, with 23 CMS families absent from its allowlist. Examples include rich_text, image/gallery/video, cards/CTA, root-toolbox and major-explorer. The frontend fails closed, but ordinary CMS-created content cannot all render. Align registries, schemas, composition and real CMS -> public tests |
| High — navigation/footer | Frontend mainly relabels an existing matching href. It does not fully apply added/removed/reordered menu items. CMS footer groups are not structurally rendered by the current items-based shell overlay. Test actual published structure changes, EN/AR and cache validators |
| High — public product/service/settings binding | Product registry and appearance/brand settings can be saved in CMS, but much public content/design remains code-owned fixture output. Verify each supported editor field reaches the public site; do not claim CMS control from successful storage alone |
| High — generic pages and articles | A new arbitrary page does not have complete registered component rendering. Knowledge creation currently creates the record/taxonomy without a complete ordinary article-body/locale/revision authoring path. Establish the contract and actual create/edit/preview/publish workflow |
| High — translation/locale creation | Existing locale-state translation is repaired; a newly created EN-only page still needs a supported initial AR locale-state workflow. Additional locales have registry controls but current runtime validation is EN/AR-bound. Do not enable unsupported locales |
| High — Arabic create flows | Internal keys are derived from titles using Arabic characters while several backend key contracts permit ASCII only. Arabic-titled creation needs automatic valid internal identifiers and preserved human names; ordinary editors must not work around database keys |
| High — public search | Search UI still searches the frozen route index instead of the accepted published-only backend search. The locale correction does not close this data-binding gap |
| High — Knowledge navigation | Six category paths are treated like article-detail paths by the current loader. The preview has 12 category 404s. Six un-published prototype articles add 12 more 404s; home cards still link to sample article slugs. Use actual published lists/taxonomy and truthful empty states |
| Expected gate — legal | Privacy and Cookies lack approved published content, producing four localized 404s and broken footer destinations in the preview. Fail-closed delivery is correct; legal content/approval and usable release navigation must be completed |
| High — inquiry behavior | A valid preview “Continue” changes the URL but leaves the displayed step unchanged under the current published-bound render path. Live submission remains deferred to FE-03. Implement the accepted definition, state/validation, real POST, consent, abuse controls and truthful outcomes |
| High — analytics | Real browser collection is disconnected. CMS fixture reports are not live visitor analytics. Dashboard preparation can mask some service failures as zero/healthy/stale values. Implement collection/privacy and explicit unavailable/stale reporting |
| High — visual preview/page tree | Editor language controls currently change preview direction without independently loading all selected-language content. The visual page tree primarily uses the content list rather than the saved hierarchy. Exact-version preview returns service data; full approved public-renderer preview still needs integration |
| High — normal editing completeness | Some structured arrays cannot add/remove entries through ordinary fields. Knowledge “Edit” primarily exposes taxonomy; several richer content/provider/media workflows need real user-path verification. Preserve professional controls while completing these paths |
| High — permission-aware CMS UI | The owner fixture signs in as root. Sidebar/actions do not yet demonstrate permission-aware rendering for every ordinary editor role. Server denial tests do not establish appropriate UI behavior or all production role flows |
| High — provider/production assembly | CMS Worker production entry/static-asset/verified Access construction and bindings need integrated release assembly. Provider demos are local adapters. Production Drive import currently asks for a raw access token; replace that ordinary-editor flow with an approved managed authorization contract |
| High — public accessibility | Existing public contrast failures remain on light/cream/dark panels. The frozen public CSS was preserved; valid pressed/name fixes do not close contrast, full keyboard/screen-reader, theme or visual parity gates |
| Launch gate — account/tools | Client login, Admin and Client Account remain planned. All 12 Toolbox and 16 Workspace positions are now mandatory commercial scope, but are presentation-only in the public preview. Design, implement and verify them in the defined later-phase product domains |
| Release gates | Full P1-FE-02 acceptance, FE-03, integrated SEC/QA/release, owner workstation reproduction, verified provider/staging behavior, legal/privacy/retention, backup/restore and release authority remain open |

The 28 route 404s are therefore not 28 independent source defects. They include deliberate legal/publication gates, unpublished sample content and a category-loader contract gap. See PUBLIC_ROUTE_MATRIX.csv and PUBLIC_LINK_AUDIT.json for every path/status.

## Sequence after this review

1. Preserve the approved UX and reviewed repair evidence; candidates remain unaccepted.
2. Close the remaining Phase 1 content/component/navigation/footer/search/locale/preview binding gaps using one integrated local CMS -> backend -> built public-site harness. Prove draft invisibility, safe media, updates without inappropriate rebuild, rollback, failure states and exact-source reproduction.
3. Close inquiry/browser analytics under accepted contracts, then integrated security, product/visual/a11y QA and release preparation.
4. Build Admin authority and operations before the Client Account. Implement the owner's mandatory student product modules with durable private data and the acceptance matrix; preserve ordinary website content in its CMS.
5. Deliver reusable isolated client CMS and controlled website factory in the frozen order. Use the common edition/profile architecture, rather than unrelated product forks.
6. Commercial Student Edition launch occurs only when its full promised package and needed delivery dependencies pass acceptance. Exact prices, limits, paid provider costs, export/share formats, notifications, health guarantees and privacy/retention remain decisions at their material gates.

No new provider resource, paid service, migration 0017+, public signup or deployment was added. The next technical task is Phase 1 binding closure; this report is not permission to release any environment.
