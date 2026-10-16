# Localization, Content, Media and Design-System Rules

## Localization

- English first-class LTR.
- Arabic first-class native RTL.
- architecture supports additional Admin-managed locales.
- locale record: code, names, direction, fallback, enabled surfaces, formatting policy, status.
- localized publishing may differ per locale; translation completeness/status must be visible.
- states may include MISSING, DRAFT, NEEDS_REVIEW, READY, PUBLISHED, OUTDATED, ARCHIVED.
- source change can mark dependent translations OUTDATED.

## Content model

- stable internal IDs distinct from labels/slugs;
- code-owned component capability registry;
- schema-validated fields;
- content workflows/versioning/concurrency;
- previews tied to exact version/revision;
- no arbitrary executable application code in content.

## Rich text

- WYSIWYG for ordinary editors;
- safe-source mode where approved;
- server-side sanitization is authoritative;
- block script/event-handler/javascript: URLs and unsafe elements/attributes/styles;
- sanitize on ingress and render defensively on egress.

## Media

- validate file type using content/signature, not only extension;
- size/dimension/decompression limits;
- quarantine before approval/finalization when needed;
- generated derivatives controlled by server pipeline;
- public delivery through safe application/CDN URLs;
- private/internal object identifiers are not browser authorization tokens;
- alt text/caption/localization support;
- external media only through registered allowlisted providers.

## Design system

- safe tokens for typography, spacing, radius, colors and approved component variants;
- public/client site profiles may choose supported tokens/variants;
- do not allow arbitrary CSS/JS injection to simulate flexibility;
- preview renderer and production renderer must share the same token semantics;
- responsive and RTL behavior is part of every component's acceptance contract.
