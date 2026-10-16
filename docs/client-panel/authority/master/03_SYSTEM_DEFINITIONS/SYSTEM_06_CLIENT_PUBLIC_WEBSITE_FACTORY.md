# System 06 — Client Public Website Factory / Major Prompt System

## Phase

Phase 5, after the reusable Client Website CMS is stable.

## Goal

Provide Codex/engineering with a controlled, repeatable method to create a new client's public website and its CMS integration without repeating architecture discovery from zero each time.

The output is not an unconstrained AI-generated production codebase. It is a website assembled from a secure supported platform architecture, blueprint/site profile, approved design system primitives and explicit client requirements.

## Inputs for each new client website

- client/site identity;
- business type and Website Blueprint;
- goals/audience/conversion actions;
- required pages and information architecture;
- languages + direction;
- brand assets/colors/type style;
- content/material availability;
- allowed modules/functions;
- forms/inquiries/booking/ecommerce/etc. only if supported;
- required integrations/providers;
- legal/privacy/consent requirements;
- SEO targets/schema types;
- performance/accessibility targets;
- approved hosting/deployment/environment;
- CMS site profile and role model.

## Generation workflow

1. Read the generic CMS/runtime contracts.
2. Create a site-specific product brief.
3. Create IA/routes and content model.
4. Create threat model and data classification.
5. Choose only supported components/modules.
6. Create site profile/blueprint configuration.
7. Build public site shell and CMS profile integration.
8. Build localized content/data fixtures.
9. Run security, accessibility, RTL/LTR, responsive, SEO and performance gates.
10. Produce owner review build.
11. Apply bounded owner changes.
12. Seal source + manifest + checksums + deployment instructions.
13. Deploy only with explicit environment/provider authority.

## Required prompt set

`06_CODEX_TASK_PROMPTS/07_CLIENT_WEBSITE_FACTORY_PROMPT.md` contains the master new-client website prompt. It must be supplemented by the real client brief and the exact CMS/runtime capability catalog at execution time.

## Guardrails

- no unsupported components invented by prompts;
- no arbitrary scripts/embeds just because a client requests them;
- integrations require registered provider contracts;
- no credentials in prompt text/artifacts;
- no client data copied across sites;
- no generated code considered production-ready until all gates pass;
- preserve independent site/CMS deployment and auth boundaries.
