**Introduction to vCenter REST API** 

As we start exploring REST API's and interacting with them, it'll be a really good idea for you to review the API explorer within VMWare Code (https://code.vmware.com/explorer-apis) - We can use these to help us understand what API endpoints we should or can use to our advantage. 

When we look at utilizing the vCenter REST API, we will need to pass a Username and Password to the session endpoint which will return a Session ID. We will pass this ID to each REST call we make essentially as our authentication. 

We build these into 2 separate functions, one that does the authentication and another that makes the API call. Each of our subsequent API functions will use these 2 functions to authenticate, then return the data with that session ID. 

It’s important to note, this is extremely inefficient. In a later module we will clean this up; right now it is creating a new session ID every single time we call the API. 

We create a few sample API calls; these can be tested using the python shell. Ultimately in the next module we will import these into our Flask Application to use in our individual intent methods. 

The response from the vCenter API is a JSON response, so its very easy for us to parse through and pull data out. 

With this module complete, we move onto building our first Alexa skills...