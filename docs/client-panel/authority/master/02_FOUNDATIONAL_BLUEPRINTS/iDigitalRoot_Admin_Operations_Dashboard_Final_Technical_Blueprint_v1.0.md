# iDigitalRoot Admin & Operations Dashboard — Final Product & Technical Blueprint v1.0

**Status:** FINAL CANDIDATE FOR IMPLEMENTATION  
**Date:** September 2026  
**Authoritative inputs:**

1. `iDigitalRoot_Public_Website_Product_Technical_Blueprint_v1.0_Candidate`
2. `iDigitalRoot_Client_Account_Dashboard_Final_Technical_Blueprint_v1.0`
3. `iDigitalRoot_Public_Website_Lead_Inquiry_Extension_v1.1`
4. Approved Admin-dashboard decisions from the product-design conversation through 22 September 2026.

---

# 0. Document Control

## 0.1 Product definition

The **iDigitalRoot Admin & Operations Dashboard** is the secured internal operating system of iDigitalRoot.

It is the staff-only platform through which authorized iDigitalRoot personnel manage:

- the public iDigitalRoot website;
- public pages, categories, subcategories, sections, navigation and media;
- all languages and translations used by the public website, public inquiry wizard and Client Account;
- visitor inquiries and the sales/qualification lifecycle;
- clients and Client Accounts;
- client websites / Digital Roots;
- website-development projects;
- Website Blueprints and their onboarding templates;
- client approvals, previews, versions and project communication;
- services, plans, subscriptions and commercial classifications;
- domains and professional-email services;
- client requests and support;
- quotes, invoices, payments and renewals;
- client-account Hero campaigns, notifications and service promotions;
- Root Health states and managed service status;
- provider / API / dependency registry;
- public Root Check configuration and operational data;
- iDigitalRoot public Knowledge Center content;
- internal staff users, roles, permissions and scope;
- security events, sessions, audit history and privileged actions;
- feature flags, global settings and localization;
- environments, deployments, monitoring, jobs, backups and infrastructure-facing operational controls.

The Admin Dashboard does **not** replace source control, infrastructure secrets storage, or each client website's independent CMS. It orchestrates and manages them through explicit secure contracts.

## 0.2 Core operating principle

> **Admin manages configuration and operations. Code manages capabilities.**

Routine business work must not require a developer.

Examples of routine Admin-managed operations:

- create a new public page;
- add a new website category or subcategory;
- edit content, HTML, images, media and embeds;
- create a new article;
- add a language;
- translate a page or Client Account label;
- create a new Website Blueprint using supported fields;
- edit an onboarding questionnaire;
- add/edit/retire a service;
- change plan pricing through versioned commercial records;
- create a client;
- manage a website project;
- reply to a lead or support request;
- create an invoice;
- publish a targeted Hero campaign.

Creating a genuinely new platform capability still requires engineering, testing and deployment.

## 0.3 Permanent separation rule

The following remain separate applications/data domains:

```text
PUBLIC iDIGITALROOT WEBSITE
          |
          v
PUBLIC INQUIRY / LEAD INTAKE
          |
          v
iDIGITALROOT CLIENT ACCOUNT
          |
          +----> Client Website A CMS
          +----> Client Website B CMS
          +----> Client Website C CMS

INTERNAL iDIGITALROOT ADMIN & OPERATIONS
          |
          +---- manages/configures all approved iDigitalRoot surfaces
          +---- controls internal operations and secure contracts
```

The Admin Dashboard may control configuration and metadata for these systems, but it must not collapse all databases, credentials or content domains into one uncontrolled data store.

---

# 1. Non-Negotiable Product Rules

1. **No shared Admin accounts.** Every staff user has an individual identity.
2. **Every Admin user has role(s), permissions and scope.**
3. **The interface itself is permission-aware.** Users see only modules/actions relevant to them.
4. **Backend authorization is mandatory.** Hidden buttons are not security.
5. **One Root Super Administrator authority exists**, with platform-wide control, but even Super Admin activity is audited.
6. **MFA is required for privileged Admin access.**
7. **Sensitive actions require re-authentication and may require stronger approval.**
8. **Significant changes are auditable.**
9. **Deletion is conservative.** Archive/retire/soft-delete is preferred; financial/security/audit history is never casually deleted.
10. **Public website content is database/CMS driven.** Routine edits do not require code deployments.
11. **Client website content remains in each client website CMS.**
12. **The Admin Dashboard does not expose raw production secrets to ordinary staff.**
13. **Public website HTML editing is supported, but script execution is controlled.**
14. **Unlimited locales are architecturally supported.** Arabic, English, French or any later language can be administered without duplicating application code.
15. **LTR/RTL behavior is locale-controlled.**
16. **No AI chatbot is required in the Admin, Client or Inquiry v1 products.**
17. **External APIs/providers are optional integrations, not core assumptions.**
18. **Free-first and cost-awareness policies remain in force.**
19. **Internal notes and client-visible messages are separate data classes.**
20. **Every significant record has stable internal identity and history.**

---

# 2. Staff Identity, Authentication & Authority

## 2.1 Staff user record

Every internal user must have at least:

- immutable internal StaffUser ID;
- full name;
- work email;
- optional work phone;
- status: invited / active / suspended / disabled / archived;
- role assignments;
- direct permission exceptions only where policy allows;
- scope assignments;
- preferred Admin language;
- timezone;
- MFA state;
- last login;
- active sessions;
- security history;
- creation date;
- creator;
- last permission change;
- staff notes visible only to authorized managers/security.

## 2.2 Authentication

Required capabilities:

- secure password authentication if passwords are used;
- strong password hashing using a current memory-hard or equivalent secure scheme;
- MFA support, with MFA mandatory for privileged staff;
- passkey support as a later or parallel secure method if selected;
- email verification/invitation for staff onboarding;
- session rotation after authentication and privilege elevation;
- short idle timeout for sensitive roles;
- absolute session lifetime;
- session revocation;
- logout all sessions;
- brute-force and credential-stuffing protection;
- recovery process that cannot bypass staff/security controls;
- no password sharing.

## 2.3 Root Super Administrator

The highest authority role is **Root Super Administrator**.

It may:

- manage staff accounts;
- create/edit/disable roles;
- assign permissions and scope;
- access every business module;
- manage platform settings;
- manage security configuration;
- approve privileged integrations;
- access operations/infrastructure controls permitted by architecture;
- view complete audit history;
- perform controlled emergency actions.

Even Root Super Administrator:

- cannot silently erase immutable audit history;
- must use MFA;
- must re-authenticate for defined critical actions;
- should be protected by the strongest authentication policy;
- should be restricted to the smallest practical number of trusted people.

## 2.4 Permission-first architecture

Roles are bundles of permissions. Permissions are the actual authorization primitive.

Examples:

```text
public_pages.read
public_pages.create
public_pages.edit
public_pages.publish
public_pages.archive
public_html.edit
public_html.trusted_embed
media.read
media.upload
media.import_external
media.delete
translations.read
translations.edit
translations.publish
leads.read
leads.assign
leads.contact
leads.convert_to_client
clients.read
clients.create
clients.update
clients.invite
projects.read
projects.manage
projects.publish_preview
projects.manage_approval
services.read
services.edit
services.retire
plans.read
plans.edit
billing.read
billing.create_invoice
billing.record_payment
campaigns.manage
staff.read
staff.create
staff.manage_roles
security.audit.read
security.sessions.manage
deployments.read
deployments.staging
deployments.production
system.feature_flags.manage
```

