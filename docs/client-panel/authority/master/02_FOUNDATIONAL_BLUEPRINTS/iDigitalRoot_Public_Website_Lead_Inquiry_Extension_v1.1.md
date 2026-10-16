# iDigitalRoot Public Website — Lead / Inquiry Extension v1.1

**Status:** FINAL EXTENSION — Approved Product Direction  
**Applies to:** `iDigitalRoot_Public_Website_Product_Technical_Blueprint_v1.0_Candidate`  
**Purpose:** Replace public self-signup with a controlled visitor inquiry and qualification workflow that feeds the future iDigitalRoot Admin & Operations Dashboard.  
**Date:** September 2026

---

## 0. Document Control

This extension modifies the public acquisition and account-creation flow defined in the Public Website Blueprint v1.0 Candidate.

It does **not** replace the full Public Website Blueprint. All previously approved public-site principles remain valid unless explicitly superseded here.

### 0.1 Authoritative change

The following rule is now permanent:

> **No visitor can create an iDigitalRoot Client Account directly from the public website.**

A public visitor may submit an inquiry, but a Client Account is created only after iDigitalRoot reviews the inquiry, contacts the visitor, qualifies the request, and accepts the visitor as a client.

### 0.2 Superseded flow

The previous public flow:

```text
Start My Digital Root
  -> visitor onboarding
  -> create account
  -> client portal
```

is superseded by:

```text
Start My Digital Root
  -> Public Inquiry Wizard
  -> Submit Inquiry
  -> Admin Lead Inbox
  -> Human Review / Contact / Qualification
  -> Proposal / Agreement / Acceptance
  -> Admin Creates Client Account
  -> Client Receives Activation Invitation
  -> Client Activates Account
  -> Client Account Dashboard
```

### 0.3 Relationship to the Client Account Blueprint

The public inquiry wizard is **not** the same as the detailed New Website onboarding that exists inside the Client Account.

- **Public inquiry wizard:** lightweight qualification and sales intake for a person who is not yet a client.
- **Client New Website onboarding:** detailed Website Blueprint-specific project intake for an accepted client who requests a website.

This separation is mandatory.

---

# PART A — PRODUCT PURPOSE

## 1. Why the inquiry workflow exists

The public website should make it easy for a serious prospect to explain what they need without forcing them to create an account first.

The inquiry workflow must:

- understand who the visitor is;
- understand broadly what they need;
- understand whether they already have a website/domain/digital presence;
- capture the visitor's main goals and requirements;
- collect enough contact information for iDigitalRoot to respond intelligently;
- preserve attribution and language context;
- protect the platform from spam, abuse, malformed input, and automation attacks;
- create a structured Lead record in the Admin Dashboard;
- support a professional human sales/qualification process;
- create a clean path from Lead -> Client -> Website Project without asking the person to repeat information unnecessarily.

## 2. What the inquiry workflow must NOT do

The public inquiry workflow must not:

- create a Client Account automatically;
- collect payment automatically unless a later commercial model explicitly introduces that step;
- create production websites automatically;
- create CMS credentials;
- create domain/email services automatically;
- expose internal pricing logic, operational notes, or cost information;
- request passwords for social media, existing hosting, registrar accounts, email, or websites;
- ask the full detailed profession-specific onboarding questionnaire before the visitor becomes a client;
- use AI chatbots or AI APIs in v1.1;
- depend on paid external APIs in v1.1.

---

# PART B — PUBLIC EXPERIENCE

## 3. Entry points

The inquiry wizard may be entered from relevant public CTAs such as:

- **Start My Digital Root**
- **Build My Professional Identity**
- **Build My Business Root**
- **Build My Organization Root**
- **Talk to iDigitalRoot**
- **Request a Website**
- contextual CTAs from audience/solution/blueprint pages.

The CTA may pass context into the wizard, such as:

- selected audience;
- selected goal;
- selected solution page;
- selected Website Blueprint;
- selected plan interest;
- public Root Check result, if applicable;
- language;
- country when explicitly provided by the visitor;
- campaign/UTM attribution.

