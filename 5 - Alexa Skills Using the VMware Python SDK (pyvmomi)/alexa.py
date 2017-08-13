from flask import Flask
from flask_ask import Ask, statement, question
import time
from pyvcapi import get_vcenter_clusters, get_vcenter_health_status, vm_count, vm_memory_count, get_uptime, get_first_cluster, count_vms_pyvmomi

app = Flask(__name__)
ask = Ask(app, "/hackathon")


@app.route('/')
def homepage():
    return 'Flask Server is Running Successfully'


@ask.launch
def start_skill():
    welcome_message = "Welcome to the hackathon, ask me a question and i'll give you some answers"
    return question(welcome_message)


@ask.intent('currentDateIntent')
def current_date():
    currentDate = time.strftime("%d/$m/%Y")
    return statement("The current date is " + currentDate)


@ask.intent('getvcHealthIntent')
def get_vcenter_health():
    health = get_vcenter_health_status()
    return statement("The health of your vCenter environment is {}".format(health))

@ask.intent("VMCountIntent")
def share_count():
    counting = vm_count()
    count_msg = 'The total number of virtual machines \
registered in this v-center is {}'.format(counting)
    return question(count_msg)

@ask.intent("memoryCountIntent")
def memory_count():
    memCount = vm_memory_count()/1024
    count_msg = 'You have provisioned {} gigabytes of memory'.format(memCount)
    return question(count_msg)

@ask.intent("ApplianceUptimeIntent")
def uptime_appliance():
    ut = get_uptime()
    uptimeMsg = 'Your current VCSA uptime is {} hours'.format(ut)
    return question(uptimeMsg)

@ask.intent("GetFirstClusterIntent")
def first_cluster():
    fc = get_first_cluster()
    return statement(fc)

@ask.intent("CountVMsPyvmomi")
def python_count():
    count = count_vms_pyvmomi()
    return statement("you currently have {} virtual machines in your environment".format(count))

@ask.intent("NoIntent")
def no_intent():
    bye_text = 'Was it something I said?'
    return statement(bye_text)


if __name__ == '__main__':
    app.run(debug=True)
