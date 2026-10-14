# Exact-source local reproduction

Use a fresh extraction, Linux/Ubuntu/WSL native storage and the manifest-pinned Node 22.19.0 frontend runtime and Node 22.16.0 server/fixture runtime. npm 10.9.2 is the npm executable from Node 22.16.0, invoked with Node 22.19.0 first on PATH for frontend dependency installation. Do not regenerate the lockfile. Chromium and its actual version are recorded in the evidence; use IDR_CHROMIUM to select a compatible installed browser.

```bash
python3 scripts/run-native.py \
  --frontend-node /absolute/path/node-v22.19.0-linux-x64/bin/node \
  --backend-node /absolute/path/node-v22.16.0-linux-x64/bin/node \
  --data-dir /absolute/path/new-isolated-acceptance-data \
  --evidence-dir /absolute/path/new-acceptance-evidence \
  --install --verify --full-browser
```

This verifies source checksums and frozen lineages, installs the exact frontend lock with npm10.9.2 (and pinned audit tool lock), compiles backend/CMS/analytics, runs Astro check and the official Workers build, verifies frontend binding boundaries, prepares shared private-preview assets, runs inherited and dedicated security suites, bootstraps only fresh synthetic local data, starts actual local Workers/D1/R2 and built Astro, runs browser publishing/inquiry/analytics/media/negative workflows and the full route/workspace inventory. All wrangler D1 operations use --local. No remote provider mutation occurs.

Acceptance refuses to run against an existing BOOTSTRAP.json to protect review edits. Choose a fresh data folder for every acceptance run. Review mode without --verify retains data for the same sealed candidate. Source edits are never silently overwritten. A new source hash gets a separate owner-review workspace. The owner launcher stages execution into native WSL storage; downloaded ZIPs can remain in Windows Downloads.

Use root SHA256SUMS.txt and RELEASE_MANIFEST.json. Historical component reports are provenance, not current acceptance; the root native runner supersedes the old disconnected preview/source-gate procedures. Original authority ZIPs remain separate unchanged in the transfer package. The source ZIP excludes generated dist/node_modules/local databases/logs/secrets; builds generate them after source verification. Official reference snapshots and final evidence live in the outer release package, with their own hashes.

Review mode uses local test-only known secrets and fake Access identity in a separate cms-local.mjs entry, guarded by exact loopback origin and LOCAL_WORKER_TEST. Never deploy local configurations or synthetic bootstrap fixtures. Production entrypoints require real verified provider identity and managed secrets. Staging dry-run templates require explicit configuration/approval.
