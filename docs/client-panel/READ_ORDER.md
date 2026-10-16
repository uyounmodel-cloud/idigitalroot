# Handoff reading order

This is a new Client Account planning handoff. Historical instructions and approvals have their original scope; do not let an old embedded prompt override the owner's current question-first request.

## A. Before asking discovery questions — read only

1. Verify this handoff's RELEASE_MANIFEST.json and SHA256SUMS.txt when using its ZIP. Use VERIFY_HANDOFF.py after reading it; it only reads/verifies files and does not install, extract or run project code.
2. Read README.md, SOURCES_AND_AUTHORITY.json and START_NEW_CONVERSATION_PROMPT.txt.
3. Read original `authority/master/00_START_HERE/LOCAL_DEVELOPMENT_AND_CLOUDFLARE_ENVIRONMENT.md`, current-state records and all system/data/identity boundaries under `authority/master/03_SYSTEM_DEFINITIONS/`.
4. Read the complete original Client Account DOCX (or its mechanical CLIENT_ACCOUNT_BLUEPRINT_ORIGINAL_TEXT.txt export) and the Admin blueprint under `authority/master/02_FOUNDATIONAL_BLUEPRINTS/`.
5. Read **every file** in `authority/master/04_SECURITY/`. These are verbatim originals, with hashes/provenance in SOURCES_AND_AUTHORITY.json.
6. Read current authority/context documents, especially STUDENT_LAUNCH_SCOPE, UNIVERSAL_ARCHITECTURE, MOTION_READING_CHECKPOINT, current verification and authority register. Historical approval/status boundaries matter.
7. Read CLIENT_PANEL_BLUEPRINT.md, FEATURE_INVENTORY.csv, DISCOVERY_QUESTIONS.csv, every new SECURITY/ file and QA_AND_RELEASE_GATES.md. New Client risk registers start NOT_ASSESSED; no public test PASS is inherited.
8. Return the verified checkpoint and ask the first 4–6 unresolved questions, prioritizing scope/sequence, first-release audience packs, account activation/identity and organizational roles. Do not create application code/screens/migrations or ask the owner to repeat fixed decisions.

If no file-reading tools exist, state what cannot be inspected and request the smallest missing access/text. Never claim a ZIP/DOCX/full file was read from its filename or summary.

## B. After discovery, before application creation

1. Retrieve the exact original master companion from the connected repository/download URL, verify SHA256 `f1ea6c341baf3c81afa5b797ed09beb9b1a400325338e8a42ed671c2a5f23b20`, ZIP CRC, RELEASE_MANIFEST.json and SHA256SUMS.txt. Inspect nested archives as applicable; never run historical launchers blindly. Keep the archive immutable.
2. Follow its `00_START_HERE/READ_ORDER.md` exactly. Latest explicit owner decisions in this handoff/conversation supersede older public structure or product-scope assumptions, without erasing historical authority. The master contains additional original source/UI/technical evidence not duplicated in the small handoff.
3. Verify/inspect the exact included MOTION01 source ZIP and all source/component manifests/checksums, not only release summaries. Inspect current shared backend, inquiry, CMS, published-content and migration boundaries before proposing integration.
4. Record whether the full master authority was actually available/read. If unavailable, continue useful discovery, but do not start application creation that requires that authority. Do not pretend the small handoff is the entire original master.
5. Resolve every implementation-blocking discovery item, mark later-gate items explicitly and present one coherent final scope/architecture/security/acceptance plan for owner approval. No silent decisions about commercial/legal rules, team seats, paid providers or phase reordering.
6. Only explicit scope approval opens local implementation. Exact public Core0001–0016 and Analytics0001–0002 remain frozen. New Client/Admin schema work requires an approved isolated migration task; never append0017 to a public lineage by accident.

## C. During implementation and delivery

Follow the approved blueprint, per-feature threat model, security registers and QA gates. Use isolated synthetic data, real local Workers/D1/R2 and browser evidence. Preserve existing review data and immutable archives. Report PASS/FAIL/BLOCKED honestly. No provider mutation/spend/deployment without exact separate authority. Finish a concrete, reviewable release candidate before asking for a release decision.
