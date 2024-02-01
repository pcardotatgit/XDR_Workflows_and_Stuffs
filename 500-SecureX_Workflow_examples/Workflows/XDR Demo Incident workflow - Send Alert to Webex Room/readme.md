## XDR Demo Incident workflow - Send Alert to Webex Room

This workflow is an Incident workflow that is automatically triggered when a New XDR Incident with a specific source name is created.

This workflow is currently pre customized to be triggered when a new incident with **source=XDR Demo** is created. 
The goal of this is to be able to use it with the [Endpoint Infection XDR Demo](https://github.com/pcardotatgit/webex_for_xdr_part-7_The_final_demo) without any customization.

That means that this workflow will work exactly the same for any other Incidents. If you want to trigger this workflow from another Incident than **XDR Demo**, you just have to go to the incident rules and add a new rule for another Incident name.

When the workflow runs it parses this new incident and extracts :

- the title
- every targets 
- every observables. 

3 separated variables are created that contain targets in one side in a list with one object per line. And the same for observables in another list. And finally title is kept into another variable as well.

Then All these variables are passed to the [**Send_XDR_Alert_to_every_Security_Operators_PROD**]() subworkflow which is included into it.

The result is that the Advanced Alert Webex Card described into the [**Send_XDR_Alert_to_every_Security_Operators_PROD**](https://github.com/pcardotatgit/webex_for_xdr_part-6_XDR_send_alert_workflow) article, is sent to every Security Operators in conversation with the XDR Alert Bot.

This Alert card has the Incident title and contains two lists Security Operators can display separately, these list are targets in one list, and observables in other list. Then Security Operators can select objects to isolate and block in the list.

For the demo, you must import this workflow into your XDR workflow library.

And you must assign the correct value to the following global XDR variables :

- **XDR_ALERT_BOT_TOKEN**

## How it works ?

When an XDR Incident with **source=XDR Demo** is created ( which the [lab_simulator-002](https://github.com/pcardotatgit/lab_simulator-002) actually does ) the workflow is automatically triggered and an Alert Card is send into the BOT Webex Room.

The workflow only does this. Next steps are not managed by the workflow.