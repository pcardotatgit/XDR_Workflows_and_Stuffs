# SecureX Workflows and Tutos

This repository intends to gather some SecureX tutorials that help on Workflow and Integration Modules creation.

## Start Your SecureX tenant - some "mandatory steps"

Here are the minimum steps to go thru in order to start your SecureX tenant. And be ready to use SecureX Advanced Services :

* Step 1 : Create your SecureX Account [sign up to SecureX](https://security.cisco.com/).

* Step 2 : Integrate your Cisco Security Solution (Umbrella or Secure Endpoint or any other one). Several videos are available on Youtube. And We published online SecureX Trainings at [Learnsecurex](https://learnsecurex.cisco.com/ ) which show that.
* Step 3 : Activate Useful/relevant free integrations. Have a look to [Adding 10 Free Threat Intelligence Sources to SecureX in Under 3 Minutes!](https://www.youtube.com/watch?v=7nCRMHo4_9Q&list=PLmuBTVjNfV0dlZ_DYgNiZ7SBlWVB0ae33&index=6). These integrations increase SecureX Enrichment accuracy.
* Step 4 : Customize your dashboards. Select, gather tiles that are relevant for you.
* Step 5 : Activate **Orchestration** Services. Click on the **orchestration** table and the click on the **start orchestration** button that is displayed in the middle of the screen.  Orchestration becomes available a few hours after.
* Step 6 : In Orchestration : Create a **SecureX_Token**. It will be the most effecient way to use SecureX native Target ( [See instructions](https://ciscosecurity.github.io/sxo-05-security-workflows/account-keys/securex-token) ). **Notice** : not anymore needed since December 8 2022 thanks to the new **SecureX APIs** target which manages it's own token. 
* Step 7 : Create an Alert / Info Webex Team Room . Webex Team is naturally a very good user interface for SecureX. And create a webex team bot as well which is the only way to create a permanent Webec Token. ([ See Instructions here ](https://github.com/pcardotatgit/Create_a_Webex_Team_Bot))
* Step 8a : Then you can Customize the **Webex Teams - Post Message to Room** atomic workflow wich is "ready" to send Alert Messages to yout Webex Alert Room.
* Step 8b : OR for pedagogical reasons, then learn about how to create from scratch a **send message to webex team** workflow ( [ See Instructions ](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/1-Create_a_Webex_Team_Bot_Target))
* Step 9 : Import useful/relevant SecureX Workflows from the workflow lists

At this point You are ready to use SecureX services and Create New Service which doesn't exist.

## SecureX Token

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

In this section you will find some information about how to create SecureX Targets.

**Notice** : a lot of these targets already exist within SecureX. Meaning you don't have to create them.

These examples below cover differents Targets scenarios that will be common in production environments. And the goal is to show how we can create them step by step.

* [Create step by step a Webex Team Bot Target - example of HTTP bearer token target ](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/1-Create_a_Webex_Team_Bot_Target)
* [Create step by step a Networking Device target - example of SSH target](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/2-Create_a_Networking_Device_Target)
* [Create step by step a FTD Device target - example of Basic + Bearer token authentication (  Oauth )](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/3-Create_a_onbox_Managed_FTD_Target)
* [Create step by step a Secure Endpoint Target - example of HTTP Basic authentication Target ](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/4-Create_an_AMP_Target)
* [Threat Response Target - an example of Oauth target ( basic + Bearer token )](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/7-ask_for_a_threat_response_token)

## Triggers

In this section you will find some tutorials dedicated to triggers which can Start SecureX workflows.

* [Trigger your workflows from the pivot menu](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/5-Trigger_your_workflow_from_the_ribbon)
* [Trigger your workflows from Webhooks](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/10-trigger_your_workflow_with_webhooks)

## Miscelaneous 

In this section some usefull tutorials.

* [JSON Parsing ( secureX and python )](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/9-JSON_Parsing_within_SecureX)

## Use Cases for learning about SecureX Orchestration

In this section you will find some use cases documented step by step. The goal is not workflows themselves but the goal is to show how to create them.

That means that in a lot of cases I show some stuff that are maybe not the best practices but which are specific aspects interesting to see and know about.

* [ Create a webex team bot ](https://github.com/pcardotatgit/Create_a_Webex_Team_Bot)
* [ Create the SecureX Webex Team Target and Send messages to an alert Webex Team Room ](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/1-Create_a_Webex_Team_Bot_Target)
* [ Send a webex alert if temperature in Paris is less than 25° ](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/9-JSON_Parsing_within_SecureX)
* [ Secure End Point detect and alert - which host are infected by this malware ](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/8-detect_and_alert_workflow_lab)
* [Dashboard and tiles for current temperature in Paris](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/6-relay_modules_for_tiles)
* [Create Public Feeds in SecureX for Cisco Secure Firewalls ( SI, CTID, Network Objects, Dynamic Objects )](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/12-create_securex_blocking_lists_for_firewalls)
* [Query SecureX for dispositions of observables in security logs](https://github.com/pcardotatgit/check_observable_dispositions_in_CTR_from_an_observable_list)
* [ Detect Threat and send an alert into webex Team, then from webex alert add bad IPs into SecureX Firewall Blocking feeds ](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/100-SecureX_automation_lab)

## Securex Workflow List from Cisco and others

* [SecureX Workflows List](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/99-SecureX_Workflow_list) ( updated Nov 18 2022 )

## My Workflows in this github repo

* [My Workflows](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/500-SecureX_Workflow_examples)

## Check your workflows or do some reverse engineering on others workflows

I wrote the tool below because needed to quickly check and clean my workflows and document them. Whatis better than a visualization tool for this ?

* [SecureX JSON workflow parser](https://github.com/pcardotatgit/SecureX_Workflow_JSON_Tree_viewer)
* [SecureX Workflow Analyser](https://ciscosecurity.github.io/sxo-05-security-workflows/analyzer)

## 3rd Party Integration Development

This specific topic is the most passioning SecureX topic. But this is the more complex topic for Security Automation Designers.

This topic shows the power of the SecureX Platform.

For integrating an IT solution within SecureX you need to develop what we call a Relay Module. A Relay Module is basically a REST Web Server that will receive REST call from SecureX and that will translate and relay these calls to the 3rd party solution.  This Relay Module will have to receive replies from the 3rd party solution and will have to translate them into valid SecureX JSON answers.

This component can be developed in any programming language that is able to expose APIs to secureX and that is able to interact with 3rd party solution.

This component must be hosted into a platform that is reachable by SecureX on the INTERNET in one hand and by the 3rd party solution in the other hand. 

This component can be deployed into physical servers into a DMZ or into any public cloud.

Python and javascript are the most obvious languages to use, but if you prefer PHP, Ruby, Go.... it's up to you.

If you are new to this topic and you want to go to it, here are some reccomendations.

* 1 - You must be confortable with python
* 2 - You must know about python flask
* 3 - Optionnal but reccommended you have to be familiar with AWS serverless, or azure 

Here is a basic example of 3rd party integration :

[Relay Module for tiles lab](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/6-relay_modules_for_tiles)

