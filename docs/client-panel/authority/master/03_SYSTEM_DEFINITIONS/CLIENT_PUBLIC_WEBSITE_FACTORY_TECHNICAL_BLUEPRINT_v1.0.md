# Client Public Website Factory — Technical Blueprint v1.0

**Status:** planned implementation authority for Phase 5.

## 1. Objective

Make future client websites fast to design and build without turning AI prompts into uncontrolled production authority. Each new website is produced from a supported public-runtime core, an approved client brief, a Website Blueprint and a validated site profile compatible with the reusable Client Website CMS.

## 2. Factory layers

1. **Generic Public Runtime Core** — routing, locale, renderer, SEO, media, forms, error handling, security headers.
2. **Component Capability Catalog** — approved hero, text, media, cards, lists, FAQ, service, article, portfolio, contact and other modules.
3. **Design Token System** — typography, colors, spacing, radii, motion, layout variants.
4. **Website Blueprint** — business-type default IA/modules/onboarding requirements.
5. **Client Site Profile** — concrete supported components/pages/locales/providers/design tokens for that client.
6. **CMS Content** — editor-managed content through the client CMS.
7. **Prompt Pipeline** — Codex instructions to produce briefs/design/implementation using only supported capabilities.

## 3. Prompt pipeline stages

### P0 Discovery

Ask only missing client-specific questions. Output: signed-off brief.

### P1 IA/content model

Routes, page goals, sections, conversion paths, locales, SEO schema, content/data requirements.

### P2 Visual system

Brand direction, type hierarchy, palette tokens, spacing/layout, imagery, motion rules. Output token/config proposal and representative screens.

### P3 Site profile

Machine-readable configuration mapping pages/components/modules/locales/providers. Validate against capability catalog.

### P4 Implementation

Build/compose public runtime and connect published CMS models. No direct DB/browser storage credentials.

### P5 Security/QA

Threat model, authorization/form/provider tests, accessibility, RTL, responsive, performance, SEO, error states, no console errors.

### P6 Owner review

Bounded review build with exact marker/version. Apply only approved changes.

### P7 Seal/release

Source ZIP, hashes, manifest, SBOM/provenance, deployment config, rollback, explicit release authority.

## 4. Controlled extensibility

If a client asks for a capability not in the catalog, do not silently generate it. Open an engineering capability-extension task: design, security review, implementation, tests, catalog/version update. Then use it in sites.

## 5. Forms/integrations

Forms, booking, ecommerce, maps, chat, newsletters, social feeds and other integrations are optional registered modules. Every module owns its schema, auth, rate limits, privacy, provider allowlist and failure behavior.

## 6. No cross-site coupling

A generated Website A must not be able to read Website B content/media/auth/config because of shared code or AI prompt context. Tests must deliberately attempt cross-site access.
