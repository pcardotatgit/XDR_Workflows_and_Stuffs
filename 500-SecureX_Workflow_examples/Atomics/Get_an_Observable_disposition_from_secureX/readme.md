---
layout: page
title: CTR GET OBSERVABLE DISPOSITION GENERIC v2
permalink: /workflows/PRODUCT-NAME/0xxx-WORKFLOW-NAME
redirect_from:
  - /workflows/0xxx
parent: PRODUCT NAME
grand_parent: Workflows
---

# CTR GET OBSERVABLE DISPOSITION GENERIC v2

This workflow gets observable verdicts from every modules but keep the highest risk disposition value instead of the lowest. In the following order ( Malicious or Suspicious or Clean ). 
Meaning that the observable is already known by Cisco Security Backends and TALOS already has a verdict.
And if TALOS doesn't know the observable, then this one will have the Unknow status

---

## Change Log

| Date | Notes |
|:-----|:------|
| October 12, 2022 | - Initial release |

_See the [Important Notes](/sxo-05-security-workflows/notes) page for more information about updating workflows_

---

## Requirements

This workflow has not specific requirements
---
## Input Variables

| Variable Name | Type | Details | Required |
|:------------|:-----|:--------|:-----------|
| observable_type | String | type of the variable to ingest into Private judgments | True |
| observable_value | String | The value of the observable pivoted on | True |

---
## Global Variables

This workflow doesn't use any global variables

---
## Output Variables

| Variable Name | Type | Details | 
|:------------|:-----|:--------|
| OUTPUT_DISPOSITION | String | Final Disposition to pass to next activity |  |
---

## Workflow Steps
1. Query Threat Response with observable details into the body of a POSTE request
2. Check if at least one verdict is Malicious
3. Set Output disposition to the determined value

---

## Configuration

* Import the workflow
* If not already done Create the SecureX token ( CTR_SecureX_Token )
- Create the CTIA_Public_Intelligence target or check that is uses the correct URL for your region

---

## Targets
Target Group: `Default TargetGroup`

| Target Name | Type | Details | Account Keys | Notes |
|:------------|:-----|:--------|:-------------|:------|
| PAT_CTIA_Public_Intelligence | HTTP Endpoint | _Protocol:_ `HTTPS`<br />_Host:_ `visibility.eu.amp.cisco.com`<br />`visibility.amp.cisco.com`<br />`visibility.zpjc.amp.cisco.com`<br />_Path:_ `/iroh` | CTR_SecureX_Token | |

---

## Account Keys

| Account Key Name | Type | Details | Notes |
|:-----------------|:-----|:--------|:------|
| CTR_SecureX_Token | SecureX Token |  | Give to it the name you want|

## Integrated Products

* Securex Public Intelligence ( Aka TALOS )