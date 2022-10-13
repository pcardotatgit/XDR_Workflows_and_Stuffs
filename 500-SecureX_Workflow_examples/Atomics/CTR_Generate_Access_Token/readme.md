---
layout: page
title: CTRGenerateAccessToken_TEXT
permalink: /workflows/PRODUCT-NAME/0xxx-TRGenerateAccessToken_TEXT
redirect_from:
  - /workflows/0xxx
parent: PRODUCT NAME
grand_parent: Workflows
---

# CTRGenerateAccessToken_TEXT
<div markdown="1">
Workflow #0xxx
{: .label }
</div>

This workflow Asks for an Access Token to SecureX Threat Response and store it into a global variable named **CTR_TOKEN_IN_GLOBALS**.

This variable can then be used by other workflows that could run at the same time

This is an alternative to the **SecureX Token** account key, that is need when we want to pass the CTR Token to a Python script for example. Or to learn about how to deal with OAuth within SecureX


---

## Change Log

| Date | Notes |
|:-----|:------|
| july 21, 2022 | - Initial release |

_See the [Important Notes](/sxo-05-security-workflows/notes) page for more information about updating workflows_

---

## Requirements

* The [targets](#targets) and [account keys](#account-keys) listed at the bottom of the page

---

## Workflow Steps

1. The Workflow Queries SecureX Threat Response Target for an Access Token :
1. Parse the JSON result and extract the authentication token from it
1. Stores the Token into the **CTR_TOKEN_IN_GLOBALS** global variable
---

## Configuration

* Check that your **CTR_For_Access_Token** target use the correct url for your region ( visibility.amp.cisco.com , visibility.eu.amp.cisco.com )
* Create an Account Key ( PAT_CTR_Credentials ) for this target Basic Authentication with the client_ID and client_password that you previously created in the SecureX > Administration > API Client

The Account Key is named PAT_CTR_Credentials in order to clearly differentiate it from the CTR_Credentials Account Key that might already exists in the Tenant. No conflict will happen but you might have duplicate names into the Account key list

---

## Targets
Target Group: `Default TargetGroup`

| Target Name | Type | Details | Account Keys | Notes |
|:------------|:-----|:--------|:-------------|:------|
| CTR_For_Access_Token | HTTP Endpoint | _Protocol:_ `HTTPS`<br />_Host:_ `visibility.eu.amp.cisco.com`<br />_Path:_ `/iroh` | PAT_CTR_Credentials | |

---

## Account Keys

| Account Key Name | Type | Details | Notes |
|:-----------------|:-----|:--------|:------|
| PAT_CTR_Credentials | HTTP Basic Authentication | _Username:_ Client ID<br />_Password:_ Client Secret | |



