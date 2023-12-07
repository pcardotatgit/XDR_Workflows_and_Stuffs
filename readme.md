# XDR Tutorials

This repository intends to gather some XDR/SecureX tutorials that help on Workflow and Integration Modules creation.
As the Threat Response part within XDR is an evolution of SecureX, almost all the content here still valid for both platforms even if some articles were created for SecureX.

## Start Your tenant - some "recommended or mandatory steps"

Here are some minimum steps to go thru in order to start your XDR tenant. :

* Step 1 : Start your XDR tenant. Follow the instruction that had been mailed to you when it was spinned up. Regarding SecureX, it is not anymore possible to create a SecureX Tenant. What currently happens is that SecureX owners are switching to XDR.

* Step 2 : Integrate your Cisco Security Solution (Umbrella or Secure Endpoint or any other one). If you don't have any Cisco product to integrate, then it is worthit to ask for a Secure Endpoint evaluation and an Umbrella evaluation. These 2 solutions are awesome solution to use to quickly dig into XDR advanced knowledge thru realistic Attack Scenarios
* Step 3 : Activate Useful/relevant free integrations. Have a look to [Adding 10 Free Threat Intelligence Sources to SecureX in Under 3 Minutes!](https://www.youtube.com/watch?v=7nCRMHo4_9Q&list=PLmuBTVjNfV0dlZ_DYgNiZ7SBlWVB0ae33&index=6). These integrations are really not mandatory. But they are nice to have.
* Step 4 : Create and Customize your dashboards. Select tiles that are relevant for you. Gather them into one single vue that help you to go fast in the understanding of the situatuion.
* Step 5 : Check that **XDR Orchestration** Services are available. Click on the **automation** selection in the left menu panel and check that you can see the default workflow library.
* Step 6 : In Orchestration : Create a **SecureX_Token**. It will be the most efficient way to use SecureX native Target ( [See instructions](https://ciscosecurity.github.io/sxo-05-security-workflows/account-keys/securex-token) ). **Notice** : not anymore needed since December 8 2022 thanks to the new **SecureX APIs** target which manages it's own token. This action is normaly not needed for XDR but it can help for compatibility of workflows that had been created in SecureX.
* Step 7 : Create an Alert / Info Webex Room . Webex is naturally an very good user interface for XDR. And for the same reason create a Webex bot is highly recommended. A lot of Security Automation use case can be based on Webex Bots. ([ See Instructions here ](https://github.com/pcardotatgit/Create_a_Webex_Team_Bot))
* Step 8a : Then you can Customize the **Webex Teams - Post Message to Room** atomic workflow which is "ready" to send Alert Messages to yout Webex Alert Room. Make this one work
* Step 8b : OR for pedagogical reasons, then learn about how to create from scratch a **send message to webex team** workflow ( [ See Instructions ](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/1-Create_a_Webex_Team_Bot_Target))
* Step 9 : In **orchestration** check that you can import workflows from the Cisco Git Repositories for atomic actions and workflows 
* Step 10 : Import useful/relevant XDR/SecureX Workflows from the workflow lists ( [See an Example](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/blob/master/100-SecureX_automation_lab/importing_workflows.md)  )

At this point You are ready to use XDR services.

## SecureX Token 

This section is not needed for XDR. But it will help some old workflows written for SecureX to work within XDR without re writing them.

**Since December 2022 SecureX Token is not anymore needed**. But still, it can be used. So I document it in this tutorial just for keeping knowledge and history of it.

SecureX exposes a lot of APIs for a lot of purposes. From this point of vue SecureX can become a powerful solution to integrate within a SOC. 

This means that SecureX exposes a few "system targets" like CTR_Target, CTIA_Target, or Private_CTIA_Target. Which all require authentication when we interact with them. Then for all of these "SecureX Targets", we are supposed to ask for authentication tokens, we have to manage Token expiration and renewal.

These token management operations are absolutely mandatory and heavy in terms of extra activities within SecureX Workflows.

The **SecureX Token** makes authentication to these SecureX system targets very easy. 

When we use these targets, we just have to use the **SecureX Token** as the account key for all of them. And that's it !. Then Token Generation and renewal is automatically managed.

Creating a SecureX Token was one of the installation mandatory steps until December 2022.

[SecureX Token instructions are here](https://ciscosecurity.github.io/sxo-05-security-workflows/account-keys/securex-token)

**December 8 2022 - Secure Token Update** : A new SecureX native Target named **SecureX APIs** had been released. This one can be use in place of legacy "system targets" : CTR_Target, CTIA_Target, or Private_CTIA_Target. One of the main benefits of this new target it that is manages the Authenthication token, we don't have to take care of it..

The benefits of this is then, We don't have to take care anymore of the authentication token for **SecureX targets**. We just have to use the targets into our workflows.

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
* 3 - [ Send a webex alert if temperature in Paris is less than 25° ](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/9-JSON_Parsing_within_SecureX)
* 4 - [ Secure End Point detect and alert - which host are infected by this malware ](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/8-detect_and_alert_workflow_lab)
* 5 - [Dashboard and tiles for current temperature in Paris](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/6-relay_modules_for_tiles)
* 6 - Manage SecureX Blocking Lists ( SecureX Feeds )
    * 6a - [Create Public Feeds in XDR for Cisco Secure Firewalls ( SI, CTID, Network Objects, Dynamic Objects )](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/12-create_securex_blocking_lists_for_firewalls) workflow
    * 6b - [Manage Threate Response Authentication token requests](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/500-SecureX_Workflow_examples/Atomics/CTR_Generate_Access_Token) workflow
    * 6c - [Get all judgments in private intell filtered by source](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/500-SecureX_Workflow_examples/Workflows/get_all_judgments_in_private_intell_filtered_by_source) workflow
    * 6d - [Add_an_Observable_into_Judgments_and_feeds](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/500-SecureX_Workflow_examples/Atomics/Add_an_Observable_into_Judgments_and_feeds) workflow
    * 6e - [Update judgments in private intell](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/500-SecureX_Workflow_examples/Workflows/update_judgments_in_private_intell) workflow
    * 6f - [ Create an XDR IP blocking list from TOR entry / exit IP address Blocking List](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/500-SecureX_Workflow_examples/Workflows/TOR_IP_blocking_list_to_SecureX_feeds) : the final workflow
    * 6g - [ The full python version of the all above workflows](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/13-Interact_with_CTIM/judgments)
* 7 - [Query XDR for dispositions of observables in security logs](https://github.com/pcardotatgit/check_observable_dispositions_in_CTR_from_an_observable_list)
* 8 - [ Detect Threat and send an alert into Webex, then from webex alert add bad IPs into XDR Firewall Blocking feeds ](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/100-SecureX_automation_lab)

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