## 2.5 Scopes

Authorization should support scope in addition to action.

Possible scopes:

- all records;
- assigned clients only;
- assigned projects only;
- specific country/region;
- specific business unit;
- specific content section;
- specific language(s);
- finance-only scope;
- infrastructure environment scope.

Authorization question:

> **Can this staff user perform this action on this specific object in this scope?**

## 2.6 Contextual navigation and Home

The Admin UI is not a single identical dashboard for everyone.

Navigation and Home widgets are derived from:

- staff identity;
- roles;
- permissions;
- scopes;
- assignments;
- work queue;
- responsibilities.

Example views:

- **Sales:** Leads, Clients, Communications.
- **Content Manager:** Public Website, Content, Media, Localization.
- **Project Manager:** Clients, Websites, Projects, Blueprints, Requests.
- **Finance:** Billing, Plans, Subscriptions, Renewals.
- **Technical Operations:** Websites, Domains, Email, Operations, Deployments.
- **Security:** Staff security, sessions, audit and investigations.
- **Root Super Administrator:** all authorized modules.

---

# 3. Admin Information Architecture

Recommended top-level navigation:

```text
DASHBOARD

SALES
  - Leads
  - Follow-ups
  - Proposals / Quotes

CLIENTS
  - Clients
  - Client Accounts
  - Communications

WEBSITES
  - Website Registry
  - Website Projects
  - Domains
  - Professional Email
  - Root Health

PUBLIC WEBSITE
  - Pages
  - Categories / Hierarchy
  - Navigation
  - Reusable Sections / Blocks
  - Media
  - SEO / Redirects
  - Root Check
  - Forms / Inquiry Wizard

CONTENT
  - Articles / Insights
  - Guides
  - Digital Future
  - Research
  - Stories / Case Studies
  - News
  - FAQs

BLUEPRINTS
  - Website Blueprints
  - Onboarding Templates
  - Palette / Design Options

COMMERCIAL
  - Services
  - Plans
  - Subscriptions
  - Costs / Dependencies
  - Billing
  - Renewals

CLIENT EXPERIENCE
  - Hero Campaigns
  - Notifications
  - Client Dashboard Content
  - Social Profile Types
  - Future Root Network Settings

SUPPORT
  - Requests
  - Work Queue
  - Escalations

LOCALIZATION
  - Languages / Locales
  - Translation Workspace
  - UI Strings
  - Content Translation Status

INTEGRATIONS
  - Provider Registry
  - APIs
  - Embed Providers
  - OAuth / Credentials Status

OPERATIONS
  - Environments
  - Releases / Deployments
  - Jobs / Queues
  - Monitoring
  - Backups / Recovery
  - Infrastructure Inventory

SECURITY
  - Staff Users
  - Roles
  - Permissions
  - Sessions
  - Audit Log
  - Security Events

SYSTEM
  - Feature Flags
  - Global Settings
  - Countries / Currencies
  - Email Templates
  - Legal Versions
  - Taxonomies
  - System Status

REPORTS
  - Sales
  - Clients
  - Projects
  - Revenue / Renewals
  - Services
  - Content
  - Operations
```

Modules not permitted for a user are not shown in navigation and remain inaccessible at the API layer.

---

# 4. Admin Home — Contextual Management Cockpit

## 4.1 Principle

The first screen answers:

> **What needs my attention now?**

It should not be a decorative wall of vanity charts.

## 4.2 Common global signals

Depending on permissions, Home can display:

- new leads awaiting review;
- follow-ups due today;
- clients requiring contact;
- projects waiting on staff action;
- projects waiting on client approval;
- QA items;
- support requests;
- high-priority incidents;
- renewals due;
- overdue invoices;
- domain/email actions;
- failed jobs;
- publication tasks;
- translation gaps;
- deployment status;
- security events.

## 4.3 Personal work queue

Each staff user receives **My Work**.

Work items can originate from any module but retain their source record.

Examples:

- review Lead `LEAD-2026-000124`;
- contact client;
- publish article translation;
- prepare website preview;
- review project QA;
- renew domain;
- reply to Request `REQ-1042`;
- reconcile payment;
- investigate failed background job.

## 4.4 Saved views

Staff may save useful filters such as:

- New Iraqi business leads — last 7 days;
- Websites waiting for client approval;
- Renewals due in 30 days;
- Unpaid invoices;
- Arabic articles missing English translation;
- Failed jobs in Production.

Visibility of saved views follows permissions.

---

# 5. Global Search

One Admin search should be capable of locating permitted records across modules.

Searchable examples:

- client name/email/phone;
- Lead reference;
- website name/domain;
- project reference;
- invoice number;
- support request;
- article title;
- service name;
- domain;
- staff user.

Search results must never reveal unauthorized object metadata merely because the object exists.

---

# 6. Common Admin CRUD / Record UX

For appropriate entities, the standard pattern is:

- List;
- Search;
- Filter;
- Sort;
- View detail;
- Create;
- Edit;
- Duplicate where meaningful;
- Archive;
- Restore;
- History;
- Export where authorized;
- Bulk action where safe.

## 6.1 Destructive-action rules

- Normal content may use Trash/Archive and recovery.
- Active services cannot be hard-deleted while referenced.
- Plan/pricing history is versioned, not overwritten.
- Leads/clients/projects retain conversion/history links.
- Invoices/payments/audit/security records are not casually deleted.
- Permanent purge is restricted, policy-driven and audited.

## 6.2 Optimistic concurrency

Editors must not silently overwrite each other's work.

Use version/revision checks such as:

- updated_at/revision ID;
- conflict warning;
- compare/reload;
- controlled overwrite only with permission.

---

# 7. Public Website CMS Manager

## 7.1 Purpose

Authorized Admin users must be able to manage ordinary public-website content without code deployment.

This includes:

- pages;
- categories;
- subcategories;
- solution pages;
- audience pages;
- Website Blueprint pages;
- service pages;
- pricing content;
- company pages;
- trust/security content;
- knowledge pages;
- contact and CTA content;
- legal pages;
- custom landing pages;
- error/maintenance content;
- structured SEO content;
- reusable sections.

## 7.2 Page hierarchy

A page can be assigned to a parent/section and ordered.

Example:

```text
Solutions
  Personal
    Students
    Graduates
  Professionals
    Doctors
    Lawyers
  Businesses
```

Supported actions:

- create;
- rename;
- move;
- reorder;
- duplicate;
- hide from navigation;
- publish/unpublish;
- schedule;
- archive;
- restore.

Moving a page must evaluate URL/redirect impact before publication.

## 7.3 Content model

A page contains:

- internal title;
- localized public title;
- page type;
- parent;
- slug(s) per locale;
- status;
- layout/template;
- ordered content blocks/sections;
- SEO metadata per locale;
- social preview per locale;
- publication schedule;
- owner/editor;
- version;
- feature/visibility flags;
- analytics/attribution tags where approved;
- structured-data configuration where relevant.

## 7.4 Approved section/component builder

Content editors should usually build pages from protected components such as:

- Hero;
- text block;
- rich HTML block;
- image;
- gallery;
- video/embed;
- CTA;
- feature cards;
- audience cards;
- service cards;
- Website Blueprint card grid;
- pricing table;
- comparison table;
- FAQ;
- testimonial;
- case study;
- statistic/metric;
- process/timeline;
- downloadable resource;
- article feed;
- research feed;
- contact section;
- custom approved block.

Editors can reorder/add/remove supported sections without access to application source code.

---

# 8. Full HTML Editor — Required but Controlled

