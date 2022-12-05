# Trigger your SecureX Workflows thanks to webhooks

Webhooks are very common and handy. SecureX Workflows can be easily triggered by webhooks. And we can pass data to the workflow thru the webhook.

Webhook trigger configuration is very well explained at this location :

[SecureX Webhooks ](https://ciscosecurity.github.io/sxo-05-security-workflows/webhooks)

In a few words , here is what you must do :

- At the bottom of the Orchestration Left menu select **Events & Webhooks**.
- Click on the **Webhook** Tab. Create a New Webhook, give it a meaningful name, a description and select the content-type. - Click on the **Submit** button . And then a **Webhook ID**, an **AO API Key** and a **Webhook URL** will be automatically generated. **Copy** the **Webhook URL** ! you will need it later.
- Then click on the **Events** tab, create a new event, give it a title, the **Select type** must be **Webhook Event**. Select the webhook you just created.
- Then go to all workflows you want trigger with this webhooks
- On the right workflow properties  panel scroll down to the **trigger** section and **Add** the new event.
- Done.

The script named **send_webhook_to_secureX.py** gives you an example of python script which triggers a SecureX workflow and which pass data to the workflow within the POST call.

Before runing it you must update within it the variable named : **url** at the top of the script.

You must paste between the quotes the **Webhook URL**.

## Important Notices

If you exceed the maximum number of allowed Webhooks per minutes ( 5 max ) or per days ( 5000 ) then your trigger will fail with an error code equal to 429 or 415.

You can pass data to the workflow thru the body POST call, in text or JSON format.  Content-type becomes important for this.

The size of the data you send must be less than 1 Mb.

In the workflow you can retreive the sent data in the **Variable Browser** thru the **Trigger => The trigger Name => Output => Request Body**.

You will have to parse the result !

We have an alternative to webhooks for triggering a workflow. Response Workflows can be triggered thanks to their APIs. This is described in another article.