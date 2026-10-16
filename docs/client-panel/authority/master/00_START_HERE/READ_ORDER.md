# Mandatory Codex Read Order

Do not modify source until this reading checkpoint is complete.

## Stage A — Transfer authority

1. `00_START_HERE/START_HERE.md`
2. `00_START_HERE/LOCAL_DEVELOPMENT_AND_CLOUDFLARE_ENVIRONMENT.md`
3. `00_START_HERE/CURRENT_STATUS_LEDGER.md`
4. `00_START_HERE/OWNER_DECISIONS_2026-10-14.md`
5. `00_START_HERE/CODEX_MASTER_START_PROMPT.txt`

## Stage B — Product/system model

6. `03_SYSTEM_DEFINITIONS/SYSTEM_BOUNDARIES_AND_DATA_OWNERSHIP.md`
7. `03_SYSTEM_DEFINITIONS/SYSTEM_01_PUBLIC_WEBSITE_STUDENT.md`
8. `03_SYSTEM_DEFINITIONS/SYSTEM_02_PUBLIC_WEBSITE_CMS.md`
9. `03_SYSTEM_DEFINITIONS/SYSTEM_04_ADMIN_OPERATIONS_PANEL.md`
10. `03_SYSTEM_DEFINITIONS/SYSTEM_03_CLIENT_PANEL.md`
11. `03_SYSTEM_DEFINITIONS/SYSTEM_05_CLIENT_WEBSITE_CMS.md`
12. `03_SYSTEM_DEFINITIONS/SYSTEM_06_CLIENT_PUBLIC_WEBSITE_FACTORY.md`
13. `03_SYSTEM_DEFINITIONS/CROSS_SYSTEM_IDENTITY_SSO_AND_AUTHORIZATION.md`
14. `03_SYSTEM_DEFINITIONS/LOCALIZATION_CONTENT_MEDIA_AND_DESIGN_SYSTEM.md`

## Stage C — Security authority

15. `04_SECURITY/SECURITY_MASTER_BASELINE.md`
16. `04_SECURITY/SECURITY_ARCHITECTURE_AND_THREAT_MODEL.md`
17. `04_SECURITY/SECURE_SDLC_SUPPLY_CHAIN.md`
18. `04_SECURITY/SECURITY_ACCEPTANCE_GATES.md`
19. `04_SECURITY/INCIDENT_LOGGING_MONITORING_BACKUP_DR.md`
20. `04_SECURITY/SECURITY_TEST_MATRIX.csv`

## Stage D — Current implemented code and frozen UI

21. Verify and inspect the exact files in `01_CURRENT_IMPLEMENTATIONS/`.
22. Public Website approved UI: `01_CURRENT_IMPLEMENTATIONS/01_PUBLIC_WEBSITE/iDigitalRoot_Personal_Student_Public_Website_UI_v4.3_A11Y_Personal_Menu_Repair.html`
23. Public Website current FE candidate: `IDIGITALROOT_P1-FE-02_PUBLIC_FRONTEND_SOURCE_v1.1.1_CANDIDATE.zip`
24. Latest FE closure operator: `IDIGITALROOT_P1-FE-02R1_LOCAL_CLOSURE_v1.7.zip`
25. CMS owner-approved UI authority: `IDIGITALROOT_PUBLIC_WEBSITE_CMS_FINAL_OWNER_REVIEW_v4.1_OWNER_APPROVED.html`
26. CMS owner-approved connected source: `IDIGITALROOT_P1-CMS_FINAL_CONNECTED_SOURCE_v1.5.3.zip`
27. Shared Public Backend: `IDIGITALROOT_P1-BE-01_PUBLIC_BACKEND_SOURCE_v1.1.2.zip`
28. Accepted technical authorities under `01_CURRENT_IMPLEMENTATIONS/04_TECHNICAL_AUTHORITIES/`.

## Stage E — Foundational approved blueprints

29. `02_FOUNDATIONAL_BLUEPRINTS/iDigitalRoot_Full_Solution_Developer_Blueprint_Requirements_v0.1.md`
30. `02_FOUNDATIONAL_BLUEPRINTS/iDigitalRoot_Admin_Operations_Dashboard_Final_Technical_Blueprint_v1.0.md`
31. `02_FOUNDATIONAL_BLUEPRINTS/iDigitalRoot_Client_Account_Dashboard_Final_Technical_Blueprint_v1.0.docx`
32. `02_FOUNDATIONAL_BLUEPRINTS/iDigitalRoot_Cross_Platform_Admin_Control_Localization_and_Rich_Media_Extension_v1.0.md`
33. `02_FOUNDATIONAL_BLUEPRINTS/iDigitalRoot_Public_Website_Product_Technical_Blueprint_v1.0_Candidate.docx`
34. `02_FOUNDATIONAL_BLUEPRINTS/iDigitalRoot_Public_Website_Lead_Inquiry_Extension_v1.1.md`

## Stage F — Delivery roadmap and task prompts

35. `05_DELIVERY_ROADMAP/MASTER_EXECUTION_ROADMAP.md`
36. `05_DELIVERY_ROADMAP/PHASE_1_COMPLETION_PLAN.md`
37. remaining phase plans
38. `05_DELIVERY_ROADMAP/DEFINITION_OF_DONE_AND_RELEASE_GATES.md`
39. `06_CODEX_TASK_PROMPTS/` only after all authorities above are understood.

## Stage G — Historical evidence

40. Use `90_PRIOR_HANDOFF_V4_EXTRACTED/` and `91_ORIGINAL_HANDOFF_ARCHIVE/` whenever chronology, previous test evidence, hashes or a disputed requirement needs confirmation.

### Required checkpoint before code changes

Codex must produce a short internal checkpoint containing:

- exact current phase;
- exact owner-approved UI authorities and hashes;
- exact current CMS source/hash and status;
- exact current FE source/hash and status;
- exact backend source/hash and status;
- migrations frozen lineages;
- hosting target (Cloudflare Workers), D1/R2 target, local WSL test environment and Cloudflare-account connection status;
- deployment/prod restrictions;
- next authorized task;
- any genuine ambiguity still unresolved after reading.

Only then may source changes begin.