## 8.1 Editing modes

The public CMS must support:

1. **Visual/Rich Text editor** for ordinary staff.
2. **HTML Source editor** for authorized content staff.
3. **Trusted Embed/HTML block** for specifically privileged staff.

The HTML editor is for **page content markup**, not application source code, server code or production JavaScript bundles.

## 8.2 HTML safety policy

Server-side sanitization is mandatory.

Default allowed content may include safe semantic HTML such as:

- headings;
- paragraphs;
- lists;
- tables;
- links;
- images through Media Manager references;
- blockquotes;
- figure/figcaption;
- safe inline formatting;
- approved iframe/embed elements through controlled provider rules.

Default blocked/stripped content includes:

- `<script>`;
- inline event handlers such as `onclick`;
- unsafe `javascript:` URLs;
- arbitrary `<object>`/`<applet>`;
- uncontrolled forms;
- dangerous CSS/URLs;
- arbitrary external scripts;
- unsafe SVG/script combinations.

## 8.3 Trusted custom HTML

If a legitimate business case requires more permissive HTML:

- permission `public_html.trusted_embed` is required;
- content is previewed in isolation;
- CSP rules apply;
- dangerous script execution remains disabled unless separately engineered;
- publication is audited;
- affected page can be rolled back immediately.

Raw application source-code editing is not provided by the public CMS.

---

# 9. Publication Workflow, Versioning & Rollback

Every public page/content object supports:

- Draft;
- In Review (optional workflow);
- Scheduled;
- Published;
- Unpublished;
- Archived.

Every publish creates a version.

Version record includes:

- version ID;
- editor;
- approver/publisher where separate;
- timestamp;
- content snapshot/change set;
- languages affected;
- publication note/reason;
- rollback source.

Required actions:

- preview draft;
- compare versions;
- restore previous version;
- schedule publish/unpublish;
- cancel schedule;
- publish only selected locale(s);
- publish all ready locales;
- prevent invalid/incomplete page state from publishing.

High-impact legal/security pages may require two-person review later.

---

# 10. Navigation Manager

Admin manages independently:

- primary desktop navigation;
- mobile navigation;
- footer navigation;
- utility links;
- CTA buttons;
- country/language-specific variations where required.

Each item supports:

- localized label;
- destination type: internal page / external URL / action;
- parent/nesting;
- order;
- active dates;
- language visibility;
- audience/country visibility if later approved;
- external-link behavior;
- status.

Broken/dangling page references must be prevented or flagged.

---

# 11. Media Manager — Local + External Rich Media

## 11.1 Supported media classes

The Media Manager supports:

- uploaded images;
- SVG only under controlled sanitization policy;
- downloadable PDFs/documents;
- infographics;
- audio references if later needed;
- video embeds;
- external media embeds;
- YouTube;
- Vimeo or similar approved providers;
- Google Drive shared media/document previews;
- other approved iframe/oEmbed providers;
- external public image/document URL import where explicitly enabled.

## 11.2 Media record

Each asset/embed stores:

- Media ID;
- type;
- source type: local / YouTube / Google Drive / Vimeo / generic provider / remote import;
- source URL or provider identifier;
- title;
- localized title where necessary;
- alt text;
- caption;
- credit/source;
- language;
- tags/collection;
- dimensions/aspect ratio when known;
- file size/MIME for local assets;
- created by;
- created time;
- usage references;
- status;
- privacy/licensing notes when needed.

## 11.3 YouTube and video providers

Editors can paste an approved public URL. The system normalizes it into the canonical embed representation.

Do not require staff to manually write iframe code for common providers.

Provider settings define:

- allowed hostnames;
- URL patterns;
- embed base URL;
- allowed iframe attributes;
- sandbox/referrer policy;
- privacy-enhanced mode where available;
- autoplay policy;
- responsive aspect ratio.

## 11.4 Google Drive

For v1, support public/shared Drive links as link/embed references where the file's sharing policy permits browser access.

Examples of supported uses may include:

- shared video preview;
- shared PDF/document preview;
- download/resource link.

The Admin must never store a user's Google password.

Private Drive OAuth/API import, if ever needed, is a future Integration and must pass provider/cost/security review.

## 11.5 Generic embeds

Generic embed support is **allowlist-based**.

An Admin can paste:

- provider URL; or
- embed HTML if their permission allows it.

The server parses/sanitizes the input and permits only approved:

- iframe hosts;
- attributes;
- protocols;
- dimensions;
- sandbox flags.

No arbitrary `<script src=...>` from unknown providers.

## 11.6 External remote import

If remote media import is later enabled:

- only `https` by default;
- SSRF protection;
- DNS rebinding protection;
- private-network block;
- size limit;
- MIME verification;
- timeout;
- quarantine;
- malware scan for file formats where appropriate;
- safe filename generation;
- metadata stripping where policy requires;
- image re-encoding/optimization where practical.

## 11.7 Media usage map

Before archive/delete, Admin should see:

> **Used on 4 pages / 2 articles / 1 campaign.**

The system prevents destructive deletion of in-use media unless explicitly resolved.

---

# 12. SEO, Redirects & Search Controls

Per page/locale Admin can manage:

- title;
- meta description;
- canonical URL;
- index/noindex;
- follow/nofollow where needed;
- Open Graph title/description/image;
- social card;
- structured-data configuration using supported templates;
- hreflang/language alternatives;
- breadcrumb metadata;
- sitemap inclusion;
- robots exceptions where permitted.

Redirect Manager supports:

- 301;
- 302/temporary where justified;
- source path;
- destination;
- language;
- active dates;
- loop detection;
- conflict prevention;
- hit count optional.

Changing published slugs should prompt for redirect creation.

---

# 13. Knowledge Center / Editorial CMS

Manage content types:

- Insights;
- Guides;
- Digital Future;
- Research;
- Stories / Case Studies;
- News;
- FAQs.

Each item may include:

- title;
- summary;
- rich content / HTML;
- structured sections;
- author;
- source links;
- publication date;
- categories/tags;
- related audience;
- related services;
- related Website Blueprints;
- images/media/embed;
- downloadable research files;
- SEO;
- language variants;
- feature-on-homepage flag;
- schedule;
- revision history.

No AI-generated automatic publishing is required. Future content automation is optional and must be explicitly integrated.

---

# 14. Localization & Translation Management — Unlimited Languages

## 14.1 Locale registry

Admin must be able to add and configure locales such as:

- Arabic (`ar`);
- English (`en`);
- French (`fr`);
- Kurdish variants if later needed;
- any additional language/locale supported by product policy.

Locale fields:

- language code;
- optional region code;
- display name;
- native name;
- direction: LTR / RTL;
- fallback locale;
- active/inactive;
- public website enabled;
- inquiry wizard enabled;
- Client Account enabled;
- default country/currency/date settings where applicable;
- sort/order;
- launch readiness status.

## 14.2 Translation surfaces

The Admin translation system covers:

### Public website

- pages;
- navigation;
- services;
- plans/pricing copy;
- Website Blueprints;
- articles;
- FAQs;
- CTA labels;
- media alt/caption;
- legal content;
- SEO metadata.

### Public inquiry wizard

- wizard title;
- step labels;
- question labels;
- help text;
- options;
- validation messages;
- confirmation message;
- communication/consent text.

### Client Account

- navigation labels;
- static UI copy managed as translation keys;
- Hero/campaign content;
- notifications;
- service descriptions;
- onboarding instructions;
- help text;
- project status display text;
- request/support categories;
- billing labels/help copy;
- email templates.

