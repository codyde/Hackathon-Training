**Hosting in Docker with UWSGI and NGINX**

In this module we focus on how to get our new skill running in a container that we can run on premises leveraging a docker host or better yet, vSphere Integrated Containers, VMware’s platform for running Docker containers as VMs. 

There are a lot of benefits to dropping our application into a container 

* Deployment consistency - Using a container for deployment, our application is deployed "fresh" every time. This also ties into dependency management; Deploying the application separately we have to install and configure each item from a Python perspective as well as an application stack perspective. Our container will deploy all of this for us. 
* Resource utilization - As a container, our platform uses only the minimum resources it needs from a size and performance perspective 
* Port Security - Containers typically (under best practice) only expose the ports that are needed. There are obviously ways to force all ports being exposed; but typically, it shouldn't be done. 

Once we build our container; our iterative builds are much easier to manage. We make our changes, commit our code, and build our container again. Its good and its good for you. 

We're going to be using NGINX to host our web server, and UWSGI to run the Python code within the webpage. We create a configs folder, that we store all of our configuration details for each component into. These configurations are currently specifically setup for my environment. You'll want to go through the files and modify them to meet your environment. Ultimately, we will be setting up a certificate; so, we'll need to match the hostname for that as well within the NGINX configuration. 

We setup UWSGI to run as the NGINX server, and configure a socket to run within the platform. This helps our scalability.

We don't need to worry about increasing threads and processes too high since at a given time there should only be one person connecting to the platform. 

Next up, we review our Dockerfile. Or Dockerfile is used to build our container up. It's essentially a step by step process for building the container. We setup an image (CentOS) followed by all of the configuration steps. We copy in our configurations, setup a virtual environment for Python, install our dependencies and run our app. Finally, we leverage a startup script to launch our application. 

Once our docker container is built and started, we should be able to easily browse our Docker IP address against port 443, and see our application! 

You've now completed your training!