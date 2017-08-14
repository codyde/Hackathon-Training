**Implementing Slots with Amazon Echo** 

Slots within Amazon Echo allow Alexa to receive "input" phrases to perform action. In the example we built in this module, we will use the NSX REST API to build a function that allows us to "speak" a virtual wire name thats created. 

Ultimately this virtual wire isn't connected to anything yet - so theres no network connectivity, but it shows the ability to vocally tell Alexa to "create" something. 

You can see we've created a new API file, nsxapi.py. We've updated our alexa.py file to store configparser values for NSX. We've also added new settings to our ClarityUI to hold NSX configuration values in a form. 

We've setup our nsxapi file to read those configuration details as part of the API POST. 

Our function feeds XML into the command for the post, as well as the logical switch name that we read. 

We've updated our speech assets to hold a new intent that holds a slot variable of "virtual_wires". Within the Amazon developer portal, we've built a custom slot that has several common names that could be uttered during createion. For our example we've done production, development, quality, testing. These are used to help "train" Alexa on what kinds of words could be used. 

We add these utterances in as well, and we're off to the races!