The visitor should not need to reselect information already chosen immediately before opening the wizard.

## 4. Wizard experience principles

The wizard must be:

- progressive rather than one long form;
- mobile-first and fully responsive;
- Arabic RTL and English LTR from the beginning;
- easy to understand without technical knowledge;
- fast enough that a visitor can complete it in a few minutes;
- clear about why each important field is requested;
- able to preserve progress during the current browser session;
- safe against malformed or hostile input;
- explicit that submission is an inquiry, not an automatic purchase or account creation.

### 4.1 Suggested progress presentation

Example:

```text
1. About You
2. What You Need
3. Your Goals
4. Current Presence
5. Main Requirements
6. Additional Information
7. Contact Details
8. Review & Submit
```

The progress indicator must reflect actual wizard steps, not artificial gamification.

---

# PART C — PUBLIC INQUIRY WIZARD

## 5. Step 1 — About You

Question:

> **Who are you building your Digital Root for?**

Candidate choices:

- Individual
- Student
- Graduate / Job Seeker
- Professional
- Freelancer / Consultant
- Creator
- Entrepreneur / Founder
- Business
- Organization / NGO / Association
- School / College / University / Education
- Healthcare / Clinic / Medical
- Other

Rules:

- one primary category is required;
- Admin may later manage public category labels and availability;
- the selected category may influence later questions;
- the category must map to the internal Audience taxonomy rather than being stored only as free text.

## 6. Step 2 — What do you need?

Question:

> **What would you like iDigitalRoot to help you build?**

Candidate choices:

- My first website
- Replace / redesign an existing website
- Personal professional website
- Portfolio website
- Business website
- Organization website
- Ecommerce website
- Website with booking / appointments
- Knowledge / news / publication website
- Custom digital solution
- I am not sure yet

Rules:

- allow one primary request type;
- allow additional needs when useful;
- if a specific public Website Blueprint was selected before entering the wizard, display it as context but allow the visitor to change it.

## 7. Step 3 — Goals

Question:

> **What should your website or Digital Root help you achieve?**

Multi-select candidate goals:

- Present myself professionally
- Build credibility
- Be discovered online
- Get hired / attract career opportunities
- Get customers / leads
- Show my work / portfolio
- Present services
- Sell products
- Receive bookings / appointments
- Publish articles / knowledge / news
- Present an organization or initiative
- Recruit people
- Centralize my digital identity
- Connect my social presence
- Other

At least one goal should be required unless the visitor selects **Not sure yet**.

## 8. Step 4 — Current Digital Presence

Questions may include:

### 8.1 Existing website

- I do not have a website
- I have a website
- I have more than one website

If website exists:

- existing website URL(s)

### 8.2 Domain

- I already own a domain
- I need a domain
- I need help choosing a domain
- Not sure

If domain exists:

- domain name

### 8.3 Professional email

- Yes
- No
- Not sure

Optional public information only. The visitor must never be asked for credentials.

### 8.4 Social presence

Optional URLs or platform selections may be collected, but no passwords, tokens, or external-account authentication are requested in v1.1.

## 9. Step 5 — Main Website Requirements

The public wizard should collect only enough information for qualification.

Candidate fields:

### 9.1 Languages

- Arabic
- English
- Arabic + English
- Other / multiple languages

### 9.2 Approximate scope

- Simple presence / small website
- Medium business/professional website
- Larger multi-section website
- Advanced/custom website
- Not sure

Do not require visitors to understand page counts if they do not know.

### 9.3 Common functions

Multi-select:

- Contact form
- WhatsApp/contact actions
- Maps/location
- Portfolio/projects
- Blog/news/articles
- Booking/appointments
- Ecommerce/products
- Documents/resources
- Careers/jobs
- Membership/login
- Multiple locations/branches
- Multilingual
- Other
- Not sure

### 9.4 Existing content

Optional:

- I already have most content
- I have some content
- I need help organizing content
- Not sure

### 9.5 Desired timing

Optional high-level field:

- As soon as practical
- Within 1 month
- Within 1–3 months
- Later / planning stage
- Not sure

