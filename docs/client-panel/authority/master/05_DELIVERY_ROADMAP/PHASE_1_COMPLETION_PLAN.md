# Phase 1 Completion Plan

## P1-FE-02 — first

- verify exact v1.1.1 candidate;
- repair closure/operator only where possible, source only when a real source defect exists;
- deterministic clean install;
- `astro check` 0 errors;
- official Cloudflare adapter server build;
- built app under workerd;
- real Chromium/Puppeteer regression;
- content publish/update without inappropriate rebuild where designed;
- draft invisibility;
- EN/AR/RTL/LTR;
- media delivery seam;
- failure modes;
- responsive/a11y/menu/reduced-motion;
- no CMS API path/direct D1/R2/browser secrets;
- seal and rerun from fresh extraction.

## P1-FE-03

- implement/verify real lead inquiry POST flow;
- server validation, schema version, locale capture, consent, anti-spam/rate limits;
- no public account creation;
- safe confirmation/error states;
- browser analytics endpoint only under accepted privacy/config policy;
- no sensitive form values in analytics;
- CSP/CORS/CSRF/cache behavior verified.

## P1-SEC-01

Run full integrated security gates in `04_SECURITY/`. Include manual/automated negative testing and threat-model update. Produce explicit residual risk list.

## P1-QA-01

- visual regression to approved UI;
- browser/device/responsive;
- EN/AR and locale fallback;
- accessibility;
- forms/errors/offline/dependency failure;
- performance/SEO/caching;
- CMS↔public publication paths;
- content/media edge cases.

## P1-REL-01

- immutable release set;
- SBOM/provenance;
- environment config matrix;
- secrets/bindings checklist;
- D1/R2/migration plan;
- backup/rollback;
- staging smoke/security verification plan;
- explicit owner release decision.

No production mutation is authorized by completing this plan alone.
