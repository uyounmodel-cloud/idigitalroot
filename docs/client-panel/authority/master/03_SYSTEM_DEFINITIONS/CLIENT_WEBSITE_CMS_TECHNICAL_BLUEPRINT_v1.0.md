# Reusable Client Website CMS — Technical Blueprint v1.0

**Status:** planned implementation authority for Phase 4; must be reconciled with the then-final Phase 1/2/3 contracts before coding.

## 1. Product objective

Build one reusable CMS product core capable of powering many independent client websites while preserving per-site deployment/data/media/security isolation. The owner-approved iDigitalRoot Public Website CMS v1.5.3 is the UX and capability reference, not a literal tenant database to reuse.

## 2. Logical architecture

```text
CMS Web UI
  -> CMS API/Worker
       -> Site Config/Profile
       -> Content/Workflow Service
       -> Localization Service
       -> Media Service
       -> Search/Index adapters (optional)
       -> Analytics adapter
       -> Auth/AuthZ/Session Service
       -> Audit Service
       -> Site D1
       -> Site R2

Client Public Website
  -> Published Read API / safe media URLs
```

A deployment may package services together initially, but boundaries must remain explicit in code/interfaces.

## 3. Site profile

Each site profile declares only supported capabilities:

- site ID and display identity;
- enabled locales and direction;
- page types;
- allowed components and schema versions;
- navigation/footer zones;
- enabled modules;
- media classes/limits;
- embed/provider allowlist;
- design tokens/variants;
- SEO defaults/schema capabilities;
- workflow policy;
- role defaults;
- public runtime contract version.

Site profile values are validated data, not executable code.

## 4. Generic content entities

Conceptual entities, subject to final schema task:

- `site`
- `locale`
- `page`
- `page_revision`
- `section_instance`
- `localized_content`
- `navigation_set` / `navigation_item`
- `footer_group` / `footer_item`
- `media_asset` / `media_variant`
- `provider` / `embed_reference`
- `seo_record`
- `publish_release` / `publish_pointer`
- `preview_token` or equivalent exact-version preview record
- `cms_user` / role / permission / scope
- `session`
- `audit_event`
- optional module entities (article, service, portfolio item, product etc.) registered by capability catalog.

Do not freeze physical tables until Phase 4 schema design reuses proven migrations/contracts safely.

## 5. Content workflow

Minimum states where applicable:

- DRAFT
- NEEDS_REVIEW
- READY
- SCHEDULED
- PUBLISHED
- UNPUBLISHED
- ARCHIVED

Publishing must use server authority, validate readiness, preserve concurrency/row-version rules and update only permitted publish pointers. Preview targets an exact revision, never “whatever is current.”

## 6. Roles

Suggested generic roles, configurable by site:

- Site Owner / Administrator
- Publisher
- Editor
- Translator
- Media Manager
- Analyst / Read-only

Roles are bundles; permissions are the primitive. High-impact actions may require re-authentication.

## 7. CMS UI requirements

- human names, not internal keys;
- visual page tree;
- visual section editor with schema fields;
- WYSIWYG + sanitized source;
- media chooser/previews/alt/caption;
- drag/reorder or accessible move controls;
- side-by-side translations;
- SEO forms;
- readable revisions;
- publishing/history;
- charts/tables for analytics;
- advanced diagnostics hidden/restricted.

## 8. Security requirements

- independent site auth/session scope;
- client Panel SSO ticket audience exactly one CMS/site;
- object/property/function/site-scope authorization;
- CSRF protection;
- server sanitization and safe URL policies;
- media file validation/quarantine/finalization;
- no arbitrary JS/CSS/SQL;
- provider/embed allowlist + CSP;
- audit material mutations;
- bounded exports and analytics;
- fail closed on unknown components/profile versions.

## 9. Public read contract

The public website receives only published, localized, public-safe models. Never expose drafts, internal IDs unnecessarily, role data, audit data, object-store credentials or private media keys.

## 10. Deployment template

For each site create a versioned deployment record including:

- Worker/app identifiers;
- custom domain/hostname;
- D1 binding;
- R2 binding;
- secret names (not secret values);
- Access/auth configuration;
- CSP/provider policy;
- backup/export configuration;
- current site profile version;
- current public runtime/CMS release versions.

## 11. Testing template

Every site profile must pass:

- schema/profile validation;
- public publish/draft isolation;
- role/authz matrix;
- SSO cross-site replay tests;
- rich content/media/embed adversarial tests;
- locale/RTL;
- responsive/browser/accessibility;
- backup/export/import safety;
- fresh-release reproduction.
