**Advanced Responses with Speech Synthesis Markup Language (SSML)**

We're going to be referencing the SSML reference from Amazon a lot for this module - https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/speech-synthesis-markup-language-ssml-reference. 

Flask has a very rich templating engine built into it. We'll be using it in the next module when we start building our user interface. For now, we are introducing a templates.yaml file which will hold our SSML code. As you read the link above, you'll see references to how to "encode" the responses. Using Flask we can feed variables into the template, which Flask-Ask will then read back. 

To support our templating, you'll notice we're also adding render_template onto our Flask imports. 

SSML will let us change how Alexa reads numbers, change her tone, emphasize words and phrases, even create some...interesting...ways of speaking. Play with it! Have fun! 

We've created a basic example within of a "Datacenter Status" intent that reads over the health of the vCenter, the version of the API, the version of vCenter, and counts the machines. 

**What’s Next** 

Up until now we've really just an API gateway for AWS. We've had to hard code configuration data within our application. In the next module we're going to dig into the user interface. We'll build a simple logon page, and a configuration page. We'll also clean up some of our code to make it a bit more production worthy. We'll introduce some configuration flat files that can be updated from our interface. 

We've built this interface using ClarityUI, VMware’s open source user interface toolkit; so you'll get a bit of experience working with that as well! 