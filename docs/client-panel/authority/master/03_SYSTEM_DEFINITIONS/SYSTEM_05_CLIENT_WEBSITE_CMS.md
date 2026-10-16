# System 05 — Reusable Client Website CMS

## Phase

Phase 4.

## Mission

Create a reusable professional CMS template for independent client websites by extracting/reusing the proven generic capabilities of the owner-approved Public Website CMS v1.5.3.

This is **not** a simple copy of the iDigitalRoot CMS and is **not** one unsafe multi-tenant CMS serving every customer from one shared authority boundary.

## Reusable generic core

Expected reusable engine capabilities:

- professional dashboard/shell;
- pages/page tree/sections;
- component registry and schema-driven safe fields;
- visual editor and responsive preview;
- WYSIWYG + sanitized source mode;
- media library/lifecycle;
- navigation/footer;
- localization/translation states;
- SEO and structured safe metadata;
- revisions/version history/rollback;
- draft/review/publish/schedule/archive;
- exact-version preview;
- users/roles/sessions;
- audit/activity history;
- safe embed/provider registry;
- analytics presentation adapters;
- site settings/branding/design tokens under bounded schemas;
- health/status surfaces appropriate to each client site.

## Per-client isolation

Each client website should have, unless a later explicit architecture proves a stronger equivalent:

- independent deployment/hostname;
- independent data boundary;
- independent media namespace/bucket/binding;
- independent secrets/config;
- independent auth/session scope;
- independent CSP/provider allowlists;
- independent backups/export/restore;
- independent audit trail;
- independent release/version record.

Cross-site ticket/audience confusion must be impossible by construction.

## Blueprint/profile model

The generic CMS is configured by a **site profile / blueprint** describing:

- page types;
- allowed components;
- content schemas;
- navigation model;
- branding/design tokens;
- allowed providers/embeds;
- enabled modules (news/blog/portfolio/services/products/etc.);
- localization set;
- SEO defaults;
- workflow policy;
- role defaults.

Capabilities are code-controlled. The site profile selects/configures supported capabilities; it does not inject arbitrary executable code.

## Relationship to Client Panel

The Client Panel may launch the CMS using bounded SSO and display high-level managed-service state, but does not synchronize or duplicate ordinary website content.
