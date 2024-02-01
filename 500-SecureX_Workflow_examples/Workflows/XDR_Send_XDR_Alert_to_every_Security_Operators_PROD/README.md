---
title: Send_XDR_Alert_to_every_Security_Operators_PROD
integrated products: Webex
---

# Send_XDR_Alert_to_every_Security_Operators_PROD

The goal of this workflow is to make XDR able to send alerts to security operators

Instead of sending the alert into an Alert Webex Room ( like we do in the [webex_for_xdr_part-6_XDR_send_alert_workflow](https://github.com/pcardotatgit/webex_for_xdr_part-6_XDR_send_alert_workflow) project ), this workflow send the alert to every Webex Users ( Security Operators ) that openned a conversation with the XDR Alert Bot.

One benefits of this method is that we don't need to indicated to the workflow the room ID of the webex alert Room. The workflow is able to identify every Webex Room the Bot is registered to. Then the alert will be sent to every of these rooms.

Security Operators who want to receive alerts from the bot must be webex users and they just have to open  a conversation with the XDR alert bot ( contact it and says hello ).

The alert is actually a Webex Adaptative card which is an interactive formular. 

The bot logic is not managed by XDR. We are supposed to create this bot logic ( see [webex_for_xdr_part-5_websocket](https://github.com/pcardotatgit/webex_for_xdr_part-5_websocket) )

Thanks to this workflow XDR is able to send to every Security Operators an alert formular whoch containsthe alert description, a list of the target with the capability to select some target and isolate them, and select malicious observables and block them.

This workflow expects as inputs a target list, an observable list and an alert description.

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
| February 1 , 2024 | - Initial release |
---

## Requirements

This workflow requires that an alert Webex bot with a room to interact with, had been setup

Instructions for creating a Webex Bot for XDR Alert can be found [here](https://github.com/pcardotatgit/Create_a_Webex_bot_for_XDR_Alerts)

## Input Variables

- target_list ( text variable with one observable per line )
- observable_list ( text variable with one observable per line )
- alert_description : A text description of the alert

Default values are provided for every of these input variables.

---
## Global Variables

- XDR_ALERT_BOT_TOKEN : secure_string :  The Alert Bot Room TOKEN
---
## Output Variables

No output variables

---

## Workflow Steps
1. The workflow reads the **target_list, observable_list and alert_description**
2. It creates the Webex Adaptative Card JSON payload ( the alert card )
3. It retreives the webex room id of every conversation openned by a security operator with the alert bot
3. It sends the alert cards JSON payload as attachment to every Rooms
---

## Installation and Configuration

* Import the **Send_XDR_Alert_to_every_Security_Operators_PROD.json** workflow into your XDR tenant
* Assign correct values to the **XDR_ALERT_BOT_TOKEN** and **XDR_ALERT_BOT_TOKEN_CLEAR** (**Notice** due to some mysterious reasons the python activity cannot be created with the **Secured String** version of the token variable... I will fix that later...)
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
| XDR_ALERT_BOT_TOKEN_CLEAR | TOKEN | | declared as a global variable |

(**Notice** due to some mysterious reasons the python activity cannot be created with the **Secured String** version of the token variable... I will fix that later...)

## Integrated Products

* Webex

# Related emos

The following Use case use this workflow 

[Webex for XDR demo part 7 - the final demo](https://github.com/pcardotatgit/webex_for_xdr_part-7_The_final_demo)
