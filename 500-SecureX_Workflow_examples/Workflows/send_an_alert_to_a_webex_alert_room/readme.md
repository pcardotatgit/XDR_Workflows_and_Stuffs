---
title: XDR_ALERT_CARD_WITH_TARGETS_AND_OBSERVABLES_TO_WEBEX_ROOM
purpose: Proof of concept of interaction with a network device
integrated products: Webex
---

# XDR_ALERT_CARD_WITH_TARGETS_AND_OBSERVABLES_TO_WEBEX_ROOM

The goal of this workflow is to make XDR able to send an alert into an Alert Bot Room.

The alert is actually a Webex Adaptative card which is an interactive formular. 

The bot logic is not managed by XDR but XDR send into it an alert message which allow Security Operators to be aware of a Security issue and make them able to take isolation and blocking actions.

This workflow expect as inputs a target list, an observable list and an alert description.

Target and observable list must be into the following format :

    target-1
    target-2
    ....
    ....
    target-n
    
One single object per line. 

That means that any parsing and formating operation must have been done before to pass inputs to the workflow

---

## Change Log

| Date | Notes |
|:-----|:------|
| December 7, 2023 | - Initial release |

---

## Requirements

This workflow requires that an alert Webex bot with a room to interact with, had been setup

## Input Variables

- target_list ( text variable with one observable per line )
- observable_list ( text variable with one observable per line )
- alert_description : A long text description of the alert

Default values are provided

---
## Global Variables

- XDR_ALERT_BOT_ROOM_ID : string : The Alert Bot Room ID 
- XDR_ALERT_BOT_TOKEN : secure_string :  The Alert Bot Room TOKEN
---
## Output Variables

No output variables

---

## Workflow Steps
1. The workflow reads the **target_list, observable_list and alert_description**
2. It creates the Webex Adaptative Card JSON payload ( the alert card )
3. It sends the alert cards JSON payload as attachment to the Alert Bot Room
---

## Installation and Configuration

* Import the workflow
* Assign correct values to the XDR_ALERT_BOT_ROOM_ID and XDR_ALERT_BOT_TOKEN
* You can run the workflow

---

## Targets


| Target Name | Type | Details | Account Keys | Notes |
|:------------|:-----|:--------|:-------------|:------|
| Webex XDR_ALERT_BOT_ROOM_ID | HTTP Endpoint | Managed by atomic subworkflow | | declared as a global variable |

---

## Account Keys

| Account Key Name | Type | Details | Notes |
|:-----------------|:-----|:--------|:------|
| XDR_ALERT_BOT_TOKEN | TOKEN | | declared as a global variable |

## Integrated Products

* Webex

# Where to go Next

Go to the next section 

The all in one Use case 

UNDER CONSTRUCTION

Go back to the previous section 

[webex_for_xdr_part-5_websocket](https://github.com/pcardotatgit/webex_for_xdr_part-5_websocket)