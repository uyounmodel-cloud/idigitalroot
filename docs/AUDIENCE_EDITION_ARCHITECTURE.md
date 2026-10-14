# iDigitalRoot audience editions and customer experience

Status: owner requirements recorded; implementation design proposed. This is not a claim of multi-edition support in the current CMS.

The owner's latest instructions establish a student-first platform with later employee, entrepreneur and business experiences; one CMS entry point selects the desired public edition; the client account retains a common structure with audience-specific presentation and services; authorized central Admin manages every edition. The owner explicitly requires the complete 12-tool Toolbox and 16-feature Student Workspace for the first commercial student release.

## Terminology and boundaries

- **Product family:** Personal or Business. Business remains a distinct product domain even when central management uses the same CMS entry point.
- **Audience edition:** student, employee/professional, entrepreneur, business, or a later registered audience. An edition is not a content revision, locale, CMS release version, subscription plan or client website.
- **Locale:** EN/AR and later supported languages within an edition. Interface language, editing locale, preview locale and selected edition are distinct controls.
- **Account:** durable customer relationship. Changing audience after graduation must not require a new account, delete data or silently revoke purchased services.
- **Website/Digital Root:** one independent site owned by an account; an account can own several sites with different audiences and service entitlements.
- **Toolbox/Workspace:** customer product modules with their own public-profile/private-planning data domains. Normal website content stays in the individual website CMS.

## One CMS entry point, explicit edition scope

The intended experience is sign in -> select an authorized edition -> edit that edition's pages/media/translations/navigation/publishing/analytics/settings. Keep a persistent edition label visible, especially in preview, save, schedule, publish, rollback, export and user-access screens. Changing edition with unsaved edits prompts Save/Discard/Stay. Changing edition cancels outstanding reads and invalidates cached content, revision selection and preview capabilities. A late response for Edition A must never populate Edition B's screen.

Do not add a browser-only dropdown to the current single-site database and call it isolation. Every server request must resolve a code-owned edition registry entry and authorize the staff identity for that edition. Browser-supplied display names, edition IDs and query parameters are untrusted. Unknown/inactive editions and unavailable services fail closed. Never accept a browser-supplied API origin, database or bucket.

**Recommended implementation direction:** reuse one professional CMS shell and shared components; a protected server gateway selects configured edition services with separately scoped D1/R2/configuration. This can preserve the frozen 0001-0016 and 0001-0002 schemas per edition, rather than adding unsafe ad-hoc tenant columns. Final gateway/session/binding contracts require an explicit architecture and security task before implementation. No new databases, resources or migrations have been created by this review.

Scope and partition content, routes, media references, publication pointers, scheduling, preview tokens, audit records, analytics, backups, caches and exports. Verify object-, property- and function-level authorization inside each edition service, as well as gateway authorization. A central owner/root identity may have access to all editions; ordinary staff retain least-privilege edition/module scopes. Individual identities and immutable audits remain mandatory.

## Reuse across public frontends

Use a shared tested public shell, component registry and typed content contracts. Each edition supplies an approved profile: allowed modules, headings/content, section order, navigation, imagery, CTA wording, design tokens, locales and service visibility. Similar headings reuse schemas and templates; the published values remain edition-specific. Publish content changes without an unnecessary frontend rebuild where the accepted runtime contract supports it. New executable capabilities still require a reviewed code release.

Global brand/company information may be shared through explicit, versioned references. Copy or inheritance must be visible to editors; editing shared content must show affected editions before publication. A draft or missing translation in one edition must never fall back silently to another edition's content. Legal approval, media rights and service availability are scoped explicitly. Do not promise 99% reuse before real edition profiles prove compatibility.

Existing student URLs and the approved v4.3 design remain the current authority. Future hostname/path conventions are not silently chosen in this review. Register routes centrally; derive canonical URLs, language alternatives and caches from the resolved edition/environment. Visitors' audience choices must not become authorization decisions.

## Common client account, audience-specific presentation

Keep one account engine: website portfolio, projects, approvals, services, renewals, support, notifications, billing where approved, and account security. Add audience presentation profiles for labels, onboarding, recommended services, cards and visual treatment. Business account ownership/staff membership is a domain/permission decision, not just a theme.

Separate audience recommendations from purchased entitlements. Entitlements are checked server-side and tied to the account/site/subscription contract; changing a theme or audience cannot grant access. All student majors retain the same complete Toolbox; a major changes suggested presentation, not tool availability.

Provide explicit navigation to Toolbox and Student Workspace product modules. Their capability scope extends the earlier relationship-only blueprint, as authorized by the owner's full-tool launch decision. Preserve the relationship dashboard and website-CMS separation. Private semester plans, budgets, application records and reflections never become public website content by default. Exports or selected public outputs require explicit user action; any CMS handoff must use a narrow approved contract rather than general cross-database synchronization.

## Admin scope

Authorized Admin manages the edition catalogue, audience profiles, supported service definitions, plan versions, entitlement policies, onboarding templates, projects, support, campaigns and operational status. Public content is edited/published through the dedicated CMS contracts. Admin configures supported capabilities; it cannot create arbitrary code, expose production secrets, or bypass publication/security controls. Cross-edition bulk actions need explicit targets, preview of effects, authorization for every target and an immutable outcome record.

## Required acceptance before claiming multi-edition support

1. Same page titles/paths in different editions remain independent.
2. Edition A draft, preview, media, report and export cannot be read or used by Edition B.
3. Publish/unpublish/schedule/rollback changes only the selected edition.
4. Locale switching and interface-language switching preserve edition identity.
5. Late responses, multiple browser tabs, unsaved drafts and session expiry do not mix contexts.
6. Staff denied one edition cannot bypass restrictions with object IDs, URL parameters, headers, gateway routes or cached responses.
7. Shared content changes declare affected editions and preserve approval/version history.
8. Audience changes preserve account history and existing entitlements.
9. Analytics ingestion/reporting and backups/restores remain correctly partitioned.
10. Unsupported editions/components and dependency failures never fall back to another site's content.

## Delivery order and launch gate

Continue Phase 1 closure first. Phase 2 builds Admin authority, then Phase 3 implements the account and the newly mandatory student product modules in explicit domains. Phases 4-5 deliver reusable isolated site CMS/runtime capability and the factory. Do not use this plan to claim those later products are implemented or to deploy anything.

Technical closure of Phase 1 is not commercial launch of the full student offering. Commercial launch requires the promised Toolbox/Workspace, account/service workflows and every dependency actually needed to deliver the sold package, plus integrated security/QA, truthful service descriptions, approved legal/privacy/commercial terms and explicit release authority.
