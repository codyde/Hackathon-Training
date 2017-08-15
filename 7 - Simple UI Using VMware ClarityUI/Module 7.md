**Implementing a Configuration UI with ClarityUI**

We're going to be doing a lot of things in this module that don't have a lot to do with our actual Alexa skill. 

* Bootstrap our UI with ClarityUI 
* Implementing a configuration screen to plug in our API endpoint details 
* Redesigning our REST Authentication to be a bit more intelligent (only refreshing SID when necessary)
* Implementing configparser to store configuration details in a flat file after they entered into our ClarityUI
* Designing a very simple (and not secure...) login functionality 
* Utilizing Jinja Templating in Flask to build headers and carry data between pages 

Transparency, we get a little bit "hacky" in this portion of the guide. 

We're going to be working a lot with Flask's templating language (Jinja - http://jinja.pocoo.org/docs/2.9/) and ClarityUI (https://vmware.github.io/clarity/).  

ClartyUI was originally setup to be used in a NodeJS implementation, where you can use node package manager to pull down and install the components. This gives us access to all the really great clarity goodies. The Clarity team at VMware has made it extremely easy to pull in and leverage Clarity components. I'd highly suggest checking out their documentation at https://vmware.github.io/clarity/documentation for more information about the components. 

We're going to want to install NPM on our desktop (https://www.npmjs.com/get-npm) and use NPM to pull down the clarity components as indicated in the Clarity getting started guide (https://vmware.github.io/clarity/get-started). We'll want to go through and pull down the CSS and JS files out of the modules that are installed via NPM. For this tutorial, I've attached the CSS and JS files to this repository. 

As we start to look through the directory structure, you'll see a lot of new additions. We've created folder structure to support the webpage design. We have a etc folder that’s holding all of our configuration files (auth.ini and config.ini; you can guess what each of these contain). We have a static folder holding our css and js files. We also have a templates folder that holds the HTML components. When we look in these files, we see that we're using the Clarity components to add parts of the page; The header, logon page, forms and body. 

We have these forms feed into configparser and dump these files into our .ini files to store statically. 

We've also changed our REST authentication calls to support reusing an "active" SID if possible, and if not, regenerating a new one. This has the hidden benefit of making our calls much faster when an active SID is called. 

We've updated our requirements.txt file with the updated modules required from Python. All is looking good! 

New routes have been created in the alexa.py file to handle the new UI paths we've built. These don't use the intent decorators because they aren't tied to Flask-Ask at all. I'd recommend inspecting the alexa.py file to understand the differences. 

With this completed, the core of our training is complete. At this point we have a solution that...

* Using ngrok to create an HTTPS tunnel, we can have AWS hit our Amazon Echo API and perform queries against our VMware infrastructure 
* Built a UI that can handle storing configuration of a page 
* Gotten experience with ClarityUI as a UI standard 
* Gotten exposure to REST APIs using Python
* Learned how to customize Amazon Echo responses with SSML 

We have 2 advanced "Challenge" modules that include teaching Alexa to take an "input" as well as building a Docker container (for use with vSphere Integrated Containers) that can "host" our application in a secure container! 