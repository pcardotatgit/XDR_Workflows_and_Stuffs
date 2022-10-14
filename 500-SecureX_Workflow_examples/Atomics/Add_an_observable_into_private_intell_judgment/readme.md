---
title: Add Observable into Judgments and feeds
purpose: Create Judgements feeds and Blocking Lists for firewalls
Integrated products: SecureX Private Intelligence
---

# Add an Observable into Judgments and feeds

This workflow creates  a judgement entry for an observable into the SecureX Private Intelligence. Once a judgement is created, the observable appears automatically within a public feed which Secure Firewall can polls for blocking malicious observables. Supported observables types are : domain, ip, ipv6, sha256, url

Note: Workflow **0015A-SecureFirewall-BlockObservable-setup** must be executed first in order to create the required indicators and feeds in SecureX. See the documentation for more information.

**Notice :** This workflow is a modification of the **0015B-SecureFirewall-BlockObservable** Cisco validated workflow. This workflow manages **source** and **disposition** for the observable to be ingested into Judgments.

Target Group: Default TargetGroup
Targets: CTR_For_Access_Token, Private_CTIA_Target

Please see: 

https://ciscosecurity.github.io/sxo-05-security-workflows/workflows/0015A
https://ciscosecurity.github.io/sxo-05-security-workflows/workflows/0015B

---

## Change Log

| Date | Notes |
|:-----|:------|
| October 13, 2022 | - Initial release |

_See the [Important Notes](/sxo-05-security-workflows/notes) page for more information about updating workflows_

---

## Requirements

This workflow needs the following subworkflows :

Atomic Workflows :

- Threat Response - Generate Access Token
- Threat Response - Create Relationship
--- 
## Input Variables 


| Variable Name | Type | Details | Required |
|:------------|:-----|:--------|:-----------|
| observable_type | String | type of the variable to ingest into Private judgments | True |
| observable_value | String | The value of the observable pivoted on | True |
| disposition | String | Disposition of the observable ( unknown / common / suspicious / malicious / clean ) | True |
| source | String | The source from where this observable was collected | True |

---
## Global Variables

No Global Variables used by this workflow

---

## Workflow Steps

1. This workflow expects as Inputs : **observable_type**, **observable_value**, **disposition** and **source**
2. Convert observable_type to indicator type and check that observable type supported
3. Determine disposition integer value base on disposition input
4. Ask for an Threat Response SecureX Token
5. Search for matching indicator
6. If Search was successful then go to next step. Else STOP
7. Extract indicator ID
8. Generate judgment JSON data
9. Create the new entry into Private Intelligence Judgement
10. If operation 9 was Not succesful then STOP. Else go top next step
11. Extract new judgment ID and create relationship
12. End of workflow

---

## Installation and Configuration

- Indicators and feed must already exist. You must have runt the **0015A-SecureFirewall-BlockObservable-setup** workflow first.

- Except CTIA account keys nothing specicific is required for this workflow

**Notice :** This workflow doesn't use the new **SecureX Token** account key. It uses the old token request method.

---

## Targets

This workflow doesn't use specific targets, but the subworkflows this workflow use, use targets.

Target Group: `Default TargetGroup`

| Target Name | Type | Details | Account Keys | Notes |
|:------------|:-----|:--------|:-------------|:------|
| **Private_CTIA_Target** | HTTP Endpoint |  _Protocol:_ `HTTPS`<br />_Host:_ `private.intel.eu.amp.cisco.com`<br />`private.intel.amp.cisco.com`<br />`private.intel.apjc.amp.cisco.com`<br />_Path:_  | No | |
|**AMP_Target**|HTTP Endpoint |  _Protocol:_ `HTTPS`<br />_Host:_ `api.eu.amp.cisco.com`<br />`api.amp.cisco.com`<br />`api.apjc.amp.cisco.com`<br />_Path:_ `/v1`|AMP_Credentials||

---

## Account Keys

This workflow 

| Account Key Name | Type | Details | Notes |
|:-----------------|:-----|:----------|:----|
| **AMP_Credentials** | HTTP Basic Authentication |_Username:_ Client ID<br />_Password:_ Client Secret  | |
---
## Integrated Products

* Securex Private Intelligence
