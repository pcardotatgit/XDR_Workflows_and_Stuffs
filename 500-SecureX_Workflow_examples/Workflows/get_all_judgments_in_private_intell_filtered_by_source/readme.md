---
layout: page
title: GET ALL JUDGMENTS IN PRIVATE INTELL FILTERED BY SOURCE v2
permalink: /workflows/PRODUCT-NAME/0xxx-WORKFLOW-NAME
redirect_from:
  - /workflows/0xxx
parent: PRODUCT NAME
grand_parent: Workflows
---

# GET ALL JUDGMENTS IN PRIVATE INTELL FILTERED BY SOURCE v2


Get all judgements values and Judgement IDs in the private intel from a specific source.
Purposes :
- Delete all Judgement from a specific source
- Create a list of all judgments from a specific source

---

## Change Log

| Date | Notes |
|:-----|:------|
| November 20, 2022 | - Initial release |

---

## Requirements
* The following [CTRGenerateAccessToken_TEXT](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/500-SecureX_Workflow_examples/Atomics/CTR_Generate_Access_Token) Workflow is used by this workflow.You must import it first.
* The [targets](#targets) and [account keys](#account-keys) 

---

## Workflow Steps

1. Step 1 When the workflow start it expect a string as a optionnal input. Thisstring input is supposed to match to a **source** in the private intelligence judgments and will be used as a filter. In order output all data stored into the Judgment, set this input to an empty value.
2. Step 2 - The workflows asks for a Token To SecureX CTR and store the result in a global Temp Variable named : **CTR_TOKEN_IN_GLOBALS**. This variable will be passed to a python activity after.
3. Step 3 - a python activity is runt to query SecureX Judgment. It uses as a input the CTR TOKEN and the source filter. The result will be 2 lists. One contains only Judgment IDs and it is stored into a global variable named  **Judgment IDs to delete**. The other one contains IP addresses plus judgment IDs and is set to the **output** type in order to be assigned to another variable into a workflow.
4. End of the workflow


---

## Configuration
* Set the `ADMIN_CTR_Credentials` with valid CTR Admin username and password.

---

## Targets
Target Group: `Default TargetGroup`

| Target Name | Type | Details | Account Keys | Notes |
|:------------|:-----|:--------|:-------------|:------|
| SecureX Private Intell jUdgments | target in python script | _Protocol:_ `HTTPS`<br />_Host:_ `private.intel.eu.amp.cisco.com`<br>`private.intel.apjc.amp.cisco.com`<br>`private.intel.us.amp.cisco.com`<br>_Path:_ `/ctia/judgement/search`<br /> | **ADMIN_CTR_Credentials** | Target in python Activity |

---

## Account Keys

| Account Key Name | Type | Details | Notes |
|:-----------------|:-----|:--------|:------|
| **ADMIN_CTR_Credentials** | HTTP Basic Authentication | _Username:_ CTR_Client ID<br />_Password:_ CTR_Client Secret | |