## 14.3 Translation data model

Use shared logical records plus localized values; do not clone an entire application/page tree per language.

Conceptually:

```text
ContentObject
  id
  type
  canonical configuration

LocalizedContent
  content_object_id
  locale_id
  fields...
  translation_status
  version
```

UI strings use stable translation keys:

```text
client.home.websites_title
client.billing.next_renewal
inquiry.step.about_you
public.cta.start_root
```

## 14.4 Translation states

Per locale:

- Missing;
- Draft;
- Needs Review;
- Ready;
- Published;
- Outdated because source changed;
- Archived.

If a source-language record changes, translations can be flagged as potentially outdated rather than silently treated as current.

## 14.5 Translation workspace

Features:

- side-by-side source and target language;
- field-level translation status;
- search/filter missing translations;
- preview in selected locale;
- direction-aware editor;
- copy source as starting point;
- translation notes;
- version history;
- publish per locale;
- bulk mark/review where authorized.

Machine translation is not required. If added later it is an optional Integration, never a silent dependency.

## 14.6 RTL/LTR

Direction is a property of the locale, not hard-coded to Arabic.

The design system must support:

- layout mirroring where appropriate;
- direction-aware icons/chevrons;
- mixed-direction text;
- phone/email/domain strings displayed safely;
- number/date formatting;
- forms;
- tables;
- editors;
- media captions;
- preview.

---

# 15. Public Inquiry Wizard Manager

The Lead Inquiry Extension v1.1 remains authoritative: public visitors submit an inquiry; they do not self-create Client Accounts.

Admin must manage the wizard through a versioned form-definition system.

## 15.1 Manageable fields

Authorized staff can manage:

- wizard title/introduction;
- step labels;
- questions;
- help text;
- choice lists;
- display order;
- required/optional status where business-safe;
- conditional logic;
- locale translations;
- CTA labels;
- confirmation content;
- active wizard version;
- effective dates.

## 15.2 Protected rules

Routine editors cannot:

- create password/secret questions;
- disable mandatory backend validation;
- bypass security limits;
- expose internal fields;
- publish invalid conditional logic;
- inject executable HTML;
- overwrite old submitted lead schema versions.

## 15.3 Versioning

Each Lead stores the wizard/schema version used.

New wizard versions affect future submissions only.

---

# 16. Leads & Sales CRM

## 16.1 Lead states

Primary workflow:

```text
NEW
-> REVIEWED
-> CONTACT REQUIRED
-> CONTACTED
-> QUALIFIED
-> PROPOSAL / QUOTE
-> WAITING CLIENT
-> ACCEPTED
-> CONVERTED TO CLIENT
```

Alternative outcomes:

```text
NOT QUALIFIED
NO RESPONSE
DECLINED
DUPLICATE
SPAM
ARCHIVED
```

## 16.2 Lead list

Search/filter by:

- Lead reference;
- name;
- email/phone;
- company;
- status;
- priority;
- assigned staff;
- source/campaign;
- audience;
- website/request type;
- country;
- language;
- created date;
- last activity;
- next follow-up;
- conversion state;
- spam/duplicate state.

## 16.3 Lead detail

Sections:

- Summary;
- Inquiry answers;
- Contact;
- Attribution;
- Contact history;
- Internal notes;
- Tasks/follow-up;
- Tags;
- Duplicate checks;
- Proposal/quote links;
- Conversion.

## 16.4 Contact lead

Authorized staff can:

- send/prepare email;
- record phone call;
- record WhatsApp contact;
- record meeting;
- add internal note;
- set follow-up;
- assign/reassign.

Internal notes are never client-visible.

## 16.5 Convert to Client

Only permissioned staff can convert an accepted Lead.

Before conversion, Admin reviews authoritative client fields.

Conversion creates/links:

- Client Account;
- Client Profile;
- initial service/subscription if applicable;
- optional initial Website Project shell;
- account invitation;
- LeadConversion record.

Original Lead remains preserved.

---

# 17. Client Management

## 17.1 Client list

Search/filter by:

- Client ID/reference;
- name;
- primary email;
- phone;
- company;
- country;
- preferred language;
- website/domain;
- status;
- subscription;
- assigned manager;
- renewal state.

## 17.2 Client 360 view

```text
CLIENT SUMMARY
PROFILE
WEBSITES
PROJECTS
SERVICES
SUBSCRIPTIONS
DOMAINS
PROFESSIONAL EMAIL
REQUESTS
BILLING
COMMUNICATIONS
SECURITY / ACCOUNT STATUS
HISTORY
```

## 17.3 Client actions

Depending on permissions:

- edit allowed profile information;
- create/invite Client Account;
- resend activation invitation;
- suspend/reactivate according to policy;
- associate website;
- add service/subscription;
- add domain/email service;
- create request/project;
- contact client;
- view audit history;
- reset specific secure state through approved workflow.

Changing primary account identity/email requires stronger verification and audit.

---

# 18. Website / Digital Root Registry

Every managed website has an Admin record independent of its day-to-day CMS content.

Fields include:

- Website ID;
- client;
- display name;
- website profile/brand name;
- primary domain;
- alternate domains where applicable;
- lifecycle state;
- Website Blueprint;
- project association;
- CMS type;
- CMS base URL;
- CMS SSO endpoint/configuration;
- plan/subscription;
- hosting/environment assignment;
- email-service association;
- launch date;
- renewal state;
- Root Health state;
- operational notes;
- created/updated history.

Actions:

- view public site;
- view website record;
- authorized Admin CMS access through safe Admin SSO if designed;
- manage CMS SSO configuration;
- view project history;
- manage subscriptions/services;
- request/perform policy-controlled suspend/restore;
- view domain/email state;
- view operational health.

No client CMS password should be displayed.

---

# 19. Website Project Management

## 19.1 Internal project model

Client-facing stages remain simple. Internal Admin may use detailed stages/substages.

Project record can include:

- project reference;
- client;
- website;
- Website Blueprint/version;
- onboarding template/version;
- project manager;
- designer;
- developer;
- QA owner;
- internal priority;
- client-visible stage;
- internal stage;
- progress;
- expected milestones;
- blocked reason;
- waiting-on-client flag;
- internal notes;
- client-visible updates;
- preview versions;
- approval records;
- launch checklist;
- launch record.

## 19.2 Internal vs client-visible

Every note/message/update is explicitly classified:

- Internal Only;
- Client Visible.

The API never returns Internal Only data to Client Account endpoints.

## 19.3 Preview and approvals

Admin can:

- register preview URL;
- set preview version;
- publish preview to client;
- request approval;
- record client decision;
- supersede with next version;
- preserve immutable approval history.

## 19.4 Launch

Admin launch checklist can include:

- final design approved;
- content/info ready;
- domain ready;
- email ready;
- QA complete;
- security checks complete;
- client final approval;
- backup/rollback readiness;
- production deploy complete;
- CMS SSO active;
- website state moved to Live.

---

# 20. Website Blueprints

Admin manages the expandable Blueprint universe.

Fields:

- internal Blueprint ID;
- category;
- subcategory;
- localized title;
- localized description;
- target audience;
- recommended pages;
- recommended functions;
- recommended services;
- compatible plans;
- onboarding-template association;
- default project stages;
- design/palette options;
- supported languages;
- public visibility;
- status;
- version.

Blueprints are architectural starting points, not cloned visual templates.

Do not delete a Blueprint version used by an existing project. Retire it for new use.

---

# 21. Onboarding Template Builder

