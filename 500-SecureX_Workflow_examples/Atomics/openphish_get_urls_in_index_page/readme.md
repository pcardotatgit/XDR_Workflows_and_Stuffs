---
title: OPENPHISH_GET_URLs_IN_INDEX
purpose: Get disposition of an observable
Integrated products: SecureX Threat Response ( TALOS and Integrated Threat Intell )
---

# OPENPHISH_GET_URLs_IN_INDEX


This workflow opens the openphish.com index page  and extract all URLs and brands index page and store the resulting list into a global variable named openphish_url_list. The final goal will be to send it judgment thru another workflow

---

## Change Log

| Date | Notes |
|:-----|:------|
| October 15, 2022 | - Initial release |

_See the [Important Notes](/sxo-05-security-workflows/notes) page for more information about updating workflows_

---

## Requirements

This workflow doesn't need any specific requirements

## Input Variables

| Variable Name | Type | Details | Required |
|:------------|:-----|:--------|:-----------|
| **Monitored_brand** | String | default value is : **-all-**<br />this a keyword for filtering specific brand. Which could be useful for brand watch uses cases  | True |

---
## Global Variables

| Variable Name | Type | Details | Required |
|:------------|:-----|:--------|:-----------|
| **openphish_url_list** | String | Store the result of the operation. To be share with other worflow  | True |
---

## Workflow Steps
1. open the openphish.com index page
2. Parses the HTML result and keep urls and associated brands 
3. Update the **openphish_url_list** global variable
4. End of the workflow

---

## Installation and Configuration
* No specific intrusction for this workflow
* Import it and run it

---

## Targets
Target Group: `Default TargetGroup`

| Target Name | Type | Details | Account Keys | Notes |
|:------------|:-----|:--------|:-------------|:------|
| **PAT_openphish_index_page** | HTTP Endpoint | _Protocol:_ `HTTPS`<br />_Host:_ `openphish.com`<br />_Path:_  | No Authentication | |

---

## Account Keys

No account key needed

## Integrated Products

* Securex Private Intelligence
* Openphish Threat Intelligence