# Connected website/CMS candidate rc9 — verification report

Local technical status: **PASS on the exact sealed source**. Phase 1 release status: **BLOCKED** pending provider/legal/policy/manual/independent gates. Not owner-approved, not deployed, not the completed commercial student product.

Source ZIP: `IDIGITALROOT_PHASE1_CONNECTED_SOURCE_2026-10-14_rc9.zip`

SHA-256: `6e409c00e4e4122343276b44dae9b838967cf1050a054b74caccf5f3960b3811`

866,985 bytes; 302 input files; CRC and checksums verified before fresh extraction. Component versions: {"website": "1.2.0-rc.7", "cms": "1.5.5-rc.4", "backend": "1.1.4-rc.1", "analytics": "1.0.1-rc.1"}. Original approvals and frozen Core16/Analytics2 lineages are preserved.

| Gate | Evidence/result |
|---|---|
| Clean source/install/build | Fresh ZIP extraction; npm10.9.2 CI for exact locks; frontend Node22.19.0/server22.16.0; Astro7.3.5 check (0 errors/0 warnings; informational hints recorded); official Cloudflare adapter14.3.3 server build |
| Contract/security suites | Backend53/53; Analytics47/47; CMS22 Node cases/files (including inherited custom assertion suites and17 Access JWT cases); frontend8 contract cases;5 HMAC/scanner cases |
| Native smoke | 6/6 |
| Native publication/media/API workflows | 11/11 including independent AR, exact preview/revoke, publication race, replay target conflict, unpublish/republish, article, actual R2 quarantine/reference gating and cron claim/cancellation |
| End-to-end UI | 13/13 including CMS draft/private preview/review/publish/site update/rollback, live inquiry storage/outbox, opt-in analytics and authorized CMS retrieval |
| Native negative gates | 12/12 including origin/CSRF/method/body bounds, protected writers/properties, reserved routes, runtime flag/version conflicts, legal gate and inquiry wording versions/stale submission/idempotent retry |
| Dedicated settings UI | 6/6 including selected saved publication target, ordinary review/publish controls, EN/AR brand separation/restore, published appearance and saved-target selection |
| Critical responsive/keyboard/console | 46/46 across EN/AR,360/1440px, menu/Escape/focus/search/language/theme/reduced motion; no console errors, runtime exceptions, CMS traffic or raw provider-storage traffic in these critical views |
| Backend outage | Own local Worker group paused: public controlled503/noindex/no internal detail, then200 after recovery |
| Broad route inventory |134 localized requests:116 published200 and18 intentional404 (unpublished prototype Knowledge and unapproved legal pages); no browser exceptions |
| Automated accessibility |0 reported WCAG-tagged axe violations on116 published route views,54 CMS workspace/language views and26 mobile light/dark views. Test-only CSP bypass is used solely for axe injection; functional tests use normal CSP. Incomplete rules, gradient contrast and assistive technology still require manual acceptance |
| Control inventory |90 public control/parameter probes (0 click errors,0 clicked/no observed change),36 CMS dialog/action probes (0 errors). Observed clicks/UI changes and gated/no-change outcomes are recorded, not silently equated with complete semantic acceptance |
| Internal destinations |77 observed internal destinations;71 returned200. The six unapproved EN/AR legal destinations intentionally return404 and block production release |
| Supply chain/bundle boundaries | Exact lock, SBOM and dated npm advisory result; only intended local/storage boundaries; strict production-entry dry-run bundles exclude local acceptance hooks/test-context credentials. No zero-vulnerability claim |
| Owner launcher | See OWNER_OPERATOR_VERIFICATION.json. Linux launcher/start/stop/persistence proof is distinct from the new Windows owner-PC run, which remains unverified |

Runtime evidence uses actual local Cloudflare workerd, native local D1/R2 and Worker service bindings plus the built Astro app. Node SQLite is used to prepare/read the synthetic fixture and validate persistence, not as a substitute for the running backend. No remote resource was mutated. Known local secrets/fixture identity are restricted to the separate local entries and must never be deployed.

## What changed

- Preserved approved v4.3 artwork/layout and CMS professional direction; enhanced depth/cards/focus/reduced motion and repaired dark-surface/Arabic contrast and card accessible names.
- Connected published editorial fields, registered sections, navigation/footer, brand/product/service/Knowledge/appearance to the actual site; draft edits remain private. Global settings acquire missing AR state without a new migration.
- Finished protected review-ready/publish/rollback/schedule flow, current-version selection, CAS/idempotency and real referenced-media delivery. Saved settings select their correct publication target; publishers use human-named controls.
- Connected accepted eight-step inquiries, real receipts, stable retries/version changes and minimized opt-in analytics/outbox/report/export behavior. No public signup.
- Added strict Access verification and production entries, server-only provider/scanner interfaces, bounded requests/responses and signed abuse context. Missing real providers/approval fail closed.

## Remaining release gates

Real Access/MFA/recovery, exact account/hosts/bindings/keys/quotas/spend authority and real provider behavior; Drive authorization/PDF scan/inline-video privacy decision; legal entity/terms/privacy/age/retention and exact bilingual legal approval; deletion/anonymization/backup/restore/alerting/incident/load/performance/SEO checks; full applicable ASVS evidence and independent adversarial/manual accessibility/owner acceptance. Security matrices explicitly retain partial/external status. P1-SEC-01/P1-QA-01/P1-REL-01 are not represented as closed production gates.

All12 Toolbox tools and16 Workspace feature positions remain mandatory for the first commercial student release and are presentation demos in this Phase 1 candidate. Admin/Client Account and scoped future audience-edition operations are not operational. No managed-service-only commercial launch was substituted.

Read INSTALLATION_GUIDE.txt and docs/FEATURE_STATUS.md. Stop older previews, extract this package into a new folder and open OPEN_CONNECTED_PREVIEW.cmd. The website and CMS share local review data; same-candidate edits persist. No deployment or token sharing is needed for that review.
