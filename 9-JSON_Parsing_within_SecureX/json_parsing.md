# JSON PARSING

In this section we are going to see how to quickly parse any big JSON data.

Open the followiing online JSON validator tool JSONPATH FINDER :

[JSON PATH FINDER](http://jsonpathfinder.com)

![](./img/image-10.png)

1. Copy the whole JSON result ( the result we had in the previous step above )
2. Go to the JSON Parser online tool : http://jsonpathfinder[.]com
3. Paste the JSON data to parse on the left panel of the tool.
4. You will see the tree structure appearing in the right panel. This one is now easy to read for humans.

![](./img/image-12.png)

On the right panel click on any item in the JSON result and look at the path edit box on the top of the panel. It contains the full path to the item.

The item will be either a final key and it's value, or a collection ( list or dictionnary ).

For example, if you search for the **hourly_data** item in the JSON result. you will understand that this one is a collection.

Okay Next step. Let's comeback to our SecureX Workflow and let's extract the current temperature in Paris.

Comeback to your workflow and in the left activity panel search for the **JSONPath Query**. Then Drag and Drop it under the **GET JSON DATA FROM WEB SITE** activity.

Name it : **extract current temperature**

![](./img/image-14.png)

Click on the activity and on it's properties panel on the right go to the **JSON Query / Source JSON to Query** edit box.

We have to put here the JSON data we want to parse. And remember this one was in the **Body** result of the **GET JSON DATA FROM WEB SITE** activity.

Then open the SecureX variable browser by clicking on the hastag icon of the **Source JSON to Query** edit box.

Then select the **Body** variable of the **GET JSON DATA FROM WEB SITE** activity.

![](./img/image-15.png)

Then scroll down to the **JSONPATH QUERIES** Section and click on the **Add** button

**JSONPath Query** edit box is where we must put the path to the key we need to extract from the JSON result.

What must we put here ?

Easy ...

Comeback to the JSONPath Finder online tool and in the right panel select the **tmp** item in the parsed data. Then copy the Path on the top of the panel.

![](./img/image-16.png)

You should have copied the following path :

**x.current_condition.tmp**

Replace the **x** letter by **$** and copy the resulting line

**$.current_condition.tmp**

This is what you have to paste in the **JSONPath Query** edit box !

This filter will extract the **tmp** item from the JSON Result and now we must assign this result to a SecureX Variable. For doing this we just have to name a variable in the **Property Name** Edit box and select it's type in the **Property Type** list box bellow.

**Property Name : RESULT**
**Property Type : Integer**


![](./img/image-17.png)


Okay, Run the workflow and check the result ... Bingo !!

![](./img/image-18.png)

So the current temperature in Paris had been assign to a SecureX Variable. This variable is now available in the SecureX Variable browser and you can use it as an input into anyother activity in this workflow.

You can update as well a global SecureX variable and make this temperature result available for other workflows !

If so, then you just have to use a **Set variable** activity, and update a Global variable that must be created first, the result of the JSONPath Query activity.

### What to do next

- Try to update a SecureX global variable
- Use the condition block activity in order to send an alert into a webex team room alert for example, if the temperature is less than 20 degrees.

## More about JSON Path Query filter

You understood that the **JSON Path Finder** online web site help a lot to figerout which **JSON Path Query filter** to use.

In order to understand why the filter must be the one we use, open the following documentation :

[https://github.com/json-path/JsonPath](https://github.com/json-path/JsonPath)

here under other filter you can use

![](./img/image-19.png)
![](./img/image-20.png)

Thanks to these Path Query filters we can do complex filtering with only one single filter.

## Parsing Nested JSON

The previous parsing method works very well for flat JSON data structures. Typically JSON files that contains several items with same keys and values.

Parsing Nested JSON with unstructured data structure is much more complex. And actually trying do parsing with only SecureX **JSONPath Query** activities leads to complex workflows. Python scripting is more relevant for such tasks

## Conclusion

We realize that SecureX has usefull JSON parsing feature that very efficient and easy to use for flat JSON structure ( Same items within the JSON structure ). But if the JSON structure to parse is complex, then we come across a lot of limitation that makes the workflow very complex to create.

And we realize that such activity would be much more simpler to acheive thanks to python scritping.

We will see this in a chapter later.

## Send an Alert to a Webex Team Room if the temperature is lower than 25°

Okay, we were able to have the current temperature in Paris, now let's see how to send an alert into a Webex Team Room if the temperature is lower than 25°.

At this achieving this goal should be easy for you.

For doing this we assume that you already know how to send an alert into a Webex Team Room.

If not have a look to the following section :

[1-Create_a_Webex_Team_Bot_Target](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/1-Create_a_Webex_Team_Bot_Target)



Here is what you have to do :

From the left activity panel, in the **logic** tab, search for the **condition block** activity and drag and drop it under the **JSON Path Query** activity.

This new activity contains 2 empty branches.  

**Notice** : you can add additionnal branches, just by clicking on the 3 dots on the top right of on of the 2 empty activities, and then select the **duplicate** action.

Then you have to customize the empty activities.

Select the first one on the left, and go to it's properties panel on the right.

- Give it a name
- In the **Condition** Section go to **Left Operand** and open the variable browser in order to select the output variable of the **JSONPath Query** activity.
- The **Operator** is : **Less Than**
- the **Right Operand** is : **25**

![](./img/image-34.png)

![](./img/image-33.png)

Now , in the left activity panel search for you **Webex_Team_Send_Alert...** activity and drag and drop it into the first empty branch. You will probably have to customize the message you want to send to tne Webex Team Alert Room. 

![](./img/image-35.png)

At this point, we don't really need the second branch as we don't want to do anything if the temperature is greater than 25 °. You can delete this second branch.

Then you can test your workflow... Run it and check the result into your alert webex team room.

![](./img/image-36.png)


## NEXT STEP JSON Parsing with a python activity

[Use python activity to parse JSON](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/blob/master/9-JSON_Parsing_within_SecureX/JSON_Parsing_with_python.md)

