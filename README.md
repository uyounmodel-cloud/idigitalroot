# iDigitalRoot — connected website and CMS review

The current package connects the public website and its dedicated CMS through local Cloudflare Workers, D1 and R2. It includes the frontend refinements, published-content binding, inquiry submission and optional analytics. **This is a review candidate; Phase 1 release is still blocked by the gates below. No Cloudflare deployment has occurred.**

[Download the connected website + CMS ZIP](https://github.com/uyounmodel-cloud/idigitalroot/raw/refs/heads/main/downloads/IDIGITALROOT_CONNECTED_WEBSITE_CMS_REVIEW_2026-10-14_rc9.zip) · [Installation guide](downloads/CONNECTED_INSTALLATION_GUIDE.txt) · [Verification report](docs/connected/VERIFICATION_REPORT.md) · [Feature status](docs/connected/FEATURE_STATUS.md) · [Phase 1 closure register](docs/connected/PHASE1_CLOSURE_STATUS.md)

1. Stop your older preview command windows by pressing Enter in each.
2. Download and extract the whole new ZIP into a **new folder** on your existing Windows + Ubuntu/WSL PC.
3. Double-click **OPEN_CONNECTED_PREVIEW.cmd** and keep its window open. Named steps show progress during installation/build.
4. When READY appears, open the website at **http://127.0.0.1:4400** and the connected CMS at **http://127.0.0.1:4198**. Click **Sign in for local owner review** in CMS.
5. Save a small Home-page text draft. Confirm the website stays unchanged; inspect exact preview; choose **Review complete — ready to publish**, publish and refresh the website. Test Arabic separately with **Content language**.

The same candidate preserves local review edits after stopping/reopening. A different candidate uses isolated data. Use synthetic data for review. The launcher rechecks an existing Cloudflare connection read-only and continues locally; no login, token sharing, deployment or paid resource is needed. If startup fails, send `PREVIEW_LOGS.zip`; you do not need to debug it.

The ZIP includes immutable source, hashes, manifests, exact locks, change/feature reports, threat model, security matrices, reproduction instructions and local browser evidence. The original owner-approved public UI v4.3 and connected CMS v1.5.3 remain recorded authorities. This changed successor requires owner review.

## Release boundaries

Local technical results are documented against the exact sealed source in the verification report. They do not establish owner Windows acceptance, independent security/QA acceptance or production readiness. Actual Access/MFA/provider integration, legal/privacy/retention decisions, operational recovery/monitoring and integrated release gates remain open. Drive/PDF services fail closed until configured and verified; unapproved legal pages remain unpublished. No production credentials are in this package.

All **12 Toolbox tools and 16 Student Workspace feature positions remain required for the first commercial student release** and are presentation demos in this Phase 1 build. Admin and the Client Account are not operational here. Future employee/entrepreneur/business editions and scoped CMS administration are documented in [the edition architecture](docs/AUDIENCE_EDITION_ARCHITECTURE.md), not presented as a working edition chooser. Read [the student launch scope](docs/STUDENT_LAUNCH_SCOPE.md). The frozen Phase 1 → Admin → Client Account → reusable client CMS → website factory order remains in force.

## Earlier downloads

Earlier separate website/CMS previews and the detailed review are preserved unchanged in `downloads/`. Their launchers use separate temporary sample data and do not update this connected build. See the [historical preview notes](docs/HISTORICAL_PREVIEW_README.md). Use the new connected package for this review.

Cloud setup helpers are in `cloud-environment/`; they reproduce this same local package without imposing a Git workflow on the owner or changing provider resources.
