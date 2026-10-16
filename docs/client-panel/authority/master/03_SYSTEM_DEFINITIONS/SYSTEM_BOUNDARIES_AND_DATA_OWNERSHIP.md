# System Boundaries and Data Ownership

## Permanent separation

The platform is a family of applications connected by explicit contracts. Do not collapse everything into one giant application/database.

| Domain | Authoritative system |
|---|---|
| Public iDigitalRoot page content | Public Website CMS |
| Public iDigitalRoot rendering | Public Website frontend |
| Public lead/inquiry intake | Public Backend / Lead service |
| Public website analytics collection/reporting | Analytics boundary approved for Phase 1 |
| Staff identities/roles/operations | Admin & Operations |
| Client relationship/profile/services/billing/projects | Client Panel + Admin authoritative backend contracts |
| Client website content | that client website's own CMS |
| Client CMS users/roles | that client CMS, optionally federated by controlled SSO |
| Client website media | that client deployment/storage boundary |
| Client website runtime | that client website deployment |
| Deployment/provider secrets | secure operations/provider secret stores, never ordinary CMS content |
| Audit/security evidence | authoritative audit/logging domain defined per system; immutable/append-only where required |

## Cross-system rules

- No browser gets direct D1 or R2 credentials.
- No UI label/slug/domain is an authorization primitive; use stable IDs + server-side scope checks.
- No reusable password is shared between Client Panel and client CMS.
- SSO tickets are short-lived, single-use, audience-restricted and replay-protected.
- Client sites do not share one uncontrolled tenant DB/media bucket by default.
- Admin may orchestrate metadata/operations but does not silently own client-site content databases.
- Public Website CMS remains a dedicated product even after Admin exists.
- Provider integrations are explicit versioned contracts and may be disabled without breaking core product operation.

## Trust boundaries

At minimum model separately:

1. anonymous public Internet;
2. authenticated customer/session boundary;
3. privileged Public CMS staff boundary;
4. internal Admin staff boundary;
5. each client CMS boundary;
6. Workers/service-to-service boundary;
7. D1 databases;
8. R2/object storage;
9. external providers/email/analytics/embed providers;
10. deployment/CI/release authority;
11. audit/logging/monitoring plane.