## 21.1 Question/field types

Supported configurable field types may include:

- short text;
- long text;
- email;
- phone;
- URL;
- yes/no;
- radio/single select;
- multi-select;
- checkbox;
- date;
- number;
- color;
- palette choice;
- reference website URL;
- grouped section;
- repeatable structured group only where safe and needed.

## 21.2 Field configuration

- stable field key;
- localized label;
- localized help text;
- type;
- required/optional;
- min/max lengths;
- validation pattern from approved set;
- options;
- conditional visibility;
- order;
- group;
- client-visible;
- internal mapping;
- sensitive-data prohibition/classification;
- version.

## 21.3 Conditional logic

Examples:

```text
IF has_existing_domain = yes
THEN show existing_domain

IF needs_ecommerce = yes
THEN show ecommerce_scope_questions
```

No arbitrary executable code in condition rules.

## 21.4 Versioning

Existing Website Projects retain the exact onboarding-template version they started with.

New versions affect new projects unless an authorized migration is explicitly performed.

---

# 22. Design Directions & Palette Manager

Admin can manage curated design choices shown during New Website intake:

- Professional;
- Minimal;
- Modern;
- Elegant;
- Luxury;
- Creative;
- Technical;
- Friendly;
- Bold;
- Natural;
- custom categories later.

Palette record:

- name;
- localized description;
- representative colors;
- recommended website categories;
- preview image/sample;
- active/inactive;
- order.

These communicate preference to the human design team; they do not auto-generate the site.

---

# 23. Services Catalog

Each service record contains:

- Service ID/code;
- category;
- localized public name;
- localized client-dashboard name;
- internal name;
- public description;
- client description;
- internal fulfillment notes;
- commercial class: Included / Free Integration / Paid Add-on / Custom / Future;
- price model;
- renewal model;
- provider/dependency links;
- cost model;
- human-time estimate/category;
- eligible plans;
- eligible website types;
- eligible countries;
- public visibility;
- Client Account visibility;
- purchase/request availability;
- active/retiring/retired;
- effective dates;
- version/history.

## 23.1 Service retirement

If used by clients, service cannot be hard-deleted.

Allowed lifecycle:

```text
ACTIVE
-> NOT AVAILABLE FOR NEW SALES
-> RETIRING
-> RETIRED
-> ARCHIVED
```

Existing subscriptions remain traceable.

---

# 24. Service Cost & Dependency Registry

For each service/integration:

- software cost;
- API/provider cost;
- infrastructure cost;
- storage;
- bandwidth;
- email cost;
- human fulfillment effort;
- support burden;
- quota/usage risk;
- scale risk;
- provider pricing link/notes;
- fallback;
- reviewed date;
- reviewer.

This supports the Free-First Product Policy and prevents unpriced promises.

Cost details are internal-only and permission protected.

---

# 25. Plans & Pricing

Plan records may include:

- plan family;
- localized name/description;
- audience;
- included services;
- service limits;
- first-year price;
- renewal price;
- currency;
- country/market;
- billing period;
- active dates;
- public visibility;
- client availability;
- upgrade/downgrade rules;
- version.

## 25.1 Price versioning

Never overwrite historical pricing used by existing subscriptions.

Create effective pricing versions:

```text
Plan v1: $150 renewal
Plan v2 effective 2027-01-01: $180 renewal
```

Subscription stores the applicable pricing/version terms.

---

# 26. Subscriptions & Entitlements

A subscription can belong to:

- Client Account;
- specific Website;
- specific service.

Fields:

- subscription ID;
- owner/client;
- website where applicable;
- plan/service;
- status;
- start date;
- renewal date;
- pricing version;
- quantity/limits;
- billing state;
- cancellation/non-renewal state;
- internal notes;
- history.

Admin actions follow permissions and audit requirements.

---

# 27. Domains

Domain record:

- domain;
- Client;
- Website;
- provider/registrar;
- ownership/management status;
- registration date where known;
- renewal/expiry date;
- auto-renew policy/state;
- nameserver/service state;
- health state;
- cost/price association;
- operational notes;
- history.

Normal Admin UI should not expose registrar passwords.

Domain transfer or ownership-sensitive actions require elevated control.

---

# 28. Professional Email

Manage email-service records by domain/client.

Possible fields:

- domain;
- provider;
- service plan;
- mailbox count/limit;
- active mailboxes or references as permitted by provider architecture;
- renewal;
- service status;
- setup instructions;
- cost/price;
- operational notes.

Do not make the Admin Dashboard a raw mail-server console unless explicitly designed later.

---

# 29. Requests & Support

Request types include:

- Major Website Change;
- New Website;
- New Service;
- Domain;
- Professional Email;
- Billing;
- Technical Problem;
- General Support.

Admin features:

- inbox/list;
- search/filter;
- priority;
- status;
- assignment;
- client/site association;
- internal notes;
- client-visible replies;
- due date/SLA if later used;
- resolution;
- closure reason;
- reopen rules;
- escalation.

Website routine content changes remain in client CMS and are not treated as iDigitalRoot requests unless the client asks iDigitalRoot to perform them as a service.

---

# 30. Communications Center

## 30.1 Communication history

Record meaningful outbound/inbound business communication associated with:

- Lead;
- Client;
- Project;
- Request;
- Invoice;
- Renewal;
- Domain/email action.

Channels may include:

- email;
- recorded phone call;
- recorded WhatsApp contact;
- meeting note;
- system notification.

## 30.2 Email templates

Templates can include:

- inquiry confirmation/follow-up;
- request for information;
- consultation;
- proposal;
- client invitation;
- project preview;
- approval required;
- renewal reminder;
- invoice notice;
- payment receipt;
- support reply;
- service announcement.

Templates support unlimited locales and versioning.

## 30.3 Sending

Actual sending provider can be implemented later or through SMTP/provider integration.

Admin product model must support:

- preview;
- localized subject/body;
- recipient validation;
- send permission;
- send log;
- delivery status where provider supports it;
- retry/failure logging;
- suppression/consent rules.

---

# 31. Billing, Quotes, Invoices & Payments

## 31.1 Quote/proposal record

Can store:

- client/lead;
- items;
- quantities;
- prices;
- currency;
- tax treatment where applicable;
- validity date;
- notes;
- version;
- status;
- accepted/rejected state.

## 31.2 Invoice

Fields:

- invoice number;
- client;
- billing identity;
- website/service association;
- issue date;
- due date;
- line items;
- currency;
- subtotal/tax/total;
- payment state;
- terms;
- document version;
- linked subscription/renewal.

## 31.3 Payment

- payment reference;
- amount;
- date;
- method;
- provider/reference if relevant;
- recorded by;
- reconciliation state;
- refund/adjustment references;
- audit history.

Manual payment-state changes require finance permissions and audit.

---

# 32. Renewals

Admin manages renewal schedules for:

- Digital Root plans;
- domains;
- professional email;
- paid add-ons;
- future integrations.

Renewal workflow supports:

- 60/30/14/7-day style reminders as configurable policy;
- client Hero banner;
- email notification;
- invoice generation where applicable;
- payment state;
- non-renewal;
- grace policy;
- suspension/expiration policy;
- completion/renewed state.

Exact business rules remain configurable and audited.

---

# 33. Client Dashboard Content & Hero Campaign Manager

## 33.1 Hero campaign

Fields:

- internal campaign name;
- localized headline;
- localized description;
- image/icon/media;
- CTA label;
- CTA target;
- priority;
- start/end;
- dismissible;
- status;
- target audience rules.