This must not be presented as a guaranteed delivery commitment.

## 10. Step 6 — Additional Information

Prompt:

> **Tell us anything important about what you want to build.**

Use a bounded plain-text textarea.

Security requirements:

- strict maximum length;
- plain text by default;
- no raw HTML execution;
- output encoding everywhere;
- server-side validation;
- logging must avoid exposing unnecessarily sensitive text.

## 11. Step 7 — Contact Details

Required/optional candidate fields:

- Full name — required
- Company / organization name — optional
- Email — required
- Phone — required or optional according to final sales policy
- Country — required or optional according to final business rules
- City — optional
- Preferred contact method — Email / Phone / WhatsApp where operationally supported
- Preferred language — Arabic / English
- Best time to contact — optional

### 11.1 Communication consent

Where required by applicable law or operational policy, separate:

- consent to be contacted regarding this inquiry;
- optional marketing/newsletter consent.

Submitting an inquiry must not silently subscribe the visitor to marketing communications.

## 12. Step 8 — Review & Submit

Before submission, show a clean summary:

- visitor type;
- request type;
- goals;
- existing website/domain state;
- main functions;
- languages;
- additional information;
- contact details.

Actions:

- **Back & Edit**
- **Submit Inquiry**

The final CTA should not say **Create Account**.

### 12.1 Confirmation copy

After successful submission:

> **Thank you. Your request has been received.**
>
> iDigitalRoot will review your requirements and contact you using the details you provided.

Optional:

- display a public inquiry reference number;
- send a confirmation email if mail delivery is configured;
- offer a link back to relevant public resources.

Do not expose internal lead qualification status publicly.

---

# PART D — LEAD RECORD & ADMIN HANDOFF

## 13. Lead creation

Every successful public submission creates a structured Lead record.

Suggested identifier:

```text
LEAD-2026-000124
```

Internal database identifiers must remain stable and separate from display/reference numbers.

## 14. Lead fields

A Lead should be capable of storing:

### 14.1 Identity and contact

- internal Lead ID
- public/display reference
- full name
- company/organization
- email
- phone
- country
- city
- preferred language
- preferred contact method
- best contact time, if collected

### 14.2 Inquiry context

- audience category
- request type
- goals
- selected public Website Blueprint, if any
- selected plan interest, if any
- existing website URLs
- domain state / domain name
- professional email state
- social-profile references, if supplied
- requested languages
- website scope
- requested functions
- content readiness
- desired timing
- free-text message

### 14.3 Attribution

- landing page
- referring URL where available and appropriate
- campaign
- UTM source
- UTM medium
- UTM campaign
- UTM term/content if used
- CTA/source page
- language
- public Root Check reference/result if intentionally passed into the inquiry

### 14.4 Technical intake metadata

- created timestamp
- submitted IP metadata only to the extent justified for security/abuse controls and privacy policy
- user agent where operationally justified
- anti-spam outcome
- rate-limit/security flags
- form/wizard version
- privacy/consent version accepted

### 14.5 Admin workflow data

- lead status
- assigned staff user
- priority
- qualification notes
- next follow-up date/time
- contact history
- internal tags
- duplicate relationship if detected
- conversion state
- linked Client ID after conversion
- linked Website Project ID if created
- archival reason where applicable

---

# PART E — LEAD LIFECYCLE

## 15. Lead status model

Recommended primary workflow:

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

The exact display wording may later be refined, but the database/state model must prevent ambiguous free-text statuses.

## 16. Status rules

- every status change is timestamped;
- every status change records the staff user responsible;
- status history is preserved;
- converting a lead must not delete the original lead;
- a converted lead remains linked to the resulting Client Account;
- rejected/spam/archived leads remain available to authorized staff according to retention policy;
- sensitive internal notes are never client-visible.

---

# PART F — ADMIN LEAD INBOX CONTRACT

## 17. Admin Lead Inbox

The future Admin Dashboard must provide a Leads area with at least:

- list view;
- search;
- filters;
- sorting;
- status;
- priority;
- assignment;
- source/campaign;
- customer type;
- website type;
- country;
- language;
- date range;
- next follow-up;
- duplicate/spam state;
- conversion state.

