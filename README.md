# iDigitalRoot local website and CMS previews

This repository download contains a local review candidate. Phase 1 remains open. No Cloudflare deployment or provider-resource change is included.

Download `downloads/IDIGITALROOT_PUBLIC_WEBSITE_LOCAL_PREVIEW_v1.1.zip`, extract it into a new folder on the existing Windows + Ubuntu/WSL PC, and double-click `OPEN_WEBSITE_PREVIEW.cmd`. Keep its command window open while inspecting the website. The launcher prepares the build locally and should open the Windows browser automatically. Read `downloads/INSTALLATION_GUIDE.txt` for the complete steps and logs to return if startup fails.

The preview uses synthetic published content and code-owned presentation copy. Inquiry submission and browser analytics remain unfinished. The Public Website CMS is a separate application; Admin and the Client Panel are not launched here.

The sealed frontend source remains v1.1.2r6 CANDIDATE, SHA-256 `677ea259a49364c3f4e8db976c7fa4ac60b8f86c5ba48c7e825184f15e79facd`. Its preview Linux build/server and 31 real browser checks passed. The Windows launcher and owner-host browser forwarding remain unverified until run on that workstation. No owner/HQ approval, full Phase 1 closure or release readiness is implied.

The ZIP includes application source, a guide, manifests/checksums and local preview evidence. Complete integrated security/QA/release acceptance remains open. No GitHub Actions workflow, deployment script or production credential is added.

Preview launcher v1.1 displays live preparation progress and bounds slow setup steps. The original v1 ZIP is retained unchanged. The owner reported that the website opened after the initial dependency-install delay. This confirms startup on that workstation; it does not establish full browser acceptance or Phase 1 closure.

## Public Website CMS

[Download the CMS preview ZIP](https://github.com/uyounmodel-cloud/idigitalroot/raw/refs/heads/main/downloads/IDIGITALROOT_PUBLIC_WEBSITE_CMS_LOCAL_PREVIEW_v1.zip) and read the [CMS installation guide](downloads/CMS_INSTALLATION_GUIDE.txt).

Extract the ZIP into a new folder, double-click `OPEN_CMS_PREVIEW.cmd`, and click **Sign in for local owner review** when the browser opens. Keep that command window open. You can leave the public website preview running; the CMS uses its own local port (4197).

This launches the exact owner-approved connected CMS v1.5.3, SHA-256 `62f9e7441372b825d4e8535febdf7679d09d9a39464a8f63843f1eadd5c6d257`, without changing its source or UX. It uses temporary local sample data, local review authentication, and simulated provider/media services. CMS changes do **not** update the separate public website preview. Shared publishing integration remains open. Press Enter in the CMS command window to stop it; its sample data resets on restart.

The Linux launcher passed source integrity and module checks, 37 actual Chromium checks (including login, all 27 workspaces and EN/AR editor geometry), and fresh ZIP extraction/startup with a verified runtime download. The approved local server returns a known favicon 404, recorded in the verification evidence. Windows CMS launcher verification and integrated security/QA/release gates remain open. No Cloudflare/provider deployment, production credentials, or paid resources are involved.