Targeting can include:

- specific Client;
- specific Website;
- plan;
- website type;
- country;
- language;
- active/missing service;
- project stage;
- renewal window;
- global.

Operational/required banners outrank marketing.

## 33.2 Client Dashboard static content

Admin can manage localized explanatory/help copy for supported Client Account surfaces without changing code.

Examples:

- service descriptions;
- onboarding help;
- status explanations;
- support-category descriptions;
- billing help;
- empty states;
- account guidance.

Application logic and security behavior remain code-controlled.

---

# 34. Notifications

Notification types:

- action required;
- important;
- project update;
- renewal/payment;
- service update;
- security;
- system;
- campaign.

Fields:

- recipient/target rules;
- locale;
- title/body;
- CTA;
- delivery channel;
- scheduled time;
- read/dismiss state;
- expiration;
- audit/source.

Notification creation can be manual or deterministic from system events.

---

# 35. Social Profile Configuration

Version 1 Client Account stores manual social-profile URLs only.

Admin manages supported profile types:

- platform name;
- icon;
- URL validation pattern;
- public/client visibility;
- order;
- help text;
- active status.

Future social APIs become Integration records and are not assumed by v1.

---

# 36. Root Health Administration

Admin manages service-health states that the Client Account can display in simple language.

Examples:

- Website Online;
- Domain Active;
- Email Active;
- SSL Healthy;
- Backup Current;
- managed service state.

The Admin operational view may contain deeper technical data.

Client-facing status must never expose sensitive infrastructure details.

Manual overrides require reason and audit.

---

# 37. Root Check Administration

Admin can control:

- check definitions;
- scoring weights/version;
- public explanation text;
- thresholds;
- enabled/disabled checks;
- rate-limit policy;
- job/queue state;
- result retention policy;
- operational errors;
- versioned methodology.

Scoring changes must be versioned so historical results remain interpretable.

Security constraints such as SSRF/private-network blocking are protected system configuration and cannot be disabled by ordinary content staff.

---

# 38. Integrations / API / Provider Registry

The system should be ready to add or retire external providers safely.

Provider record:

- provider name;
- capability;
- provider category;
- official API?;
- API version;
- free/paid;
- pricing/cost notes;
- quota/rate limits;
- commercial-use status;
- terms reviewed date;
- authentication model;
- client authorization required?;
- privacy/data classification;
- environments;
- health status;
- enabled/disabled;
- dependent services;
- fallback;
- responsible owner.

## 38.1 Secret handling

API keys/secrets:

- are not stored as ordinary readable CMS fields;
- should live in a dedicated secrets mechanism;
- are referenced by secret identifier;
- are masked in UI;
- access is highly permissioned;
- viewing/rotation is audited;
- production and staging secrets are separated.

## 38.2 Integration lifecycle

```text
CANDIDATE
-> SECURITY/COST REVIEW
-> APPROVED
-> CONFIGURED
-> TESTING
-> ACTIVE
-> DEGRADED / DISABLED
-> RETIRED
```

---

# 39. Staff Work Queue & Internal Tasks

Admin may provide lightweight internal tasks without becoming a massive project-management suite.

Task fields:

- source module/object;
- title;
- assignee;
- priority;
- due date;
- status;
- internal notes;
- completion record.

Tasks may be generated by deterministic events, e.g.:

- Lead follow-up date reached;
- renewal action due;
- project waits for staff;
- failed job requires review;
- translation incomplete before scheduled publish.

---

# 40. Reporting & Management Analytics

Reports are permission aware and derived from authoritative records.

Potential areas:

### Sales

- inquiries;
- source/campaign;
- qualification rate;
- conversion rate;
- response/follow-up times.

### Clients

- active clients;
- websites per client;
- countries/languages;
- new clients;
- churn/non-renewal.

### Projects

- active projects;
- average stage duration;
- waiting on client/staff;
- launch throughput.

### Commercial

- subscriptions;
- revenue;
- renewals;
- unpaid invoices;
- service adoption;
- internal service cost exposure where authorized.

### Content

- published content;
- language coverage;
- scheduled content;
- public performance metrics where collected.

### Operations

- service health;
- failed jobs;
- deployment outcomes;
- backup/recovery tests;
- incidents.

Reports must state measurement period and definitions.

---

# 41. Feature Flags

Admin-controlled feature flags can enable/disable supported capabilities by:

- environment;
- country;
- locale;
- client cohort;
- staff cohort;
- global state.

Feature flags do not replace authorization.

Critical security features cannot be disabled by ordinary feature-flag permissions.

Every flag change is audited.

---

# 42. System Settings

Configurable examples:

- company name/contact details;
- support email/phone;
- default locale;
- enabled locales;
- countries;
- currencies;
- contact channels;
- public social links;
- maintenance message;
- default SEO values;
- legal-document active versions;
- renewal reminder policy;
- public wizard active version;
- status-page reference;
- system time/date display settings.

Settings are typed and validated. Avoid unsafe arbitrary key/value editing for nontechnical staff.

---

# 43. Legal Version Management

Terms/Privacy/Service conditions may require versioned records:

- document type;
- version;
- locale;
- effective date;
- status;
- published content/PDF;
- acceptance requirement;
- superseded version.

Client/Lead consent/acceptance stores the version accepted.

---

# 44. Internal Notes vs Client-Visible Data

Every module with communication must distinguish:

```text
VISIBILITY = INTERNAL_ONLY
VISIBILITY = CLIENT_VISIBLE
VISIBILITY = PUBLIC
```

Rules:

- internal notes never pass through Client/Public APIs;
- UI uses distinct styling and warnings;
- changing Internal -> Client Visible may require explicit confirmation;
- audit history records visibility changes.

---

# 45. Staff Impersonation / View as Client — Optional Controlled Capability

If implemented for support:

- special permission required;
- reason required;
- short-lived session;
- clear persistent banner: `IMPERSONATION MODE`;
- start/end audited;
- no client password is known or used;
- dangerous client actions may be disabled while impersonating;
- security team can review history.

This capability is optional and should not be enabled merely for convenience.

---

# 46. Security Center

Security module can include:

- staff accounts and MFA compliance;
- failed logins;
- active sessions;
- locked/suspended accounts;
- role/permission changes;
- SSO ticket events;
- client invitation events;
- integration-secret changes;
- production-deployment actions;
- suspicious Admin behavior;
- high-risk audit events;
- public abuse/rate-limit events;
- investigation notes with restricted access.

Security events are not editable business records.

---

# 47. Audit Log

## 47.1 Minimum event properties

- audit event ID;
- timestamp;
- actor type/user;
- role/permission context;
- action;
- target object type/id;
- client/website where relevant;
- before/after values or change reference where safe;
- reason if required;
- request/session correlation ID;
- IP/device metadata where justified;
- success/failure;
- environment.

## 47.2 Required audit examples

- page publish/unpublish/rollback;
- HTML/embed changes;
- language/translation publish;
- lead status/assignment/conversion;
- client creation/invitation/suspension;
- website/project stage changes;
- preview/approval actions;
- service/plan/pricing changes;
- invoice/payment changes;
- renewal changes;
- campaign changes;
- role/permission/staff changes;
- CMS SSO configuration and privileged issuance;
- integration/provider configuration;
- secret rotation/reference changes;
- feature-flag changes;
- deployment actions;
- backup/recovery operations.

Audit retention is policy-driven and should be tamper-resistant.

---

# 48. Admin Input Security

Every Admin field is still untrusted input.

Required:

