# Introduction

The goal of this lab is to share with participants every details about how to build an automated threat detection and mitigation scenario.

This scenario is a complete **SecureX XDR demonstration**

## Automated threat detection and mitigation scenario

This automated threat hunting scenario is the following :

Imagine vulnerable a Web server that exposes the log4J vulnerability. This vulnerability open the door to RCE ( remote code execution ) attacks.  

Meaning that an hacker connected to web page of this vulnerable web server, that present a formular,  can use one of the edit field of the formular in order to trigger execution of shell code on server's operating system.

Even if the web server is equiped by an Endpoint Protection solution, this RCE vulnerability can't be detected by it as it is due to unsecured coding of the web page which allow this attack.

![](/assets/img/lab_network.png)

So We start with the situation where hacker have a potential remote administration acces to a victim web server.

In this lab, the web server is a windows machine that run apache web server and very vulnerable php scripts and which exposes the log4j vulnerability. But the web server is protected by Secure Endpoint.

- Step 1 : the hacker send a log4j Attack into a web server formular. This attack make the Web server to download from a malicious location a piece of code that will be executed by it's windows operating system. This code is a powershell code that runs into memory a "mimikatz" attack.
- Step 2 : Secure Endpoint will detect this attack attempt and will block it. At the same time, Secure Endpoint will create a SecureX Incident.
- Step 3 : Within SecureX a workflow runs every 5 minutes and reads SecureX incidents. For every new incidents since last 5 minutes, the worklow will analyses their details and will extract from them  targets and malicious observable information. 
- Step 4 : for every severe incidents, the workflow send to Security Operators alert Webex team room, a documented alert that warn them about this new threat, with the list of targets and malicious observable that try to pawn them.
- Step 5 : Thanks to clickable links into the webex team Alert message, the security operator can trigger SecureX workflows which add malicious observables into SecureX blocking feeds.
- Step 6 - Final step, once malicious observable are in the blocking feeds, they are automatically deployed a few minutes later as new blocking rules into all company firewalls.

## What will you learn in this lab

In this lab you will learn 

- How to create Incidents and Sightings into SecureX
- How to create feeds
- How to create judgments for observables and how to add them into SecureX Feeds
- How to Read Incident and Sigthings
- How to parse them into SecureX workflow
- How to send markdown formatted message to webex team room and how to use Webex Team as a User Interface for SecureX
- How to trigger a webhook and how to send data to a workflow from a script
 

## Lab components

In this lab you need the following components :

- A laptop with a python ( 3.7 + ) interperter installed into it
- The Lab simulator
- A SecureX tenant
- SecureX Threat Response API credentials
- A Webex Team Room that will be used a an Alert Webex Room
- A Webex Team bot that will be used to send alert into the Webex Team Room

## Preparation Steps

### Demo Part 1 - Threat Detection & Create Incident 

1. Check your SecureX tenant. If you don't have a SecureX tenant you can use DCLOUD **Cisco SecureX Orchestration v1 - Instant Demo** 
2. Create Threat Response API client with all scopes. Copy **client ID** and **Client Password** and save them somewhere.
3. Install the Lab Simulator into you laptop . [see Instructions]
4. Open the **config.py** script located into the simlator root directory. Update the **ctr_client_id** and **ctr_client_password** variables with  CTR client ID and Client Password you got in step 2. 
5. Depending on your region uncomment the **host=xxx** and **host_for_token=xxx** variables. **Notice** DCLOUD demos are located in the US.
5. Start the simulator and open your browser to **http://localhost:4000**
5. Check between the Lab Simulator and your SecureX tenant. Click on the **check SecureX** link. 
8. At this point you can run the half of the full demo ( Detection and Alert )

Infection scenario :

Open your browser to  **http://localhost:4000** and click on the hacker.  This opens an hacker console that is supposed to be used to send some shell commands to the victim.


### Demo Part 2 - Send Alert into Webex Team Room and add Malicious observables into SecureX blocking feeds

1. Create a dedicated webex Team Bot for this lab. Copy and save it's authentication token
2. Edit the **config.py** script and update the **webex_bot_token** variable value
3. Create an Alert Webex Team Room and check that you can send messages into it from SecureX workflows. Copy it's Room ID
4. Edit the **config.py** script and update the **webex_room_id** variable value
5. Create a SecureX target for Webex [ see instructions ]
6. Go to Orchestration and import the **Receive observables from a rest client**
7. Customize the Target of this workflow
8. In SecureX Orchestration go to the admin panel and then select Create a webhook **Events & Webhook** then create an event  named **PVT_Demo_Webhook** and create within it a webhook named **Webhook_trigger** copy it's **webhook url**
9. Edit the **Receive observables from a rest client** workflow and assign to it the webhook you created above in the trigger section of the workflow properties panel on the right
8. edit the **config.py** file and update the **SecureX_Webhook_url** variable
9. Test this setup with the **z_test_webhook.py** file. When you run this script you are supposed to see a message into your webex team room.
![](assets/img/2.png)

10. If you received the success message you are goo to move forward. Of not check here [troubleshooting instructions]
11. Go to Orchestration and import the **Check Incidents every 5 minutes**
12. Check the SecureX **Private_CTIA_Target** . This one must use a host fqdn that match to your region ( ex : **private.intel.eu.amp.cisco.com** ) and this target must use the **SecureX_Token** you created at the begining of this lab.
13. Run the **Check Incidents every 5 minutes** workflow. You will be asked to enter the **webex_bot_token** and the **webex_room_id**.

For the purpose of this lab we dont store the **webex_bot_token** and **webex_room_id** variables into global SecureX Variables. We voluntary let the workflow asking you these value is required inputs.  For production you will have to modify this part a create static variables into your secureX tenant.

The expected result is a formatted alert message into the alert webex team room 

![](assets/img/1.png)

**CONGRATULATION !! you are ready for the last part of this lab**

You have probably noticed that IP addresses observables in the webex team alert message are clickables.  The purpose of this is to allow security operators to add malicious observables into SecureX blocking Feeds. And once any observable is into such SecureX Feeds, it can be automatically consumed by firewalls and converted into a blocking security rule.

This is the goal of this last part of the lab.

- Step 1 - Create SecureX Feeds
- Step 2 - import the workflow that add an observable into SecureX Feeds.

