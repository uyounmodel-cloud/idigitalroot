# iDigitalRoot Cross-Platform Admin Control, Localization & Rich Media Extension v1.0

**Status:** FINAL EXTENSION  
**Date:** September 2026  
**Applies to:**

- `iDigitalRoot_Public_Website_Product_Technical_Blueprint_v1.0_Candidate`
- `iDigitalRoot_Public_Website_Lead_Inquiry_Extension_v1.1`
- `iDigitalRoot_Client_Account_Dashboard_Final_Technical_Blueprint_v1.0`
- `iDigitalRoot_Admin_Operations_Dashboard_Final_Technical_Blueprint_v1.0`

---

# 0. Purpose

This extension synchronizes the previously approved blueprints with the final Admin Dashboard requirements.

It does not replace the source blueprints. It supersedes only the specific constraints described below.

---

# 1. Unlimited Language Administration

Previous references to Arabic and English as initial first-class languages remain valid for launch, but the architecture is now explicitly frozen as:

> **Admin-managed unlimited locale support.**

Authorized staff may add, activate, translate and publish additional locales such as French without an application-code redesign.

Each locale stores:

- language/locale code;
- display/native name;
- LTR/RTL direction;
- fallback locale;
- enabled surfaces;
- country/date/number/currency formatting configuration where applicable;
- status.

The same locale registry is shared logically by Public Website, Inquiry Wizard and Client Account.

---

# 2. Public Website Localization Amendment

The public website must allow Admin to manage per-language:

- page title/content;
- slugs;
- navigation;
- CTA text;
- service content;
- Website Blueprint content;
- pricing copy;
- articles/research/news;
- FAQs;
- media alt/caption;
- SEO metadata;
- structured public content where supported;
- legal pages.

Translation is implemented through localized fields/records rather than duplicated hard-coded websites.

A page may be published in one locale while another locale remains Draft, but Admin must clearly see translation completeness.

---

# 3. Client Account Localization Amendment

The Client Account v1.0 remains a separate application from client Website CMSs.

However, the following Client Account content becomes Admin-localizable:

- navigation labels;
- explanatory/help content;
- static headings;
- empty-state copy;
- service descriptions;
- support/request labels;
- billing/renewal help copy;
- onboarding help copy;
- project-stage display names;
- campaign/Hero content;
- notification templates;
- email templates;
- security guidance copy where safe.

Business logic, permissions, secure errors and system behavior remain code-controlled even when their display strings are translated.

---

# 4. Inquiry Wizard Localization Amendment

The Lead/Inquiry Extension v1.1 remains authoritative regarding no self-signup.

The wizard is now manageable in any enabled locale.

Admin can translate:

- wizard title;
- introduction;
- step labels;
- question labels;
- help text;
- options;
- validation display messages;
- consent copy;
- review labels;
- confirmation content.

Each Lead continues to store the locale and wizard-version used during submission.

---

# 5. Translation Workflow

Each localized item supports states:

```text
MISSING
DRAFT
NEEDS REVIEW
READY
PUBLISHED
OUTDATED
ARCHIVED
```

When source content changes, related translations can be marked `OUTDATED`.

Admin translation workspace must support:

- source/target side by side;
- RTL/LTR editor mode;
- field-level status;
- locale preview;
- version history;
- per-locale publish;
- fallback behavior;
- missing-translation filters.

No AI/machine translation is required. Future machine translation is an optional Provider Integration only.

---

# 6. Public Website Full HTML Editor Amendment

The public website CMS now explicitly requires:

- rich text/WYSIWYG editor;
- source HTML editor;
- approved content-section builder;
- trusted embed block for permissioned users.

This is **content HTML**, not application/source-code editing.

Server-side HTML sanitization is mandatory.

Default blocked items include scripts, unsafe event handlers, `javascript:` URLs and unapproved executable/embed elements.

---

# 7. Rich Media / External Media Amendment

Public website media must support both local and approved external sources.

Required source classes:

- local image/document upload;
- YouTube URL/embed;
- Google Drive public/shared file preview/link;
- Vimeo or comparable approved provider;
- generic approved iframe/oEmbed-style provider;
- future provider integrations.

For common providers, Admin should paste a normal public URL and the CMS should create the correct responsive embed automatically.

Generic embed HTML is available only to authorized roles and is sanitized/allowlisted.

No external-media password is collected.

Private provider API/OAuth access is a future Integration and requires security/cost review.

---

# 8. Embed Security

Embed providers must be registered in Admin with:

- provider name;
- allowed hostname(s);
- URL patterns;
- allowed iframe attributes;
- sandbox policy;
- referrer policy;
- autoplay policy;
- privacy-enhanced mode where available;
- active status.

Content Security Policy must align with approved embed domains.

Arbitrary external JavaScript is not accepted as normal CMS content.

---

# 9. Admin Publishing / Versioning Extension

The same content-governance model applies to:

- public pages;
- articles;
- wizard definitions;
- localized strings/content;
- campaigns;
- service descriptions.

Supported states where relevant:

- Draft;
- Needs Review;
- Scheduled;
- Published;
- Unpublished;
- Archived.

Important content supports version history and rollback.

---

# 10. Admin Permissions Extension

The Admin permission system must distinguish at least:

```text
locales.read
locales.manage
translations.read
translations.edit
translations.publish
public_html.edit
public_html.trusted_embed
media.upload
media.import_external
media.manage_embed_providers
inquiry_wizard.edit
inquiry_wizard.publish
client_ui_content.edit
client_ui_content.publish
```

No content capability implies permission to manage code, secrets or production infrastructure.

---

# 11. Final Supersession Rules

This extension supersedes any narrower reading that:

- only Arabic and English can exist;
- adding French requires duplicating pages or rebuilding the application;
- Client Account UI text must be hard-coded;
- public inquiry labels are fixed in code;
- public media is limited to local uploads;
- public editors cannot use controlled source HTML;
- YouTube/Google Drive/approved external embeds require manual source-code deployment.

It does **not** supersede:

- the separation between Client Account and each client Website CMS;
- the no-public-self-signup rule;
- the prohibition on AI chatbot/API dependency in current Client/Inquiry v1;
- the security, tenant-isolation, SSO and audit requirements already approved.

---

# 12. Definition of Done

This extension is satisfied when:

- Admin can add French or another locale without changing application architecture;
- Admin can designate RTL/LTR per locale;
- public website content can be translated/published independently by locale;
- Client Account Admin-managed copy can be translated;
- Inquiry Wizard questions/options can be translated/versioned;
- public CMS offers WYSIWYG + source HTML editing under sanitization;
- YouTube embeds work from public URLs;
- permitted Google Drive shared media/document references work without credentials;
- generic external embeds are allowlisted and sandboxed;
- all new actions are role/permission controlled and audited.

**END OF EXTENSION**
