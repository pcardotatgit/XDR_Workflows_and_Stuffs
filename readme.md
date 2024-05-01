# XDR Tutorials

This repository intends to gather some XDR/SecureX tutorials which could help to better understand Workflow and Integration Modules creation.
A lot of the article here was written in the context of SecureX. And as the Threat Response and workflows part within XDR are just evolutions what was existing in SecureX, then all the SecureX content here is still valid for XDR platform.

SecureX and XDR GUIs are different but features and access to these features are the same.

## Start Your tenant - some "recommended or mandatory steps"

Here are some minimum steps to go thru in order to start correctly your XDR tenant. :

* **Step 1** : Start your XDR tenant. Follow the instruction that had been mailed to you when it was spinned up. Regarding SecureX, it is not anymore possible to create a SecureX Tenant. What currently happens is that SecureX owners are switching to XDR.

* **Step 2** : Integrate your Cisco Security Solutions (Umbrella or Secure Endpoint and any other one). If you don't have any Cisco product to integrate, then it is worthit to ask for both a Secure Endpoint and an Umbrella evaluation. The Evaluation Requests are easy to find thru google. These 2 solutions are awesome solutions to use to quickly dig into XDR advanced knowledge. Secure Endpoint natively create Incidents within XDR and tons of attack scenarios are easy to setup. Umbrella allows us to setup very easily nice realistic Attack Scenarios which can be used to create detect/alert/block automation use case.
* **Step 3** : Activate Useful/relevant free integrations. Have a look to [Adding 10 Free Threat Intelligence Sources to SecureX in Under 3 Minutes!](https://www.youtube.com/watch?v=7nCRMHo4_9Q&list=PLmuBTVjNfV0dlZ_DYgNiZ7SBlWVB0ae33&index=6). These integrations are really not mandatory. But they are nice to have.
* **Step 4 :** Create and Customize your dashboards. Select tiles that are relevant for you. Gather them into one single vue that help you to go fast in the understanding of the situatuion.
* **Step 5 :** Check that **XDR Orchestration** Services are available. Click on the **automation** selection in the left menu panel and check that you can see the default workflow library.
* **Step 6 :** In **Orchestration** (SecureX) or **Automate** ( XDR ) : Create a **Cisco XDR Token** for XDR ( or a **SecureX_Token** for SecureX). It will be an efficient way to manage Authentication Toekn for XDR native Targets ( Threat Response, Public and private Intell,... ) ( [See instructions](https://docs.xdr.security.cisco.com/Content/Automate/account-keys-cisco-xdr-token.htm) ). **Notice** : **This Token** is not anymore needed since December 2022 thanks to the new **XDR API** targets which manages the CTR token. So **Cisco XDR Token** is normaly not needed for XDR for any new workflow you create from scratch. But still it will help old workflows that had been created for SecureX, to work in XDR.
* **Step 7 :** Create an Alert / Info Webex Room. Webex is natively a very good user interface for XDR. And for the same reason create a Webex bot is highly recommended. A lot of Security Automation use case can be based on this Webex Bots. ([ See Instructions here ](https://github.com/pcardotatgit/Create_a_Webex_Team_Bot))
* **Step 8a** : Then you can Customize the **Webex Teams - Post Message to Room** atomic workflow which is "ready" to send Alert Messages to yout Webex Alert Room. Make this one work. Run it , send a text message and use your webex alert roomid and token. Check that you receive this message into the alert webex room
* **Step 8b** : OR just for reason of learning how to do, then learn about how to create from scratch a **send message to webex team** workflow ( [ See Instructions ](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/1-Create_a_Webex_Team_Bot_Target)).
* **Step 9** : In **Orchestration** (SecureX) or **Automate** ( XDR ), click on the **[Import Workflow]** button. Check that you can import workflows from the : **CiscoSecurity_Atomics** and **CiscoSecurity_Workflows** **Git Repositories**. 
* **Step 10** : Import useful/relevant XDR/SecureX Workflows from the workflow lists ( [See an Example](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/blob/master/100-SecureX_automation_lab/importing_workflows.md)  )

At this point You are ready to use XDR services.

## Cisco XDR Token 

This section is not needed for XDR. But .

In theory, **Since December 2022 the XDR Token is not anymore needed**. 

But it can still be used. It can be used for some old workflows written for SecureX to work within XDR. And Avoid re writing them.

XDR exposes a lot of APIs for a lot of purposes. From this point of vue XDR becomes a powerful Threat Hunting solution to integrate within a SOC. It exposes a lot of Security Services that can be easily used.

XDR exposes a few "system targets" like Platform APIs, Conure APIs Automation APIs, Private Intelligence API and Public API. Which all require authentication when we interact with them. Then for all of these "XDR Targets", we are supposed to ask for authentication tokens, and we have to manage Token expiration and renewal.

These token management operations are absolutely mandatory and are heavy in terms of extra activities within XDR Workflows.

The **Cisco XDR Token** makes authentication to these XDR system targets very easy. 

When we use these targets, we just have to use the **Cisco XDR Token** as the account key for all of them. And that's it !. Then Token Generation and renewal is automatically managed by XDR.

**A few word about history of this Token :**

Creating an XDR / SecureX Token was one of the installation mandatory steps until December 2022. It was named at that time **SecureX Token**.

[SecureX Token instructions are here](https://ciscosecurity.github.io/sxo-05-security-workflows/account-keys/securex-token)

**December 8 2022 - Secure Token Update** : A new SecureX native Target named **SecureX APIs** had been released. This one can be use in place of legacy "system targets" : CTR_Target, CTIA_Target, or Private_CTIA_Target. 

These targets are now within XDR Platform APIs, Conure APIs Automation APIs, Private Intelligence API and Public API.

One of the main benefits of this new target it that is manages the Authenthication token, we don't have to take care of it..

The benefits of this is then, We don't have to take care anymore of the authentication token for **XDR/SecureX targets**. We just have to use the targets into our workflows. and the authentication is automatically managed for us.

## Targets

In this section you will find some information about how to create XDR Targets objects.

**Notice** : a lot of these targets already exist within XDR. Meaning that normally you don't have to create them. But it is worthit to recreate them from scratch. It helps to understand in depth targets creation

These examples below cover differents Targets scenarios that will be common in production environments. And the goal is to show how we can create them step by step.

* [Create step by step a Webex Bot Target - example of HTTP bearer token target ](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/1-Create_a_Webex_Team_Bot_Target)
* [Create step by step a Networking Device target - example of SSH target](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/2-Create_a_Networking_Device_Target)
* [Create step by step a FTD Device target - example of Basic + Bearer token authentication (  Oauth )](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/3-Create_a_onbox_Managed_FTD_Target)
* [Create step by step a Secure Endpoint Target - example of HTTP Basic authentication Target ](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/4-Create_an_AMP_Target)
* [Threat Response Target - an example of Oauth target ( basic + Bearer token )](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/7-ask_for_a_threat_response_token)

## Triggers

In this section you will find some tutorials dedicated to triggers which can Start SecureX workflows.

* [Trigger your workflows from the pivot menu ( SecureX only )](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/5-Trigger_your_workflow_from_the_ribbon)
* [Trigger your workflows from Webhooks](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/10-trigger_your_workflow_with_webhooks)

## Miscelaneous 

In this section some usefull tutorials.

* [JSON Parsing ( Thru workflow and thru python )](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/9-JSON_Parsing_within_SecureX)

## Use Cases for learning about Orchestration

In this section you will find some use cases documented step by step. The goal is not workflows themselves but the goal is to show how to create them.

That means that in a lot of cases I show some stuff that are maybe not the best practices but which are specific aspects interesting to see and know about.

The recommendation here is to do all the exercices here under one after the other in the proposed order.

* 1 - [ Create a Webex bot ](https://github.com/pcardotatgit/Create_a_Webex_Team_Bot)
* 2 - [ Create the Webex Target and Send messages to an alert Webex Room ](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/1-Create_a_Webex_Team_Bot_Target)
* 3 - [ Send a webex alert if temperature in Paris is less than 25° ](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/9-JSON_Parsing_within_SecureX) ( workflow )
* 4 - [ Secure End Point detect and alert - which host are infected by this malware ](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/8-detect_and_alert_workflow_lab) ( workflow )
* 5 - [Dashboard and tiles for current temperature in Paris](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/6-relay_modules_for_tiles)
* 6 - Manage XDR Blocking Lists ( XDR Feeds )
    * 6a - [Create Public Feeds in XDR for Cisco Secure Firewalls ( SI, CTID, Network Objects, Dynamic Objects )](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/12-create_securex_blocking_lists_for_firewalls)( workflow )
    * 6b - [Manage Threat Response Authentication token requests](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/500-SecureX_Workflow_examples/Atomics/CTR_Generate_Access_Token) ( workflow )
    * 6c - [Get all judgments in private intell filtered by source](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/500-SecureX_Workflow_examples/Workflows/get_all_judgments_in_private_intell_filtered_by_source) ( workflow )
    * 6d - [Add_an_Observable_into_Judgments_and_feeds](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/500-SecureX_Workflow_examples/Atomics/Add_an_Observable_into_Judgments_and_feeds) ( workflow )
    * 6e - [Update judgments in private intell](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/500-SecureX_Workflow_examples/Workflows/update_judgments_in_private_intell) ( workflow )
    * 6f - [ Create an XDR IP blocking list from TOR entry / exit IP address Blocking List](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/500-SecureX_Workflow_examples/Workflows/TOR_IP_blocking_list_to_SecureX_feeds) : ( workflow )
    * 6g - [ The full python version of the all above workflows](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/13-Interact_with_CTIM/judgments) ( python )
* 7 - [Query XDR for dispositions of observables in security logs](https://github.com/pcardotatgit/check_observable_dispositions_in_CTR_from_an_observable_list) ( python )
* 8 - SecureX Demo - [ Detect Threat and send an alert into Webex, then from webex alert add bad IPs into XDR Firewall Blocking feeds ](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/100-SecureX_automation_lab)
* 8a - XDR Demo - [ Detect Threat and send an alert into Webex, then from webex alert add bad IPs into XDR Firewall Blocking feeds ](https://github.com/pcardotatgit/webex_for_xdr_part-7_The_final_demo)
* 9 - [Create an XDR Incident with python](https://github.com/pcardotatgit/XDR_create_incident_with_python) ( python )
* 10a - [Delete XDR Demo Incidents and every attached objects](https://github.com/pcardotatgit/clean_XDR_Incidents) ( python )
* 10b - [Delete XDR Incidents based on selected Incident ](https://github.com/pcardotatgit/clean_XDR_Incidents_based_on_selected_Incident) ( python )
* 11 - [add an object to XDR feed thanks to python](https://github.com/pcardotatgit/Add_Object_To_XDR_Feed) ( python )
* 12 - [Create an XDR Incident from Attack Detection into apache logs](https://github.com/pcardotatgit/XDR_demo_-_create_incident_from_apache_log_threat_analysis) ( python )
* 13 - [ Ransomware Detection and Incident Creation within XDR](https://github.com/pcardotatgit/Ransomware_real_time_detector) ( python )

## XDR/Securex Workflow List from Cisco and others

* [XDR Workflows List](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/99-SecureX_Workflow_list) ( updated May 7 2023 )

## My Workflows in this github repo

* [My Workflows](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/500-SecureX_Workflow_examples)

## Check your workflows or do some reverse engineering on others workflows

I wrote the tool below because I needed to quickly check some of my workflows, for cleaning them and document them. What is better than a visualization tool for this ?

* [XDR workflow JSON parser](https://github.com/pcardotatgit/SecureX_Workflow_JSON_Tree_viewer)
* [Workflow Analyser](https://ciscosecurity.github.io/sxo-05-security-workflows/analyzer)

## Cisco Threat Intelligence Model ( CTIM )

XDR APIs allow anyone to interact with XDR Threat Hunting services. This is what makes XDR a very powerful solution to have into any SOC. 

- To learn more about **Cisco Threat Intell Model** secrets you can to go to the following [ DEVNET Learning Lab ](https://developer.cisco.com/learning/modules/security-securex-threat-response/), which will help you to understand the details of how the CTIM APÏs can be used into your Threat Hunting Activities.
- And you will naturally want to intensively use CTIM APIs. Then the [ CTIM API documentation here ](https://github.com/threatgrid/ctim/blob/master/doc/tutorials/modeling-threat-intel-ctim.md) will be very usefull for you.

The [ Detect Threat and send an alert into Webex, then from webex alert add bad IPs into XDR Firewall Blocking feeds ](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/100-SecureX_automation_lab) lab gives an example of direct interaction with CTIM for creating Sigthings and Incidents within SecureX.

## 3rd Party Integration Development

This specific topic is the most passioning SecureX topic. But this is the more complex topic for Security Automation Designers.

This topic shows the power of the XDR Platform.

For integrating an IT solution within XDR you need to develop what we call a Relay Module. A Relay Module is basically a REST Web Server that will receive REST call from XDR and that will translate and relay these calls to the 3rd party solution.  This Relay Module will have to receive replies from the 3rd party solution and will have to translate them into valid SecureX JSON answers.

This component can be developed in any programming language that is able to expose APIs to secureX and that is able to interact with 3rd party solution.

This component must be hosted into a platform that is reachable by SecureX on the INTERNET in one hand and by the 3rd party solution in the other hand. 

This component can be deployed into physical servers into a DMZ or into any public cloud.

Python and javascript are the most obvious languages to use, but if you prefer PHP, Ruby, Go.... it's up to you.

If you are new to this topic and you want to go to it, here are some reccomendations.

* 1 - You must be confortable with python
* 2 - You must know about python flask
* 3 - Optionnal but reccommended you have to be familiar with AWS serverless, or azure 

Here is a basic example of 3rd party integration :

- [Relay Module for tiles lab](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/6-relay_modules_for_tiles)

We created some dedicated DEVNET learning labs :

- [SecureX Integrations](https://developer.cisco.com/learning/modules/security-securex-integrations/)
- [SecureX Serverless Relay Modules](https://developer.cisco.com/learning/modules/securex-serverless-relay-modules/)

We have more advanced content on this part ( workshop and code ) on this part. Dedicated to teams who will actively develop XDR Integratations for production.

- For those who know me, I will be happy to share this content with you. Ping me 