- server-side schema validation;
- max lengths;
- type validation;
- Unicode normalization where appropriate;
- output encoding;
- HTML sanitization;
- URL validation;
- parameterized database operations/safe ORM;
- CSRF protection;
- rate limiting for sensitive actions;
- authorization on every request;
- object-level access checks;
- content-type/request-size limits;
- anti-XSS CSP;
- safe file/media handling;
- log redaction.

Staff authentication does not make staff input inherently safe.

---

# 49. File / Upload Security

For Admin-managed public media and controlled project files:

- extension allowlist;
- MIME verification;
- maximum size;
- filename normalization/random internal storage key;
- no execute permission;
- quarantine where appropriate;
- malware scanning for risky document types if supported;
- image reprocessing where appropriate;
- reject polyglot/mismatched types where detected;
- storage outside executable web root;
- signed/controlled access for private objects;
- retention rules;
- audit upload/delete actions.

Public inquiry v1.1 continues to disallow arbitrary uploads unless separately designed.

---

# 50. Admin API Architecture

Logical authenticated API groups may include:

```text
/api/admin/dashboard
/api/admin/search
/api/admin/work
/api/admin/public/pages
/api/admin/public/navigation
/api/admin/public/media
/api/admin/public/seo
/api/admin/public/root-check
/api/admin/inquiry-wizard
/api/admin/leads
/api/admin/clients
/api/admin/websites
/api/admin/projects
/api/admin/blueprints
/api/admin/onboarding-templates
/api/admin/services
/api/admin/plans
/api/admin/subscriptions
/api/admin/domains
/api/admin/email-services
/api/admin/requests
/api/admin/billing
/api/admin/renewals
/api/admin/communications
/api/admin/campaigns
/api/admin/notifications
/api/admin/locales
/api/admin/translations
/api/admin/integrations
/api/admin/root-health
/api/admin/staff
/api/admin/roles
/api/admin/permissions
/api/admin/audit
/api/admin/feature-flags
/api/admin/system
/api/admin/operations
/api/admin/deployments
```

Exact routes are implementation details; security contracts are mandatory.

## 50.1 API rules

- authentication required;
- authorization required on every operation;
- object scope verified;
- server validation;
- consistent error model;
- idempotency for duplicate-prone/financial actions;
- rate limits on sensitive actions;
- correlation IDs;
- audit hooks;
- pagination for large lists;
- safe filtering/sorting allowlists;
- no mass assignment;
- no unnecessary database ID leakage.

---

# 51. Shared Core Data Model

Key entities include, at minimum:

```text
StaffUser
Role
Permission
RolePermission
StaffScope
StaffSession
AuditEvent
SecurityEvent

Locale
TranslationKey
TranslationValue
LocalizedContent

Page
PageVersion
PageBlock
NavigationMenu
NavigationItem
MediaAsset
EmbedProvider
Redirect
SEORecord

Article
ArticleCategory
FAQ
CaseStudy
ResearchItem

InquiryWizardDefinition
InquiryWizardVersion
InquiryStep
InquiryField
InquiryOption
Lead
LeadStatusHistory
LeadAssignment
LeadContactActivity
LeadNote
LeadAttribution
LeadConsent
LeadConversion

ClientAccount
ClientProfile
ClientInvitation
Website
WebsiteProfile
WebsiteProject
ProjectStage
ProjectVersion
ProjectPreview
ProjectApproval
WebsiteBlueprint
WebsiteBlueprintVersion
OnboardingTemplate
OnboardingTemplateVersion
OnboardingField
Palette

Service
ServiceVersion
ServiceCostRecord
Plan
PlanVersion
Subscription
Domain
EmailService
MailboxServiceReference
RootHealthRecord

SupportRequest
SupportMessage
InternalNote
Task

Quote
Invoice
InvoiceLine
Payment
Renewal

Campaign
Notification
EmailTemplate
CommunicationLog

Provider
Integration
IntegrationEnvironment
FeatureFlag
SystemSetting
LegalDocumentVersion

Deployment
Environment
JobExecution
BackupRecord
RecoveryTest
OperationalIncident
```

Some records may be implemented with JSON where appropriate, but history, authorization and reporting requirements must remain enforceable.

---

# 52. Background Jobs & Event Processing

Required or likely job types:

- scheduled publication;
- scheduled unpublish;
- email delivery;
- renewal reminders;
- campaign activation/deactivation;
- notification fan-out;
- project reminders;
- Lead follow-up reminders;
- invitation expiry cleanup;
- CMS SSO ticket cleanup;
- Root Check workers;
- health checks;
- media processing;
- backup jobs;
- billing status synchronization if later integrated;
- search indexing;
- translation staleness marking.

Job requirements:

- idempotent where possible;
- bounded retries;
- exponential/backoff strategy where appropriate;
- dead-letter/failure state;
- observable;
- manual retry permissioned;
- audit for privileged manual retry/cancel;
- no hidden infinite retry loops.

---

# 53. Operations & Infrastructure Module

## 53.1 Separation

Operations UI is restricted to technical roles.

Content/Sales/Finance staff should not see infrastructure controls.

## 53.2 Operational inventory

May include:

- applications/services;
- environments;
- domains/certificates;
- deployment target;
- current release;
- health;
- backup status;
- job/queue status;
- database service state;
- storage state;
- CDN/WAF status reference;
- monitoring links;
- provider references.

## 53.3 No raw secrets

Admin records may show secret **status/reference**, not secret value by default.

## 53.4 Environment separation

At minimum:

- Development;
- Staging;
- Production.

Production actions require stronger permissions.

---

# 54. Deployment Management

The proper release path remains:

```text
Source Control
-> Automated Build/Test
-> Staging
-> Approval
-> Production
-> Verification
-> Rollback if required
```

Admin Operations may display and trigger approved pipeline actions, but should not become a browser source-code editor.

Deployment record:

- release ID/version;
- application;
- environment;
- commit/build reference;
- initiator;
- approver if required;
- start/end;
- result;
- health verification;
- rollback reference;
- logs link/reference.

Production deployment may require reauthentication and optionally second approval.

---

# 55. Observability

Admin operations should expose permitted operational signals:

- application availability;
- error rates;
- API errors/latency;
- authentication failures;
- email-delivery failures;
- CMS SSO failures;
- background-job failures;
- Root Check failures;
- database health;
- queue depth;
- deployment status;
- backup status;
- public inquiry error rate;
- client-account critical errors.

Do not expose raw sensitive logs to broad staff roles.

---

# 56. Backups & Disaster Recovery

Back up according to defined policy:

- shared platform database;
- public content;
- media/configuration metadata;
- client-account data;
- project/approval records;
- billing records;
- audit data according to policy;
- configuration;
- critical secrets via the appropriate secure secrets solution, not normal database export.

Requirements:

- retention policy;
- encryption;
- access control;
- off-system/off-account protection where appropriate;
- restore documentation;
- periodic restore tests;
- recorded RecoveryTest result;
- RPO/RTO targets defined during infrastructure phase.

A backup is not considered trustworthy until restore is tested.

---

# 57. Privacy & Data Retention

Admin must support policy-driven retention classes for:

- leads;
- spam;
- client profiles;
- projects;
- communications;
- invoices/payments;
- audit/security logs;
- public inquiry technical metadata;
- expired invitations;
- archived content;
- media.

Deletion/erasure workflows must respect:

- legal obligations;
- accounting/audit requirements;
- security evidence;
- active contracts;
- backup-retention realities.

Sensitive personal data should be minimized.