## 18. Lead list columns

Candidate columns:

- Lead Ref
- Name
- Company
- Request Type
- Audience
- Country
- Source
- Status
- Assigned To
- Created
- Last Activity
- Next Follow-up

Columns should be configurable or responsive so the screen remains usable.

## 19. Lead detail page

The Admin Lead detail view should group information into:

### Summary

- who the visitor is;
- what they want;
- urgency/timing;
- current status;
- assigned staff;
- next action.

### Inquiry

- full wizard answers;
- existing site/domain information;
- goals;
- functions;
- language;
- selected blueprint/plan interest.

### Contact

- email;
- phone;
- preferred contact method;
- contact history.

### Attribution

- page/campaign/source/UTM information.

### Internal

- qualification notes;
- tags;
- priority;
- follow-up;
- duplicate/spam controls;
- internal activity history.

### Conversion

- Convert to Client action, when permitted.

---

# PART G — HUMAN CONTACT & COMMUNICATION

## 20. Contacting a lead

Authorized Admin users should be able to initiate or record contact with the lead.

Supported operational paths may include:

- email;
- phone-call record;
- WhatsApp/contact record where business policy supports it;
- meeting/consultation note;
- other approved communication channel.

The Admin Dashboard should record meaningful contact history even when the external communication itself occurs outside the platform.

## 21. Email templates

Future Admin may support structured templates such as:

- inquiry received;
- request for more information;
- consultation invitation;
- proposal sent;
- follow-up;
- accepted / next steps;
- not proceeding.

Templates must support Arabic and English independently.

No email template should expose internal notes, internal pricing calculations, infrastructure information, or security details.

---

# PART H — LEAD TO CLIENT CONVERSION

## 22. Conversion principle

A Lead may become a Client only through an authorized Admin action.

There is no public self-conversion.

## 23. Convert to Client workflow

```text
Qualified / Accepted Lead
  -> Authorized Admin selects Convert to Client
  -> System shows conversion review
  -> Admin verifies client identity/contact information
  -> Admin confirms account owner email
  -> Admin selects/creates initial services as applicable
  -> Admin optionally creates initial Website Project shell
  -> System creates Client Account
  -> Lead is linked to Client Account
  -> System generates secure activation invitation
  -> Invitation sent to client
  -> Client activates account and configures credentials/security
  -> Client can access Client Account Dashboard
```

## 24. Conversion review screen

Must show before confirmation:

- client/account name;
- primary contact name;
- primary email;
- phone;
- country;
- preferred language;
- company/organization, if applicable;
- accepted service/plan where already agreed;
- website request summary;
- domain information;
- whether an initial Website Project should be created;
- assigned client manager/project owner where applicable.

The system must not blindly copy every public form field into authoritative Client records.

The Admin confirms which values become authoritative Client data.

## 25. Duplicate protection

Before client creation, check for possible existing:

- Client Account with the same email;
- active/past Lead with the same email;
- same phone where appropriate;
- same business/domain.

Do not automatically merge records without authorized review.

## 26. Account invitation

Invitation requirements:

- cryptographically strong random token;
- single-use;
- limited lifetime;
- bound to the intended account/email;
- stored safely (prefer hashed token storage where appropriate);
- invalid after successful activation;
- invalidated when regenerated;
- audited issuance and redemption;
- safe error response that does not reveal sensitive account information.

The invitation may lead the client through:

- confirm identity/email;
- set password if password-based auth is used;
- enable MFA when required/recommended;
- accept active terms/privacy/service documents;
- enter Client Account.

---

# PART I — HANDOFF TO FIRST WEBSITE PROJECT

## 27. Reuse of public inquiry data

Once converted, the client should not be forced to re-enter basic information already provided.

Appropriate inquiry fields may prefill the first New Website onboarding as **draft/reference values**, such as:

- website type;
- goals;
- existing domain;
- requested languages;
- requested functions;
- existing website URL;
- general project notes.

However:

