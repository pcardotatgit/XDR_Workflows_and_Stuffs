---
title: SSH_to_ASA_and_do_show_interfaces
purpose: Proof of concept of interaction with a network device
integrated products: Cisco ASA or Cisco Switches or Cisco IOS devices
---

# SSH_to_ASA_and_do_show_interfaces


This workflow opens an SSH administration session with an ASA ( that is accessible thru INTERNET ) execute a show interface command and store the result into a JSON data

This workflow is a proof of concept

---

## Change Log

| Date | Notes |
|:-----|:------|
| October 13, 2022 | - Initial release |

---

## Requirements

This workflow requires that the managed ASA ( or switch ) to be reachable by SecureX on the INTERNET. Meaning that you must expose the device's administration interface on the INTERNET thanks to port forwarding into INTERNET firewall.

## Input Variables

No input variable for this workflow

---
## Global Variables

No Global Variables used by this workflow
---
## Output Variables

| Variable Name | Type | Details | Note |
|:------------|:-----|:--------|:-----------|
| **W_INTERFACE_JSON_LIST** | String JSON | Interface list with relevant details| This variable is supposed to be assign to another SecureX variable by next activities |
---

## Workflow Steps
1. Open an SSH connection to the ASA ( or switch )
2. Parse the show interface result and store text chunk that are the interfaces details
3. Create a JSON text result with all interfaces and their details
---

## Installation and Configuration
* Import the workflow
* Modify the device IP address in the **Cisco_ASA** target
* Modify **Device_Credential** account keys
* Modify the prompt in the **Cisco_ASA** target which is set to **ciscoasa>**. Replace by your device prompt
* Modify the which is set to **ciscoasa#** in the **Execute Terminal Command(s)** Activity and the **Cisco_ASA** target. Replace them by your device prompt.

---

## Targets


| Target Name | Type | Details | Account Keys | Notes |
|:------------|:-----|:--------|:-------------|:------|
| Cisco_ASA | terminal . endpoint | _Protocol:_ `SSH`<br />_Host/IP Address:_ `an INTERNET IP Address` | Device_Credential | |

---

## Account Keys

| Account Key Name | Type | Details | Notes |
|:-----------------|:-----|:--------|:------|
| Device_Credential | username / password | _Username_: <br />_Password_:<br />_Enable_Password_: | |

## Integrated Products

* Cisco ASA or Cisco Switchs or Cisco IOS devices