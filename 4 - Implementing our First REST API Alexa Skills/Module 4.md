**Building our first skills with REST API**

We introduce a few new components in this module. You'll notice we now have a speech assets folder. We will use this to load our intent schema and utterances onto the Amazon developer center when we build our skill. You can learn more about this process at https://www.thehumblelab.com/integrating-echo-vmware/. 

We've created our basic API functions, and updated our alexa.py file to include these imports now. We've added some additional intents just for additional testing’s sake. 

You can see we've build our "@ask.launch" skill, which welcomes us to the hackathon and then presents us our question. 

Below this, each of our intents are decorated wiht the @ask.intent decorator. We've built out several intents that map back to utterances and into our intent schema within the Speech Assets folder. 

When our Alexa skill is configured and we read our utterances, the intent will be caught and the functions ran. The functions will run against the REST API and return values. 

One of the challenges we have working with the Alexa skills, is how we parse the data we get in a response. Take an example of the memoryCountIntent; this returns the memory in megabytes. In order for this to really mean anything to us, we need to change it over to gigabytes (dividing by 1024). 

Another example is how we need to limit the responses; With a standard REST call we could return all of our Virtual Machines as a JSON response. Having Alexa read us 34 machines details would be a bit brutal. We ultimately would want to consider how we want to parse this out; Only listing machines that follow certain criteria.

In our next module, we will show how we can leverage the extensive pyvmomi python SDK to query the API as well.  