- detailed Website Blueprint onboarding still occurs inside the Client Account;
- the client can confirm/correct prefilled information;
- public inquiry data is not assumed to be fully authoritative project data;
- project-specific fields remain separate from the Client Profile.

## 28. Multi-website compatibility

This extension must not assume one client = one website.

The converted Client Account may later create multiple Website Projects, each with independent:

- Website Profile;
- Blueprint;
- onboarding answers;
- domain;
- CMS;
- plan/subscription;
- lifecycle;
- approvals;
- support history.

---

# PART J — PUBLIC FORM SECURITY

## 29. Zero-trust input rule

Every visitor input is untrusted.

All validation must occur on the server even if client-side validation also exists.

## 30. Required controls

At minimum:

- strict field schemas;
- maximum field lengths;
- type validation;
- email normalization/validation;
- phone normalization where practical;
- URL allowlisting to `http`/`https` where URL fields are accepted;
- Unicode normalization where appropriate;
- output encoding;
- HTML sanitization only if any formatted content is explicitly supported;
- parameterized database operations / safe ORM usage;
- CSRF protection where applicable;
- rate limiting;
- bot/spam protection;
- request body limits;
- secure cookies for session state;
- Content Security Policy and secure HTTP headers;
- log redaction for sensitive data;
- no executable uploads in the ordinary inquiry wizard;
- no credential/password fields for external services.

## 31. Spam and abuse controls

The public inquiry endpoint should support layered abuse controls such as:

- IP/request rate limits;
- form/session rate limits;
- bot challenge where justified;
- hidden honeypot or equivalent passive signal where appropriate;
- repeated-content detection;
- disposable/invalid input checks where economically justified;
- server-side duplicate submission protection;
- abuse flags rather than immediate destructive deletion;
- security monitoring for abnormal submission patterns.

No single third-party anti-spam provider should become an unavoidable dependency if a simpler safe approach is sufficient.

## 32. Idempotent submission

A user double-clicking Submit or retrying after a network interruption must not create multiple identical leads whenever the system can safely detect the retry.

Use a submission/request token or equivalent idempotency strategy.

## 33. No arbitrary file uploads in v1.1

The initial public inquiry wizard should **not** support arbitrary file uploads.

Reasons include:

- malware;
- macro documents;
- parser exploits;
- storage abuse;
- sensitive-data leakage;
- malicious filenames/content.

If iDigitalRoot later requires documents from a prospect, use a separately designed controlled upload flow with allowlists, size limits, isolated/quarantine storage, malware scanning, and explicit retention rules.

---

# PART K — PRIVACY, CONSENT & RETENTION

## 34. Data minimization

Collect only information useful for:

- responding to the inquiry;
- qualification;
- preparing a relevant proposal/solution;
- converting an accepted prospect into a client;
- security and abuse prevention;
- lawful business records.

Do not collect unnecessary sensitive personal information.

## 35. Privacy notice

Before submission, the visitor must have access to the relevant privacy information describing:

- what is collected;
- why it is collected;
- how iDigitalRoot will contact them;
- retention principles;
- applicable rights/processes;
- third parties/processors where relevant.

## 36. Marketing consent separation

Inquiry follow-up is not the same as marketing subscription.

If newsletters/promotional communications are offered, consent must be distinct where required.

## 37. Retention

The final retention schedule will be defined in the security/privacy architecture, but the system must support different retention policies for:

- spam;
- rejected leads;
- no-response leads;
- qualified leads;
- converted leads;
- communication history;
- security metadata.

Deletion/retention operations must respect audit/legal requirements.

---

# PART L — INTERNATIONALIZATION & ACCESSIBILITY

## 38. Languages

Initial first-class languages:

- Arabic
- English

Requirements:

- complete RTL/LTR support;
- translated wizard questions and choices;
- localized validation messages;
- localized confirmation page;
- localized confirmation emails if used;
- preferred language stored with the Lead;
- Admin can see the language used by the visitor.

## 39. Accessibility

The wizard follows the public website's WCAG 2.2 AA target.

At minimum:

