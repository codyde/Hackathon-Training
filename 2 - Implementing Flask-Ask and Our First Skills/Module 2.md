**Implementing Flask Ask and our First Skills**

As we start to add Flask skills, there are a few concepts to understand. Firstly; Each time we initiate a skill, we have to utilize the @ask decorator. Primarily we'll be leveraging @ask.launch and @ask.intent. 

@ask.launch is a function that runs when the skill is launched the first time. We can instantiate variables, run starter functions - anything programmatically we would want to do. 

@ask.intent is used to decorate any intents we are looking to leverage within our skill. As you recall, Intents are used to initiate actions and return responses. 

As you can see in the code, we also import the statement and question methods. These are types of responses for Flask. A statement is a single response, a question expects another response afterwards. We can use these to build conversations - or just to keep our skill open for initiating more intents after the first one is completed. 

As you can see in the code, we are able to define a variable that is a string phrase, and simply return the comment. We can also use other methods to create different types of data to return, like our date intent. 