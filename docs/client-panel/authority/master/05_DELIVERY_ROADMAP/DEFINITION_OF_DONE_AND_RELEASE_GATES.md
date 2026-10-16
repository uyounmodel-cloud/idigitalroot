# Definition of Done and Release Gates

A feature is not done because the UI looks correct or because a unit test passes.

## Feature Done

- requirement traced;
- correct system/domain ownership;
- server-side authz where applicable;
- validation/error/failure path;
- EN/AR/localization behavior;
- accessibility;
- tests incl. negative/abuse path;
- no fake-success/dead controls;
- documentation updated.

## System Candidate

- clean install/build/type check;
- deterministic lock/toolchain;
- integration/E2E/browser tests;
- threat model/security matrix updated;
- dependency/secret scans;
- exact artifact + hashes;
- fresh-extraction reproduction.

## Owner Review Candidate

- professional user-facing UX;
- no debug/developer internals in normal workflows;
- review launcher or staging path proven;
- exact build marker/version;
- simple bounded review checklist.

## Release Ready

- owner-approved UX where required;
- independent technical acceptance;
- full security gate;
- full QA gate;
- SBOM/provenance;
- backup/rollback/monitoring;
- environment/binding/secret checklist;
- staging verification;
- no unresolved critical/high risks unless explicitly accepted by owner/security authority;
- explicit owner release authorization.

## Production Done

Only after actual deployment evidence + post-deploy smoke/security verification + monitoring/rollback readiness. Never claim production from a local build.