- semantic form controls;
- labels associated with inputs;
- keyboard completion;
- visible focus;
- clear error summaries;
- field-level validation messages;
- sufficient contrast;
- logical heading structure;
- no information conveyed only by color;
- screen-reader-compatible step/progress state;
- reduced-motion support where animations exist.

---

# PART M — RESPONSIVE & UX REQUIREMENTS

## 40. Mobile-first completion

A visitor must be able to complete the full wizard comfortably on a phone.

Requirements:

- no horizontal scrolling;
- large touch targets;
- correct virtual keyboard/input types;
- short step pages;
- save current step while moving forward/back;
- preserve entered values on validation errors;
- obvious Back/Next controls;
- clear final Submit action;
- Arabic mobile typography and wrapping tested thoroughly.

## 41. Error states

Design dedicated states for:

- validation errors;
- connectivity interruption;
- expired browser/session draft;
- duplicate submission;
- service temporarily unavailable;
- rate limit;
- submission failure;
- successful resubmission after retry.

Never lose the visitor's entered information unnecessarily after a recoverable error.

---

# PART N — ANALYTICS & ATTRIBUTION

## 42. Public funnel events

The public analytics model may track privacy-appropriate events such as:

- inquiry wizard opened;
- step reached;
- wizard abandoned;
- wizard submitted;
- submission success/failure;
- CTA source;
- selected audience;
- selected goal;
- selected website type;
- language.

Do not record raw free-text inquiry content in analytics systems.

## 43. Lead attribution

Preserve relevant acquisition context so Admin can later understand:

- which pages produce inquiries;
- which campaigns produce qualified leads;
- which audience pages convert;
- which Website Blueprints attract demand;
- which languages/countries generate interest.

Attribution must never be treated as more precise than the underlying data supports.

---

# PART O — DATA MODEL EXTENSION

## 44. New / refined entities

The Public Website Blueprint's existing `Lead` concept is now expanded into a formal acquisition model.

Recommended entities/records:

```text
Lead
LeadAnswer / LeadInquiryData
LeadStatusHistory
LeadAssignment
LeadContactActivity
LeadNote
LeadTag
LeadAttribution
LeadConsent
LeadConversion
LeadSecurityFlag
InquiryWizardDefinition
InquiryWizardVersion
```

Some of these may be implemented as normalized tables or structured records according to the final shared data architecture; the functional separation is what matters here.

## 45. Inquiry wizard versioning

Every submitted Lead should retain the wizard/schema version used.

If the public wizard later changes, old Leads remain interpretable.

Do not rewrite historical inquiry answers to match newer question definitions.

---

# PART P — API / BACKEND CONTRACT

## 46. Public inquiry API boundary

Candidate logical endpoints:

```text
GET  /api/public/inquiry/schema
POST /api/public/inquiry/draft        [optional if server-side draft persistence is used]
POST /api/public/inquiry/submit
GET  /api/public/inquiry/status/:publicReference   [only if a safe public status use case is later approved]
```

The initial product does **not** need a public lead-status endpoint.

## 47. Admin lead endpoints

Authenticated Admin-only logical boundaries may include:

```text
GET    /api/admin/leads
GET    /api/admin/leads/:id
PATCH  /api/admin/leads/:id
POST   /api/admin/leads/:id/assign
POST   /api/admin/leads/:id/contact
POST   /api/admin/leads/:id/status
POST   /api/admin/leads/:id/convert
POST   /api/admin/leads/:id/archive
POST   /api/admin/leads/:id/restore
```

Exact routing is finalized in the shared API architecture.

All Admin actions require authorization checks, not merely hidden UI controls.

---

# PART Q — ADMIN PERMISSIONS REQUIRED BY THIS EXTENSION

## 48. Permission families

The future Admin RBAC/permission system should be able to distinguish actions such as:

```text
leads.read
leads.create_manual
leads.update
leads.assign
leads.contact
leads.change_status
leads.add_internal_note
leads.archive
leads.restore
leads.mark_spam
leads.convert_to_client
leads.export
leads.manage_tags
lead_wizard.read
lead_wizard.edit
lead_wizard.publish
```

