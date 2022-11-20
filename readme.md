# SecureX Workflows and Tutos

This repository intends to gather some SecureX tutorials that help on Workflow and Integration Modules creation.

## Start Your SecureX tenant - some "mandatory steps"

Here are the steps for starting your SecureX tenant with a minimum of useful services :

* Step 1 : Create your SecureX Account [sign up to SecureX](https://security.cisco.com/).


* Step 2 : Integrate your Cisco Security Solution (Umbrella or Secure Endpoint or another one)
* Step 3 : Activate Useful/relevant free integrations [Adding 10 Free Threat Intelligence Sources to SecureX in Under 3 Minutes!](https://www.youtube.com/watch?v=7nCRMHo4_9Q&list=PLmuBTVjNfV0dlZ_DYgNiZ7SBlWVB0ae33&index=6)
* Step 3 : Customize your dashboards
* Step 3 : Activate Orchestration. Click on the **orchestration** table and the click on the **start orchestration** button that is displayed in the middle of the screen.  Orchestration becomes available a few hours after.
* Step 4 : In Orchestration : Create a SecureX_Token. It will be the most effecient way to use SecureX native Target ( [See instructions](https://ciscosecurity.github.io/sxo-05-security-workflows/account-keys/securex-token) )
* Step 5 : Create an Alert / Info Webex Team Room . Webex Team is naturally a very good user interface for SecureX ([ See Instructions ](https://github.com/pcardotatgit/Create_a_Webex_Team_Bot))
* Step 6a : Customize the **Webex Teams - Post Message to Room** atomic workflow
* Step 6b : Or learn about how to create from scratch a **send message to webex team** workflow ( [ See Instructions ](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/1-Create_a_Webex_Team_Bot_Target))
* Step 7 : Import useful/relevant SecureX Workflows from the workflow lists

At this point You are ready to use SecureX services and Create New Service which doesn't exist.

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

## Use Cases

In this section you will find some use cases documented step by step. The goal is not workflows themselves but the goal is to show how to create them.

That means that in a lot of cases I show some stuff that are maybe not the best practices but that are interesting specific aspects to see and know about.

* [ Send a webex alert if temperature in Paris is less than 25° ](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/9-JSON_Parsing_within_SecureX)
* [ Secure End Point detect and alert - which host are infected by this malware ](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/8-detect_and_alert_workflow_lab)
* [Dashboard and tiles for current temperature in Paris](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/6-relay_modules_for_tiles)
* [Create Public Feeds in SecureX for Cisco Secure Firewalls ( SI, CTID, Network Objects, Dynamic Objects )](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/12-create_securex_blocking_lists_for_firewalls)
* [Query SecureX for dispositions of observables in security logs](https://github.com/pcardotatgit/check_observable_dispositions_in_CTR_from_an_observable_list)

## Securex Workflow List from Cisco and others

* [SecureX Workflows List](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/99-SecureX_Workflow_list) ( updated Nov 18 2022 )

## My Workflows in this github repo

* [My Workflows](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/500-SecureX_Workflow_examples)

## Check your workflows or do some reverse engineering on others workflows

I wrote the tool below because needed to quickly check and clean my workflows and document them. Whatis better than a visualization tool for this ?

* [SecureX JSON workflow parser](https://github.com/pcardotatgit/SecureX_Workflow_JSON_Tree_viewer)
* [SecureX Workflow Analyser](https://ciscosecurity.github.io/sxo-05-security-workflows/analyzer)