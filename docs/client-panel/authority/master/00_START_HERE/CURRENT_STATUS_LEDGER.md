# Current Status Ledger — 2026-10-14

## Status vocabulary

- **OWNER-APPROVED** — owner explicitly reviewed/approved the user-facing result.
- **ACCEPTED TECHNICAL AUTHORITY** — accepted architecture/data/service contract/foundation that must not be silently redesigned.
- **CURRENT CANDIDATE** — newest implementation under closure; not accepted until its gates pass.
- **PLANNED / FUTURE** — product scope defined but implementation has not been accepted.
- **HISTORICAL** — evidence/reference only; never supersedes newer explicit authority.

## Public Website — Personal / Student

**Owner-approved UI/content authority**  
`iDigitalRoot_Personal_Student_Public_Website_UI_v4.3_A11Y_Personal_Menu_Repair.html`  
SHA-256: `d10b1cff47d5912fecb49d88579971f3e21bb19a33b179e29356ea0eac5646fd`  
Status: **OWNER-APPROVED**

**Current frontend candidate**  
`IDIGITALROOT_P1-FE-02_PUBLIC_FRONTEND_SOURCE_v1.1.1_CANDIDATE.zip`  
SHA-256: `3709a3aa234e7f1a5dbb840037b9a9c04e53ac49172b8b216bb309697f24ef95`  
Status: **CURRENT CANDIDATE — P1-FE-02 not yet accepted**

**Latest local closure operator**  
`IDIGITALROOT_P1-FE-02R1_LOCAL_CLOSURE_v1.7.zip`  
SHA-256: `82a5019841d86deb1c566d590e7e1e394d137ec6676068d5f9ac61e6b38d33b9`  
Status: **CURRENT TEST OPERATOR, not evidence of PASS by itself**

### Last known FE-02 evidence before transfer

Owner WSL runs progressively proved:

- ZIP and source integrity gates passed;
- deterministic npm install succeeded;
- a compatible Chrome for Testing was obtained;
- browser launch issues were traced to cache extraction/executable permissions;
- Astro exact pins were verified;
- `astro check` passed with 0 errors;
- official Cloudflare adapter build passed;
- an earlier closure defect that ran BE tests before BE build was repaired;
- latest v1.7 repairs cached Chrome helper executable permissions before Puppeteer launch.

**Important:** v1.7 was prepared after the latest failure, but no owner-run PASS for v1.7 is recorded here. Codex must run/repair/close P1-FE-02 independently.

## Public Website CMS

**Owner-approved CMS UX authority**  
`IDIGITALROOT_PUBLIC_WEBSITE_CMS_FINAL_OWNER_REVIEW_v4.1_OWNER_APPROVED.html`  
SHA-256: `7f7e099e3c525b27dd8ee285410ad0a9ce71c5055d845219c40a8501f8ee60cf`  
Status: **OWNER-APPROVED**

**Connected professional CMS source**  
`IDIGITALROOT_P1-CMS_FINAL_CONNECTED_SOURCE_v1.5.3.zip`  
SHA-256: `62f9e7441372b825d4e8535febdf7679d09d9a39464a8f63843f1eadd5c6d257`  
Status: **OWNER-APPROVED CONNECTED CMS**

**Owner review package used for the approved build**  
`IDIGITALROOT_P1-CMS_OWNER_REVIEW_CONNECTED_v1.8.zip`  
SHA-256: `4dd32c93b90ede8634e7bbc0e54d7bcfb9c56e1d069b08a2340847c21ef459cd`

Owner approval in this conversation after v1.8: **“this is great and approved lets continue”**.

### CMS UX rule now frozen

Ordinary editors must see a professional CMS, not developer internals:

- human page/section/service names, not stable keys;
- forms/buttons/selectors/media controls, not raw JSON;
- WYSIWYG with sanitized safe-source mode where needed;
- charts/metrics/tables, not raw analytics payloads;
- readable revision diffs and activity history;
- EN LTR / AR full RTL mirror;
- Arabic sidebar right; Visual Editor page tree right / canvas center / inspector left;
- internal IDs, row versions, structured payloads and technical diagnostics hidden from normal workflows.

Do not redesign this approved experience unless the owner asks.

## Shared Public Backend

`IDIGITALROOT_P1-BE-01_PUBLIC_BACKEND_SOURCE_v1.1.2.zip`  
SHA-256: `c32aefa179bca74cd6d4f11c42fe02cb5421db6117a9f5f4d711ef674829d1a0`  
Status: **CURRENT bounded backend authority used by FE-02 work**

v1.1.2 added the safe public media-byte delivery seam required by the frontend. No new core migration was introduced.

## Accepted/frozen service/data lineages carried from prior handoff

- Public CMS backend foundation v1.4.1: `9da0b0174c6c5ce57b1ec8705ed0ca8119f57e7b269b145efffc242b03922239`
- Prior accepted Public BE v1.1.1: `781aa26489e39c2ce32096da18268bcdc5a763a601724ca7bb15e1d4f8f35ee9`
- DATA-03 v1.1: `bc0e19b9a9240741b04e1085819164e3a6b6e75f91c059a77070c5c3be9068b6`
- Analytics Core v1.0: `22d144914828c9e6503b03d0bac63c3b13aadd970ffe5dde4727943787cea86a`
- Core migrations: exactly `0001`–`0016`
- Analytics migrations: exactly `0001`–`0002`
- No `0017+` migration may appear unless a new explicit schema task authorizes it.

## Future systems

- Admin & Operations Dashboard: **PLANNED / blueprint exists, implementation not accepted**.
- Personal Client Panel / Client Account: **PLANNED / blueprint exists, implementation not accepted**.
- Reusable Client Website CMS: **PLANNED / derived from approved CMS core, not yet implemented**.
- Client Public Website Factory: **PLANNED / prompt/template architecture defined in this transfer package, not yet implemented**.

## Immediate next authorized work

1. Close P1-FE-02 on the exact current FE candidate or produce a bounded successor with full evidence.
2. Close FE-03 live inquiry submission and browser analytics under accepted contracts.
3. Run P1-SEC-01 integrated security closure.
4. Run P1-QA-01 integrated product/visual/accessibility/localization/runtime QA.
5. Run P1-REL-01 staging/release preparation.
6. Do not deploy until explicit owner/provider/credential/spend/release authority is granted.
7. Only after Phase 1 is closed: start Phase 2 Admin & Operations.
