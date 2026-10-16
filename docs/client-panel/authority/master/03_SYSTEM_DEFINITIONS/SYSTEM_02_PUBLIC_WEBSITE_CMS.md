# System 02 — iDigitalRoot Public Website CMS

## Status

The connected professional editor source v1.5.3 is **owner approved**. Preserve it as Phase 1 CMS authority.

## Purpose

A dedicated secured CMS for the public iDigitalRoot website. It is intentionally separate from the future Admin & Operations Dashboard.

## Professional editor rule

The ordinary editor sees a real product, not internal developer structures. The UI must use human-facing names, forms, WYSIWYG, media cards, ordering controls, translation workspaces, revision diffs, publishing controls, metrics/charts/tables and understandable status language.

Raw JSON, internal stable keys, row versions, correlation IDs and raw provider payloads are internal implementation details except in deliberately restricted diagnostics.

## Core capabilities

- pages/page tree/website map;
- sections/components driven by registered safe schemas;
- Visual Website Editor;
- navigation/footer management;
- EN/AR and extensible localization;
- media lifecycle and provider registry;
- Knowledge content;
- services/categories as approved;
- legal/SEO/public inquiry definition administration;
- draft/review/ready/publish/schedule/unpublish/archive as applicable;
- preview exact version;
- version history/rollback/audit;
- publishing concurrency and stale-version protection;
- analytics reporting UI;
- user/role/session administration within CMS authority;
- site health/settings bounded to CMS scope.

## Security boundaries

- protect CMS with strong identity/session controls and Cloudflare Access/Zero Trust where accepted;
- server-side authorization on every action;
- CSRF protection for browser mutations;
- no arbitrary executable JavaScript/CSS/SQL;
- rich HTML allowlist + server sanitization;
- embed provider allowlist + CSP alignment;
- file/media type/size/content validation and quarantine/finalization;
- audit material changes;
- no fake-success UI;
- failed/stale/unauthorized mutation never mutates data;
- production secrets not editable as normal CMS content.

## Reuse principle

The future Client Website CMS may reuse the generic CMS engine and UX patterns, but iDigitalRoot-specific site profile/business content must remain a profile/plugin-like configuration rather than contaminating the generic core.
