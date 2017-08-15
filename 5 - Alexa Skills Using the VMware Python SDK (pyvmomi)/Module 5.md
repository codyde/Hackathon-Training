**Integrating Pyvmomi**

This module is a straight forward one. Thus far we've been exclusively working with the REST API; but there are significant amounts of API calls that are not in the vCenter REST API yet. Many of these capabilities are still accessible in Pyvmomi. 

The REST API is typically much easier to use; but with the amount of time the python SDK has been around; there are significant community resources available. 

Initially, as an example we've imported several of the pyvmomi components including SmartConnect. SmartConnect will be used to initiate the connection to the API; similar to how we pull a Session ID from the REST API. 

We create 2 functions, 1 that handles the actual authentication (creating the Service Instance), and another that simply counts the VMs in our environment. 

We map these back to Intents in our main app (alexa.py) that function through our Amazon Echo Skill. 

**Testing our Skill** 

Hopefully by now you've started testing the skill. The shortest path to testing is using Ngrok (https://ngrok.com/). Ngrok will create a secure tunnel to your localhost over a designated port. When you combine this with Flask, it'll allow you to publish our Flask app and make it accessible from AWS. 

What’s especially great is that its SSL protected; which AWS requires in order to publish Skills. 

In one of the "Advanced Concepts" modules we'll visit how to build the app in a container; which will also involve attaching a cert to it so we can publish it "properly"; for now, Ngrok is a great way to start. Make sure you’re testing your stuff! Our stuff. The stuff! 

**Next Up**

As we start parsing data and building more advanced responses; the simple one line responses that we've been working with so far aren’t the best. Additionally; Alexa's default responses don't always handle data correctly. For example, if we're returning a vCenter Server build number that’s 5 digits long, its going to read it like a standard number (ten thousand five hundred...etc). The next module will introduce us to Speech Synthesis Markup Language (SSML) which we can use to construct more advanced responses. 