The Super Administrator may hold all permissions, but ordinary staff see only modules and actions relevant to their role/scope.

## 49. Audit events

Audit at least:

- Lead status changes;
- assignment changes;
- contact records;
- priority changes;
- internal-note creation/edits according to final note policy;
- spam/archive/restore actions;
- conversion to Client;
- invitation issuance;
- duplicate linking/merge decisions if later supported;
- inquiry-wizard configuration changes;
- inquiry-wizard publishing/version changes.

---

# PART R — PUBLIC WEBSITE CMS REQUIREMENTS FROM THIS EXTENSION

## 50. Admin-manageable public inquiry content

The future Public Website Manager should allow authorized staff to manage without code changes:

- wizard title/introduction;
- step labels;
- question labels;
- help text;
- select/multi-select choices;
- required/optional status where business-safe;
- display order;
- conditional visibility;
- CTA text;
- confirmation message;
- Arabic and English content;
- active wizard version;
- effective publication date.

## 51. Guardrails

Admin content editing must not allow routine users to:

- inject arbitrary JavaScript;
- disable mandatory security validation;
- bypass backend required-field rules;
- expose internal fields;
- collect passwords/secrets through custom questions;
- modify protected system identifiers;
- publish an invalid wizard schema.

Publishing a new wizard version should pass validation first.

---

# PART S — OPERATIONAL RULES

## 52. No automatic customer promise

Submitting the inquiry does not guarantee:

- acceptance as client;
- quoted price;
- domain availability;
- delivery timeline;
- requested functionality;
- plan eligibility.

All commercial and delivery commitments occur after human review.

## 53. Manual qualification is intentional

The absence of self-signup is not a temporary limitation.

It reflects the iDigitalRoot managed-service model:

> iDigitalRoot first understands the client, then creates the appropriate professional relationship and Digital Root solution.

## 54. No AI dependency

The v1.1 inquiry system contains no AI chatbot, AI qualification service, or LLM API dependency.

Classification/recommendation may use deterministic rules only where needed.

Future AI features require separate product approval, cost/dependency review, privacy review, and explicit integration classification.

## 55. Free-first principle

Core inquiry intake should rely on iDigitalRoot's own application stack and standard web capabilities.

Paid external providers are not required for the fundamental Lead workflow.

---

# PART T — QA & SECURITY TESTING

## 56. Functional QA

Test at minimum:

- Arabic wizard end-to-end;
- English wizard end-to-end;
- all major visitor categories;
- all conditional branches;
- Back/Next behavior;
- browser refresh/session behavior;
- validation errors;
- successful submission;
- duplicate/double submission;
- Admin Lead creation;
- attribution capture;
- Lead status workflow;
- assignment;
- communication history;
- conversion to Client;
- invitation creation;
- first Client Account activation;
- prefill/handoff into first Website Project where applicable;
- responsive/mobile completion.

## 57. Security QA

Test at minimum:

- XSS payloads in every text field;
- SQL/ORM injection attempts;
- oversized inputs;
- malformed Unicode;
- invalid/hostile URLs;
- CSRF where relevant;
- automated submission bursts;
- rate-limit enforcement;
- bot-control bypass attempts;
- duplicate submission/replay;
- Admin authorization bypass;
- IDOR/BOLA on Lead IDs;
- unauthorized Lead export;
- unauthorized Lead conversion;
- invitation-token replay/expiry;
- log/analytics leakage of sensitive text;
- privilege escalation from Lead-management roles.

## 58. Accessibility QA

Test:

- keyboard-only completion;
- screen-reader labels;
- focus order;
- error announcements;
- RTL form flow;
- mobile zoom/readability;
- contrast;
- touch target sizing.

---

# PART U — DEFINITION OF DONE

## 59. Public Inquiry Extension v1.1 is complete when

### Product

- No public self-signup remains in the customer acquisition flow.
- `Start My Digital Root` leads to the approved inquiry flow.
- The visitor understands they are submitting a request for review.

### UX

- Wizard is progressive, simple, responsive, Arabic/English, and easy to finish.
- Visitor can review before submitting.
- Confirmation is clear and professional.

