**Getting Started with Flask**

Eventually, Flask will function as a API endpoint provider for our Alexa skills. We will need to build out all of our intents and routes. 

In flask, we define routes as endpoints, and then use directives to "return" content back. This content could be web pages or text. 

This module is straight forward as we will define out our "base" route (/) and have it return hello world. 

When we run "python alexa.py" from our command line, it will start the Flask development server on the "localhost". If we open up chrome and browse to http://localhost:5000 we should see "Hello, World" displayed.