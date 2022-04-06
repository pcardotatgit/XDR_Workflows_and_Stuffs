# Create a Webex Team Bot

Base on the instruction bellow, create a Webex Team Bot, Create an alert webex team room and test it.

Click on the link Bellow :

[Create a Webex Team Bot instructions ](https://github.com/pcardotatgit/Create_a_Webex_Team_Bot)

For our needs, we don't have to take care about the BOT logic. We are only interested by the Webex Team Bot itself as a Webex entity that has the capability to send Webex messages thanks to a never expire Webex Token.

And we need a webex Team Room to send alert messages into it on behalf of our bot.

Go to SecureX and create a Target for your Webex Team Bot. Once done create a basic SecureX workflow that will take as an input any string and will send it to your Alert Webex Team Room created above. Make it atomic.

Click on the link Bellow :

[ Create the Webex Team Target and Send to Webex Team atomic workflow ](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/1-Create_a_Webex_Team_Bot_Target)

**OK DONE !**

# NEXT STEP : Interact with Cisco Threat Response

In our workflow, we will interact with SecureX Threat Response for requesting some security services.  Actually we are going to use the **inpect** Threat response API that is a magic API that extract from any row text content ( security logs, blog posts ) all the observable it contains and their types.

In our example we will use it only to check if the type of the observable passed to the workflow is a sha256 or not. For doing this, we need to interact with Threat Response.

Let's have a look now to how we will interact with Threat Response

[ Ask to Threat Reponse for an Authentication Token instructions ](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/7-ask_for_a_threat_response_token)