### Lead Management

- Every valid submission creates one structured Lead.
- Lead has stable identity, lifecycle, attribution, assignment, and history.
- Admin can search/filter/view/update/assign/contact/archive/restore according to permissions.

### Conversion

- Only authorized Admin staff can convert a Lead to a Client.
- Conversion preserves the original Lead.
- Client Account creation is controlled.
- Activation invitation is secure and auditable.
- Relevant inquiry data can prefill the first Website Project without collapsing Lead, Client, and Website Profile boundaries.

### Security

- Server-side validation is complete.
- Abuse controls are active.
- No external credentials are requested.
- No arbitrary file uploads are present in v1.1.
- Admin access is permission-controlled and audited.

### Operations

- Wizard content is manageable through the future Admin Public Website Manager.
- Schema/configuration changes are versioned.
- Historical Leads remain interpretable.

---

# PART V — AUTHORITATIVE SYSTEM FLOW

## 60. Final acquisition-to-client flow

```text
PUBLIC VISITOR
      |
      v
PUBLIC WEBSITE
      |
      v
START MY DIGITAL ROOT
      |
      v
PUBLIC INQUIRY WIZARD
      |
      v
VALIDATE + SECURE SUBMISSION
      |
      v
LEAD CREATED
      |
      v
ADMIN DASHBOARD — LEADS
      |
      +--> Review
      +--> Assign
      +--> Contact
      +--> Qualify
      +--> Proposal / Quote
      +--> Follow-up
      |
      v
ACCEPTED
      |
      v
AUTHORIZED ADMIN
CONVERT TO CLIENT
      |
      v
CLIENT ACCOUNT CREATED
      |
      v
SECURE ACTIVATION INVITATION
      |
      v
CLIENT ACTIVATES ACCOUNT
      |
      v
iDIGITALROOT CLIENT DASHBOARD
      |
      v
DETAILED NEW WEBSITE ONBOARDING
      |
      v
WEBSITE PROJECT
```

---

# 61. Frozen Decisions in Extension v1.1

The following decisions are considered approved and should carry forward into the Admin & Operations Dashboard Blueprint and shared platform architecture:

1. There is no public self-registration for iDigitalRoot Client Accounts.
2. Public visitors submit inquiries through a progressive wizard.
3. The public wizard collects qualification-level information, not full project onboarding.
4. Detailed Website Blueprint-specific onboarding occurs only after the person becomes a client and requests a website.
5. Each successful inquiry creates a structured Lead record.
6. Leads are reviewed and managed by authorized iDigitalRoot staff.
7. Lead lifecycle/status history is preserved.
8. Human review/contact/qualification occurs before Client Account creation.
9. Only authorized Admin users can convert a Lead into a Client.
10. Conversion does not delete or overwrite the original Lead.
11. Client Accounts are created by Admin and activated through a secure invitation.
12. Relevant inquiry data may prefill a future Website Project but must remain distinct from authoritative Client and Website records.
13. The system supports clients owning multiple websites/Digital Roots.
14. No AI chatbot or AI API is required in v1.1.
15. No paid external API is required for the core inquiry workflow.
16. No social/external account passwords are ever collected through the inquiry wizard.
17. No arbitrary public file upload is included in v1.1.
18. Public inquiry inputs are handled as hostile/untrusted data and validated server-side.
19. Lead operations are permission-controlled and audited.
20. Inquiry wizard content/configuration is managed through the future Admin Dashboard with protected schema/security rules.
21. Arabic and English are first-class throughout the inquiry and Admin handoff.
22. Mobile completion is mandatory.
23. Inquiry follow-up consent and marketing consent remain distinct where applicable.
24. The Admin Dashboard becomes the authoritative operational destination for all public inquiries.

---

## End of Extension

**Document:** iDigitalRoot Public Website — Lead / Inquiry Extension  
**Version:** 1.1  
**Status:** FINAL EXTENSION  
**Next authoritative design stage:** iDigitalRoot Admin & Operations Dashboard — Full Product & Technical Blueprint
