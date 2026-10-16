# System 01 — iDigitalRoot Public Website (Personal / Student)

## Purpose

The public commercial website for Personal iDigitalRoot, initially marketed primarily to university students while remaining extensible to future Personal audiences.

## Frozen product authority

- UI/content direction: v4.3 approved HTML, hash recorded in CURRENT_STATUS_LEDGER.
- Architecture: Astro + TypeScript, Cloudflare Workers server/on-demand rendering, published-content APIs, D1/R2 behind server boundaries.
- EN LTR and AR RTL.
- No redesign unless owner requests it.

## Core responsibilities

- public pages, services, categories/subcategories, Knowledge content and legal pages;
- published navigation/footer;
- localized published content;
- media rendering through safe public media delivery, never direct browser object-store authority;
- SEO and structured data controlled by code/CMS-safe schemas;
- lead/inquiry entry;
- public analytics only through approved minimal browser collection contract;
- graceful controlled failure when backend content is unavailable.

## Non-goals

- public self-signup;
- client portal functionality;
- Admin functionality;
- arbitrary CMS code execution;
- direct D1/R2 browser access;
- production secret exposure.

## Current work

P1-FE-02 must be closed on exact sealed bytes. Then FE-03 adds/finishes live inquiry submission and approved browser analytics. Then integrated security/QA/release gates.

## Acceptance essentials

- pixel/structural parity with approved v4.3 direction;
- correct published data without rebuild where contract requires runtime binding;
- drafts never leak publicly;
- locale and RTL behavior correct;
- no horizontal overflow at target widths;
- accessible keyboard/focus/menu behavior;
- safe cache semantics and no personalized/sensitive content cached publicly;
- CSP/security headers appropriate to final deployment;
- no runtime console/module failures;
- fail closed for malformed/unknown CMS components;
- media URLs do not expose internal object keys as authority;
- inquiry abuse/rate-limit/validation/consent controls in FE-03.
