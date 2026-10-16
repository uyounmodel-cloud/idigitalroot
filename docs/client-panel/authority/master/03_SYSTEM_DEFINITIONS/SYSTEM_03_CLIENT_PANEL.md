# System 03 — Personal Client Panel / Client Account

## Phase

Phase 3, after Admin & Operations has been built and Phase 1 is closed.

## Existing authority

The foundational document `iDigitalRoot_Client_Account_Dashboard_Final_Technical_Blueprint_v1.0.docx` is included and must be read before implementation.

## Product definition

The Client Panel is the customer-facing operating center for the client's relationship with iDigitalRoot and all owned Digital Roots. It is not a website builder, server panel, generic analytics product, AI chatbot or copy of the website CMS.

## Key customer questions

- What websites/services do I have?
- Does anything require my attention?
- What is happening with a website being built?
- How do I open a live website’s CMS?
- What renews next and what is due?
- How do I approve/reject a project stage or request changes?
- How do I request support/major work/new services?

## Main modules

- Home command center / Needs Your Attention;
- My Websites portfolio;
- selected website details;
- New Website onboarding;
- Website Blueprint questionnaire engine;
- project timeline/status;
- protected previews;
- approvals and revision requests;
- launch readiness/history;
- Open Website Admin SSO;
- client profile/security;
- domains;
- professional email services;
- services/subscriptions/renewals;
- social profile links;
- Root Health summarized managed-service state;
- requests/support;
- billing/invoices/payments where contractually approved;
- notifications and targeted Hero campaigns managed by Admin.

## Data separation

Client-account relationship data stays in iDigitalRoot platform domains. Normal website content, media, website users/products/posts remain in each website CMS.

## SSO requirement

Open Website Admin must use a signed/tamper-evident, single-use, very short-lived, audience-bound ticket tied to one client user + one website + minimal scope + nonce. Replay, expiry, wrong audience, wrong website or altered ticket must fail closed.
