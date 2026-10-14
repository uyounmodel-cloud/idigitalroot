#!/usr/bin/env bash
set -euo pipefail
export ASTRO_TELEMETRY_DISABLED=1 WRANGLER_SEND_METRICS=false
python3 /workspace/idigitalroot/cloud-environment/install.py
