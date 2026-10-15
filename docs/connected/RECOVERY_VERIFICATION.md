# Installer recovery — 15 October 2026 R1

**Local recovery verification: PASS. Owner Windows run: UNVERIFIED. Production/Phase1 release remains BLOCKED.**

The supplied diagnostic recorded EIDLETIMEOUT connecting to registry.npmjs.org:443 during npm ci. All sealed-source checks passed. The failure preceded application build and Cloudflare identity verification. The npm upgrade notice was not a remedy; npm10.9.2 stays pinned. No personal paths or uploaded owner logs are published here.

The application source ZIP is unchanged, SHA256 `6e409c00e4e4122343276b44dae9b838967cf1050a054b74caccf5f3960b3811`. Core16/Analytics2 lineages and original owner authorities are preserved. The registry outage is not evidence of a broken application or invalid Cloudflare login.

## Repair

The recovery ZIP includes a sealed Linux x64 dependency tree from clean npm10.9.2 CI using the exact source lock. All16,641 files/links match the prior rc9 dependency install byte for byte. Original npm integrity verification, per-file SHA256, archive/manifest SHA256, safe path/link extraction and executable permissions stay enforced. No TLS verification, dependency version or lock was changed. All package licenses remain in the dependency archive. The archive/manifest are bound to the exact frontend package/lock hashes.

The launcher stages and verifies a complete replacement in native WSL storage before moving an incomplete dependency directory aside. Existing review data is untouched. A valid existing install is reused; other architectures retain pinned online npm with bounded retries, fewer simultaneous connections and cache reuse. The installer records strategy and file verification in diagnostics. Cloudflare identity stays read-only; no login, provider mutation or deployment is performed.

## Current verification

- 8 integrity/path/link/preservation rejection checks passed.
- A synthetic malformed stamp and incomplete installation were repaired with npm registry configured to an unreachable loopback endpoint. A test shim actively rejected any npm ci/install command and delegated real version/build/check commands to pinned npm; no download command was attempted.
- All16,641 dependency files/links were checked; the old partial directory and existing data marker were retained.
- Actual backend/CMS/analytics builds, Astro check and official Cloudflare server build, native workerd/D1/R2 and EN/AR readiness passed.
- 6 native smoke checks and13 integrated browser checks passed: actual CMS draft/private preview/review/publish/rollback, inquiry storage/outbox, opt-in analytics and authorized CMS retrieval; no browser exceptions.
- Normal stop, free ports, warm restart without re-extraction, and the authenticated private draft/history after reopening passed. Root source checksums passed after the run.

The initial internal restart check identified an incorrect Astro executable path in readiness detection; this was repaired before publication, and the complete cold/warm verification repeated. The final exact installer/helper hashes are in RECOVERY_VERIFICATION.json.

The previous application's broader134-route/54-CMS/36-dialog/90-control and security evidence remains in VERIFICATION_REPORT.md and evidence/. It is baseline evidence for the identical application source, not a claim those broader sweeps were repeated for this installer-only change. Real Windows/WSL browser forwarding, provider/legal/independent security/QA/release gates remain open. All Toolbox/Workspace capabilities remain mandatory commercial scope and presentation demos here; Admin/Client are not operational.

Read INSTALLATION_GUIDE.txt. Close the failed preview, download/extract the complete new ZIP into a new folder and run OPEN_CONNECTED_PREVIEW.cmd. Existing rc9 review data is selected by the same source hash. Node runtimes still require their official downloads if they are not already prepared. The included offline dependency path is Linux x64, matching the tested Ubuntu/WSL target.
