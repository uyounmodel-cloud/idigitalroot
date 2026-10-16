# iDigitalRoot Full Solution Target Architecture v1.0

## Purpose

This is the consolidated target architecture for the six-system product family. It does not supersede accepted source contracts; it tells Codex how the complete solution must fit together as development proceeds.

## Application topology

```text
Public Internet
   |
   +--> Personal/Student Public Website (Astro/Workers)
   |        |
   |        +--> Published Content / Media / Inquiry / Analytics APIs
   |
   +--> Personal Client Panel (future)
   |        |
   |        +--> iDigitalRoot Platform APIs
   |        +--> one-time SSO ticket --> Client Website CMS A/B/C
   |
Staff / Protected Access
   |
   +--> Dedicated Public Website CMS
   |        +--> CMS service/data/analytics boundaries
   |
   +--> Admin & Operations Dashboard (future)
            +--> Platform operations APIs
            +--> orchestration metadata for clients/sites/projects/services
            +--> deployment/provider operations via privileged narrow contracts

Per Client Website
   |
   +--> Client Public Website runtime
   +--> Client Website CMS
   +--> isolated DB/media/secrets/config/auth/audit
```

## Cloudflare-first target

Unless a later explicit architecture decision changes it:

- public runtimes: Astro + TypeScript;
- server runtime: Cloudflare Workers;
- relational persistence: D1;
- media/object storage: R2;
- edge/CDN/WAF: Cloudflare;
- privileged access: Cloudflare Access/Zero Trust where accepted, plus application authz;
- environment secrets: provider secret bindings, never content DB fields;
- static/dynamic caching: explicit safe rules, not implicit broad caching.

## Shared code vs shared authority

Reusable code/packages are encouraged. Shared production authority is not.

Safe to share as code:

- UI primitives/design system;
- validation/sanitization libraries;
- auth helper code;
- permission policy engine abstractions;
- localization libraries;
- CMS generic component framework;
- audit/logging libraries;
- schemas/types;
- test/security harnesses.

Not safe to share as one uncontrolled authority:

- client data stores;
- client CMS auth/session namespace;
- client media stores/credentials;
- site-specific secrets;
- publish pointers across sites;
- client audit/history;
- provider credentials.

## Service contract principles

- versioned request/response schemas;
- explicit identity/audience/scope;
- server-side validation;
- idempotency/replay behavior defined for high-impact mutations;
- clear timeout/retry semantics;
- no hidden browser-to-database shortcuts;
- no client-controlled authority fields;
- observability without secret leakage.

## Environment model

At minimum:

- local developer fixture environment;
- bounded review/test environment;
- staging;
- production.

Staging and production use separate secrets, bindings and data. Preview URLs must be inventoried/protected/retired to prevent orphaned access.

## Release model

Every deployable system has a release unit containing exact source hash, dependency lock, migrations, environment contract, SBOM/provenance, tests, security evidence, rollback instructions and owner/release status.
