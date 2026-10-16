# Secure SDLC and Software Supply Chain

## Development lifecycle

1. Requirements include security acceptance criteria.
2. Threat model before implementation of material features.
3. Code review includes authorization/data exposure/error paths.
4. Tests include positive + negative + abuse + concurrency paths.
5. Static checks/lint/type/build.
6. Dependency/SCA/license/provenance review.
7. Secret scanning.
8. Artifact integrity/manifest/checksums.
9. Fresh-extraction reproducibility.
10. Staging security/QA.
11. Explicit release approval.
12. Post-deploy verification/monitoring/rollback readiness.

## Dependency policy

- exact/pinned direct critical toolchain versions where practical;
- committed deterministic lockfiles;
- review package-manager install scripts;
- no automatic dependency upgrades in release artifacts without review;
- transitive vulnerability review;
- avoid unmaintained packages in security-critical paths;
- record exceptions.

## Artifact policy

Every candidate/release must have:

- source archive;
- SHA-256;
- file manifest and checksums;
- toolchain versions;
- dependency lock;
- changelog;
- test/security evidence;
- build/reproduction instructions;
- release status.

## SBOM/provenance

Before production release, generate and archive a machine-readable SBOM for each deployable application/service. Preserve build provenance sufficient to answer which exact source/dependency/toolchain produced the deployed bytes.

## Secrets

- never commit production secrets;
- never put secrets in prompts, screenshots, logs or ZIP manifests;
- use environment/provider secret bindings;
- rotate compromised/exposed credentials;
- use separate credentials per environment and least privilege.

## CI/CD / release

The owner's review workflow does not require Git. Engineering may use internal source-control/automation where available, but the owner-facing release authority remains immutable artifacts + hashes + evidence. Production deployment still requires explicit owner authority.
