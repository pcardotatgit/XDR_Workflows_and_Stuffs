# Webex Team Alert Message

The goal of this section is to share more details about how to create nice alert messages into Webex Team. And How to manage user interactivity with Webex messages.

Actually there are two ways for creating messages.

- Markdown messages
- Webex Team Cards

Both allow us to include clickable links into the messages displayed to people who will read them.

But Webex Team Cards are much more nice than markdown messages. They are more close to Web GUI than Markdown messages.

In our use case as we want to trigger a SecureX workflow with a webhook. And we want to pass data ( ip address, Webex Bot Token, Room ID ). There is an impact on the way to handle the user click actions.

Within SecureX, the workflow will handle only data that will be passed by a POST operation, and not a GET. 

A direct consequence of this is that we can't put the webhook_url + data in the URL into URL links into the Webex Message. Because Webex http call when click on links are only GET calls and not POST.

For this reason we must use a bot logic underneath the Webex Team messages. A bot logic where to send the GET calls from the Alert. And ask to this bot logic to send to SecureX the Webhook + data thru POST calls.

This is a perfect job for the lab simulator which is a flask application which exposes APIs endpoint in one hand and send REST calls in the other hand. This is exactly what we do in this use case.

![](assets/img/12.png)

This part is handled by the **@app.route('/block',methods=['GET'])** route in the **app.py** script.

## Webex Team Markdown

Markdown messages are basic in terms of format. And they are limited in term of markdown tags. 

You can see what are the available tags by clicking on the markdown icon available int the webex team GUI

![](assets/img/13.png)

The only interactivity capability is an url link we can insert into the message thanks to the approriate markdown tag.

All this is enough to acheive our goal. We actually don't need more. Another big benefit of markdown is that the bot logic we need underneath can be very basic a very fast to write. Which is not the case for Webex Team Cards.

This is because of this only reason that I decided to use it in this use case.

It is very simple to create a Webex Team Markdown message.

Open the **u3_send_alert_to_webex_room.py** script and have a look at it. 

The alert is contained into the **message_out** string variable. This variable can be a mix of static string and dynamic string.

This **message_out** variable is just assigned to the **markdown** key sent to Webex Team thru a POST to the appropriate /messages API endpoint.

And that's it.  

The message is easy to create within a python script but very easy to create as within a Secure Workflow.

Have a look to the Webex Post Message activities of the **Receive observables from a rest client** workflow.

## Webex Team Cards

Webex Team Cards are much more nice than markdown message. They act exactly like Web Pages and actually behave the same.

They offer the capability to create web formulars with complexe behaviors. With colorisation,images, Select boxes, check boxes and other nice components dedicated to interactivity with users.

![](assets/img/14.png)

Interactive Webex Team cards are very powerful, but they require "complex" bot logic needed to handle actions and selections user does.

Once again, our simulator is a perfect place to put this "complex" bot logic. And to keep the lab simple I decided to not handle this part.

Here are some awesome resources for working with Webex Team Cards :

- [Webex Team Card Designer ](https://developer.webex.com/buttons-and-cards-designer)
- [PyAdaptiveCards](https://developer.cisco.com/codeexchange/github/repo/CiscoSE/pyadaptivecards)

The Webex Team Card Designer is an online tool you can use to create your own Webex team card. The result is a JSON payload you have to pass into the **attachments** key within the POST REST call you send to Webex.

## Learn more about Webex Team Cards

Go to this link [ under construction ] if you want more information about how to work with Webex Team Cards.