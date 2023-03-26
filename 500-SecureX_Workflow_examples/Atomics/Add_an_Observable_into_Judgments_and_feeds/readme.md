# Add_an_Observable_into_Judgments_and_feeds workflow

This workflow adds an observable into one of the SecureX Private Intelligence feeds, created by the [Create Text Public Feeds for firewalls](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/12-create_securex_blocking_lists_for_firewalls) workflow.

First the obervable is added by the workflow into the SecureX private intelligence judgments, with it's **type**, it's **value**, it's **disposition** and a **source**. 

The workflow links the observable **type** to a SecureX **indicator** which is linked to a specific **feed** for the type. 

Thanks to this, when the workflow adds an observable to the Judgments, then it is automatically added to the corresponding SecureX feed. And then it can be automatically consumed by the company firewalls.

---

## Change Log

| Date | Notes |
|:-----|:------|
| Month Day, Year | - Initial release |

---

## Requirements
* The following [system atomics](/sxo-05-security-workflows/atomics/system) are used by this workflow:
	* Threat Response - Generate Access Token
	* Threat Response - Create Relationship
---

## Workflow Steps
1. The workflow begins with converting the observable type into an indicator type. And check if the observable is a supported observable type.
2. Then it convert the disposition into it's numerical value
3. The next step is to query Threat Response in order to get indicator names and IDs.
4. Then it check if an indicator name exist for the indicator type. And it keep the indicator ID.
5. Then the workflow create a private intell judgement for the observable
6. And the last step is to create a relationship for the created judgement and the corresponding indicators.
---

## Configuration
* Set the `MY_CTIA_Private_Intelligence` target to the correct host value depending on your region

---

## Targets
Target Group: `Default TargetGroup`

| Target Name | Type | Details | Account Keys | Notes |
|:------------|:-----|:--------|:-------------|:------|
| MY_CTIA_Private_Intelligence | HTTP Endpoint | _Protocol:_ `HTTPS`<br />_Host:_ `private.intel.eu.amp.cisco.com`<br />`private.intel.amp.cisco.com`<br />`private.intel.apjc.amp.cisco.com`<br />_Path:_ `/ctia` | SecureX Token | |

---

## Account Keys

| Account Key Name | Type | Details | Notes |
|:-----------------|:-----|:--------|:------|
| SecureX Token | automatically defined | no need to be defined | |