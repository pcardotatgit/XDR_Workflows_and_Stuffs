# Webex Team Alert Message

The goal of this section is to share more details about how to create nice alert messages into Webex Team. And How to manage user interactivity with Webex messages.

Actually there are two ways for creating messages.

- Markdown messages
- Webex Team Cards

Both allow us to include clickable links into the messages displayed to people who will receive them.

Webex Team Cards are much more nice than markdown messages. They are more close to Web GUI than Markdown messages. But they require an operationnal bot logic attached to the webex bot in order to be fully functionnal.

In our use case as we just want to trigger a workflow thanks to a webhook, and pass some data ( ip address, Webex Bot Token, Room ID ) to it, then markdown are enough for this and it will be easier to set up. 

In XDR/SecureX, workflow can handle only data that are passed thru a POST method in the webhook call, and not thru GET. 

A direct consequence of this is that in the Webex Alert Message, regarding clickable URL links, we can't build them with a concatenation of webhook_url and data to pass to the workflow. Because http calls sent from webex messages  are only GET calls and not POST calls.

For this reason we must use a bot logic underneath the Webex Team messages. A bot logic to which we can send the GET calls from the the clickable links in the Webex Alert message. And then ask to this bot logic to forward the calls to XDR/SecureX, as a POST call.

This is a perfect job for the lab simulator which is a flask application. It can exposes APIs endpoints for receiving call from the Webex Message in one hand, and send POST calls to XDR/SecureX in the other hand. This is exactly what we need in our use case.

![](assets/img/12.png)

This part is handled by the **@app.route('/block',methods=['GET'])** route in the **app.py** script.

## Webex Team Markdown

Markdown messages are basic in terms of format. And they are limited in term of markdown tags. 

You can see what are the available tags by clicking on the markdown icon available int the webex team GUI

![](assets/img/13.png)

The only interactivity capability is an url link we can insert into the message thanks to the approriate markdown tag.

All this is enough to acheive our goal. We actually don't need more. Another big benefit of markdown is that the bot logic we need underneath can be very basic a very fast to write. Which is not the case for Webex Team Cards.

It is very simple to create a Webex Team Markdown message.

Open the **u3_send_alert_to_webex_room.py** script and have a look at it. 

The alert is contained into the **message_out** string variable. This variable can be a mix of static string and dynamic string.

This **message_out** variable content has to be assigned to the **markdown key** that is sent to Webex Team POST API endpoint whic send the message.

And that's it.  

The message is easy to create within a python script but very easy to create as within a Secure Workflow.

Have a look to the Webex Post Message activities of the **Receive observables from a rest client** workflow.

## Webex Team Cards

Webex Team Cards are much more nice than markdown message. They act exactly like Web Pages and actually behave the same.

They offer the capability to create web formulars with complexe behaviors. With colorisation, images, select boxes, check boxes and other nice components dedicated to interactivity with users.

![](assets/img/14.png)

Interactive Webex Team cards are very powerful, but they require "complex" bot logic needed to handle actions and selections user does in the formular.

Once again, our simulator is a perfect place to put this "complex" bot logic. And to keep the lab simple I decided to not handle this part.

Here are some awesome resources for working with Webex Team Cards :

- [Webex Team Card Designer ](https://developer.webex.com/buttons-and-cards-designer)
- [PyAdaptiveCards](https://developer.cisco.com/codeexchange/github/repo/CiscoSE/pyadaptivecards)

The Webex Team Card Designer is an online tool you can use to create your own Webex team card. The result is a JSON payload you have to pass into the **attachments** key within the POST REST call you send to Webex.

## Learn more about Webex Team Cards

Go to this link [ under construction ] if you want more information about how to work with Webex Team Cards.