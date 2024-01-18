# (W0017c) - Search DNS Activity to domain in Umbrella

This workflow collects from Umbrella V2 the last 15000 DNS Activities and check if we have some DNS requests which ask for one of the domains contained in a global list of Risky Domains. Anytime an access attempt to one of these risky domains is discovered, the workflow first adds to a **target** list the internal ip address of the system which asked for this access, and second it adds to an **observable** list the requested domain.

Then the workflow builts an alert which is a webex adaptive card which contains targets and observables and send it into an Webex alert Room.

The workflow doesn't manage response action. We let the developper to developp this part. But Buttons and example of URLs to call as responses are contained into the adaptive card. Then developpers have to modify them based on their needs.

This workflow is a response workflow. That means that it can be run from the pivot menu into the ribbon or into the XDR plugin. Then in this case, the workflow doesn't use the default Risky Domain List, but it uses the selected domain into the pivot menu.

---

## Change Log

| Date | Notes |
|:-----|:------|
| January 18, 2024 | - Initial release |

---

## Requirements

This workflow requires a few subworkflow that are included into the JSON file. You have to customized initialization variables

- An Umbrella account is needed
- A Webex account is needed and an Alert Room must be created

---

## Workflow Steps

1. The workflow asks for a Athentication Token to Umbrella V2
2. Then within a loop it collect 3 time 5000 DNS requests from the Umbrella DNS Activity API
3. At the same time the collect is done thee worklfow check for every requested  domains that this one belong or not to the Risky Domain List.
4. The Risky Domain List is either the content of the **Risky_Domains** global variable if No DOMAIN Value was passed to the workflow from the pivot menu. If the workflow is triggered from the pivot menu then Risky Domain List contains the domain name of the domain that was selected. 
5. Every Time a requested domain belong to the Risky Domain List, the domain name is uniquely added to an observable list and the source internal IP address is added to a target list.
6. If matches to the Risky Domain List had been found, then the workflow  buit an Alert Adaptive Card which contains targets and observable list.
7. Finally the workflow Send the adative card to the Webex Alert Room.

---

## Configuration

Check that you have a SecureX Token configured. It is named **SecureX Token** in this workfkow.

You will have to set the value of your Umbrella **organizationID** and configure your **Umbrella Reporting basic password and basic username**.

You will have to create a dedicated Webex Bot if you don't already have One and have for it an Webex Alert Room.

Then you will need :

-**XDR_ALERT_BOT_ROOM_ID**

-**XDR_ALERT_BOT_TOKEN**


**Risky_Domains** is defined as a global XDR variable and contains by default every domains related to **ngrok**. But don't hesitate to add anyother risky domains you want. For this you just have to add these domains at the end of the existing list and use semi column as separator.

---

## Targets
Target Group: `Default TargetGroup`

| Target Name | Type | Details | Account Keys | Notes |
|:------------|:-----|:--------|:-------------|:------|
| Webex Team | HTTP Endpoint | Pre defined into XDR | XDR_ALERT_BOT_TOKEN | |
| Umbrella Reporting v2 | HTTP Endpoint | Pre defined into XDR | Umbrella Reporting : basic password and basic password | |
---

## Account Keys

| Account Key Name | Type | Details | Notes |
|:-----------------|:-----|:--------|:------|
| Umbrella Reporting | HTTP Basic Authentication | _Username:_ Client ID<br />_Password:_ Client Secret | |