**Welcome to Python and Amazon Echo Training**

In this training, we're going to take you through implementing a simple Python web server leveraging Flask. This web server is going to have 2 functions: 
* Handle API calls to our REST endpoints; processing the response into an Alexa readable format 
* Interact with the Amazon Developer Portal/Skills Portal to handle incoming calls from AWS via Intents and Utterances 

**What are Intents and Utterances** 

Intents are a lot like functions and  live within the Amazon Echo/Alexa platform. Utterances are used to call intents, which on our Python web server will run functions to call API's. Within AWS, an intent is formatted as follows 

[
    {
        'intent':'initialIntent'
    }
]

In this case; initialIntent is the intent. An utterance is formatted as follows

initialIntent call initial intent 

As you can see, this follows the format of "_intent_ phrase to start" 

There is also the concept of "slots" which are input fields within a phrase, we will cover these in greater detail much later

**Our Path Moving Forward**

We will be leveraging a "wrapper" tool to accelerate our learning. Flask-Ask (or Flask Alexa Skills Kit) was implemented by John Wheeler (https://github.com/johnwheeler/flask-ask) and will significant improve the speed of our skill development. 

Flask-Ask will allow us to map Flask routes back to functions within Python. These functions could be REST calls, Pyvmomi calls, pyNSXV calls, and even PowerCLI calls with enough "integrating". 

In this training, we will go end to end with building a skill that interacts with our API's in a number of different ways. Lets jump in! 

PROCEED TO "1 - Getting Started"