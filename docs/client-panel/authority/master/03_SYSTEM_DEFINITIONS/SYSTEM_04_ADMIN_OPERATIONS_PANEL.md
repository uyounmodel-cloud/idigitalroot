# System 04 — Admin & Operations Dashboard

## Phase

Phase 2, immediately after Phase 1 closure.

## Existing authority

`iDigitalRoot_Admin_Operations_Dashboard_Final_Technical_Blueprint_v1.0.md` is the foundational product/technical blueprint and is included in this package.

## Product definition

A secured internal staff operating system for running iDigitalRoot. It is not a public CMS replacement and it must not collapse all client website CMSs/databases/secrets into one domain.

## Major capability domains

- staff identities, roles, permissions, scopes, MFA and sessions;
- leads/inquiries and qualification lifecycle;
- clients and client accounts;
- websites/Digital Roots;
- project execution and client approvals;
- Website Blueprints and onboarding templates;
- services/plans/subscriptions/commercial classifications;
- domains/professional email operations;
- requests/support;
- quotes/invoices/payments/renewals as approved;
- targeted Client Panel Hero campaigns and notifications;
- Root Health managed service state;
- provider/API/dependency registry;
- localization registry and translation governance;
- public-content administration orchestration without replacing the dedicated CMS product;
- security events/audit/session controls;
- feature flags/global settings;
- deployments/environments/jobs/backups/monitoring controls through explicit privileged contracts.

## Core principle

> Admin manages configuration and operations. Code manages capabilities.

Routine business work must not require developers, but the Admin must never become a raw arbitrary-code console.

## Authorization model

Permission-first; roles are permission bundles. Scope every operation to business/domain ownership. Object/property/function authorization is server-side. Sensitive operations require re-authentication and/or stronger approval. Root Super Administrator is still auditable and cannot erase immutable security history.

## Security expectation

This is the highest-risk application in the platform. Apply the strictest identity, session, authorization, audit, network/access, secret-management and operational controls in the package. Treat privileged Admin flows as candidates for ASVS highest-assurance controls where applicable.