---

# 58. Admin Responsiveness & Accessibility

The Admin Dashboard is desktop-powerful but fully responsive.

Critical workflows must work on:

- phone;
- tablet;
- desktop.

Complex public page/HTML editing may display **desktop recommended** guidance but should degrade safely on mobile rather than break.

Accessibility target: WCAG 2.2 AA where practical for the internal product.

Requirements include:

- keyboard navigation;
- focus states;
- form labels;
- accessible tables;
- clear validation;
- screen-reader semantics;
- RTL/LTR correctness;
- contrast;
- reduced motion;
- large touch targets on mobile.

---

# 59. Security Testing Requirements

## 59.1 Authentication/authorization

Test:

- login bypass;
- MFA bypass;
- session fixation;
- session hijacking controls;
- disabled-user access;
- role escalation;
- permission bypass;
- scope bypass;
- IDOR/BOLA;
- field-level exposure;
- hidden-module API access.

## 59.2 Content/CMS

Test:

- stored XSS through rich text/HTML;
- iframe/embed bypass;
- unsafe URL schemes;
- malicious SVG;
- media upload bypass;
- HTML sanitizer bypass;
- CSP violations;
- open redirects;
- publishing without permission;
- version rollback authorization.

## 59.3 Business logic

Test:

- unauthorized Lead conversion;
- price/version tampering;
- invoice/payment tampering;
- subscription cross-client access;
- website/project cross-client access;
- client-visible leakage of internal notes;
- CMS SSO misrouting/replay;
- duplicate financial operations.

## 59.4 Integrations/operations

Test:

- secret exposure;
- environment confusion;
- production-action bypass;
- webhook/API replay if later used;
- SSRF in remote media/Root Check;
- deployment authorization;
- audit tampering.

---

# 60. Quality Assurance

Functional QA must include, at minimum:

- every role navigation;
- every permission boundary;
- Super Admin control;
- staff invite/disable;
- public page create/edit/publish/rollback;
- HTML editor safety;
- YouTube/Drive/generic embed flows;
- media usage/deletion protection;
- multilingual page editing;
- Arabic RTL;
- French/English LTR;
- locale fallback;
- wizard version editing/publishing;
- Lead intake to Client conversion;
- Client Account creation/invitation;
- multiple websites per client;
- Website Project lifecycle;
- Blueprint/template versioning;
- service retirement;
- plan pricing versions;
- billing/renewal;
- campaigns;
- support requests;
- API/provider registry;
- audit records;
- feature flags;
- backup/restore record;
- deployment access;
- responsive behavior.

---

# 61. Definition of Done — Admin Dashboard

The Admin Dashboard is production-ready only when:

### Authority

- every staff member uses an individual account;
- MFA and session security work;
- roles/permissions/scopes are enforced server-side;
- Root Super Administrator management works;
- unauthorized modules/actions cannot be reached through direct API calls.

### Public Website Management

- pages/categories/subcategories can be created/edited/reordered/published without code changes;
- full rich text + controlled HTML editing works;
- media uploads and approved external embeds work;
- navigation/SEO/redirects work;
- versioning/rollback/scheduling work;
- arbitrary languages can be added/administered.

### Inquiry / Sales

- public wizard definitions are Admin-managed and versioned;
- new inquiries become structured Leads;
- Lead workflow/contact/assignment/filtering work;
- authorized Lead-to-Client conversion is secure and auditable.

### Client Operations

- Clients, Websites, Projects, Blueprints, onboarding templates, approvals, domains, email, services and requests are manageable according to blueprint contracts.

### Commercial

- services, plans, pricing versions, subscriptions, invoices, payments and renewals are traceable and permission protected.

### Client Experience

- Hero campaigns/notifications/localized Client Account content are Admin controlled;
- internal data cannot leak into client-visible surfaces.

### Localization

- Public Website, Inquiry Wizard and Client Account content/UI strings can be managed in Arabic, English, French and future locales;
- RTL/LTR works per locale;
- translation versions/status/fallback are controlled.

### Security

- audit trail exists;
- privileged actions are protected;
- media/HTML/embed surfaces pass security tests;
- secrets are not exposed as normal fields;
- tenant/object isolation passes tests.

### Operations

- jobs, monitoring, environments, releases and backup state are observable by authorized roles;
- production operations are permission protected;
- tested recovery procedures exist.

---

# 62. Implementation Phasing

The blueprint defines the full target platform. Delivery should be phased without weakening the architecture.

## Phase A — Security/Foundation

- Admin auth;
- Staff/roles/permissions/scopes;
- audit;
- locale registry;
- system settings;
- basic dashboard/work queue.

## Phase B — Public Website CMS

- pages/hierarchy;
- section builder;
- rich/HTML editor;
- media/external embeds;
- navigation;
- SEO;
- versioning/publishing;
- localization.

## Phase C — Inquiry / Leads

- inquiry wizard manager;
- Lead inbox;
- qualification/contact;
- Lead conversion;
- account invitation.

## Phase D — Client / Website Operations

- clients;
- website registry;
- Website Projects;
- Blueprint/template builder;
- approvals/previews;
- domains/email.

## Phase E — Commercial & Support

- services;
- costs/dependencies;
- plans/pricing;
- subscriptions;
- billing/renewals;
- support/requests;
- communications.

## Phase F — Client Experience Controls

- Hero campaigns;
- notifications;
- Client Account translation/content controls;
- Root Health;
- social profile configuration.

## Phase G — Operations

- integration registry;
- monitoring;
- jobs;
- deployments;
- backups/recovery;
- reporting;
- advanced security center.

---

# 63. Final Frozen Architecture Summary

```text
                               iDIGITALROOT
                                    |
                +-------------------+-------------------+
                |                                       |
          PUBLIC WEBSITE                            CLIENT ACCOUNT
                |                                       |
        Inquiry / Lead Wizard                    Multiple Digital Roots
                |                                       |
                +------------------+--------------------+
                                   |
                                   v
                     ADMIN & OPERATIONS DASHBOARD
                                   |
         +-------------------------+--------------------------+
         |              |              |                     |
      CONTENT         SALES          CLIENTS              COMMERCIAL
  Pages / Media     Leads / CRM    Sites / Projects    Services / Billing
  Localization      Conversion     Domains / Email     Renewals / Costs
         |              |              |                     |
         +-------------------------+--------------------------+
                                   |
                              OPERATIONS
                         Integrations / Jobs
                       Deployments / Monitoring
                          Backups / Recovery
                                   |
                              SECURITY
                       Staff / Permissions
                         Audit / Sessions
```

## Final principle

> **The Admin Dashboard is the secure management plane of iDigitalRoot. It must allow authorized staff to operate and evolve the public website, the sales funnel, the Client Account experience, client relationships, website projects, commercial services and technical operations without exposing uncontrolled code, secrets or cross-client data.**

---

# 64. Required Blueprint Synchronization

The accompanying extension document:

`iDigitalRoot_Cross_Platform_Admin_Control_Localization_and_Rich_Media_Extension_v1.0.md`

formally updates the prior Public Website, Client Account and Lead/Inquiry blueprints where the new Admin requirements add:

- unlimited Admin-managed locales;
- Arabic/English/French and future RTL/LTR support;
- Admin-managed translation workflow;
- Client Account UI/content localization administration;
- Admin-managed inquiry wizard localization;
- full public CMS HTML editing with security controls;
- YouTube/Google Drive/approved external embed support;
- shared Admin-managed content/versioning principles.

**END OF BLUEPRINT**
