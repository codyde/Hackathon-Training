from flask import Flask, render_template, redirect, request, url_for, jsonify, session
from flask_ask import Ask, statement, question
from flask_assets import Bundle, Environment
import time
from pyvcapi import *
from nsxapi import *
import configparser

app = Flask(__name__)
app.secret_key = "super secret key"
ask = Ask(app, "/hackathon")

env = Environment(app)
js = Bundle('js/clarity-icons.min.js', 'js/clarity-icons-api.js',
            'js/clarity-icons-element.js', 'js/custom-elements.min.js')
env.register('js_all', js)
css = Bundle('css/clarity-ui.min.css', 'css/clarity-icons.min.css')
env.register('css_all', css)


@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == "POST":
        attempted_username = request.form['username']
        print(attempted_username)
        attempted_password = request.form['password']
        print(attempted_password)
        if attempted_username == "admin" and attempted_password == "password":
            session['logged_in'] = True
            session['wrong_pass'] = False
            session['username'] = request.form['username']
            return redirect(url_for('configurepage'))
        else:
            session['logged_in'] = False
            session['wrong_pass'] = True
    return render_template('index.html')


@app.route('/configure/', methods=['GET', 'POST'])
def configurepage():
    if session['logged_in'] is True:
        if request.method == "POST":
            url = request.form['vcenterurl']
            user = request.form['vcenteruser']
            password = request.form['vcenterpassword']
            nsxurl = request.form['nsx_server_url']
            nsxuser = request.form['nsx_server_user']
            nsxpass = request.form['nsx_server_pass']
            Config = configparser.ConfigParser()
            cfgfile = open(".//etc//config.ini", 'w')
            Config.add_section('vcenterConfig')
            Config.set('vcenterConfig', 'url', url)
            Config.set('vcenterConfig', 'user', user)
            Config.set('vcenterConfig', 'password', password)
            Config.add_section('nsxConfig')
            Config.set('nsxConfig', 'url', nsxurl)
            Config.set('nsxConfig', 'user', nsxuser)
            Config.set('nsxConfig', 'password', nsxpass)
            Config.write(cfgfile)
            cfgfile.close()
        return render_template('configure.html')
    else:
        return redirect(url_for('homepage'))


@app.route('/logout/')
def logout():
    session['logged_in'] = False
    return redirect(url_for('homepage'))


@ask.launch
def start_skill():
    welcome_message = "Welcome to the hackathon, ask me a question and i'll give you some answers"
    return question(welcome_message)


@ask.intent('currentDateIntent')
def current_date():
    currentDate = time.strftime("%m/%d/%Y")
    return question("The current date is " + currentDate)


@ask.intent('getvcHealthIntent')
def get_vcenter_health():
    health = get_vcenter_health_status()
    return question("The health of your vCenter environment is {}".format(health))


@ask.intent("VMCountIntent")
def share_count():
    counting = vm_count()
    count_msg = 'The total number of virtual machines \
registered in this v-center is {}'.format(counting)
    return question(count_msg)


@ask.intent("memoryCountIntent")
def memory_count():
    memCount = vm_memory_count() / 1024
    count_msg = 'You have provisioned {} gigabytes of memory'.format(memCount)
    return question(count_msg)


@ask.intent("ApplianceUptimeIntent")
def uptime_appliance():
    ut = get_uptime()
    uptimeMsg = 'Your current VCSA uptime is {} hours'.format(ut)
    return question(uptimeMsg)


@ask.intent("CountVMsPyvmomi")
def python_count():
    count = count_vms_pyvmomi()
    return statement("you currently have {} virtual machines in your environment".format(count))


@ask.intent("dcReportIntent")
def dc_report():
    count = count_vms_pyvmomi()
    health = get_vcenter_health_status()
    (version, build) = get_vcenter_build()
    report_msg = render_template('AdvancedSSML', count=count, health=health, version=format(version), build=build)
    return question(report_msg)


@ask.intent("CheckNsxApi")
def check_nsx():
    status = validateNSX()
    return question(status)


@ask.intent("createNSXWire")
def create_vwire(vwname):
    lsvwire = createNsxWire(vwname)
    return question(lsvwire)


@ask.intent("NoIntent")
def no_intent():
    bye_text = 'Was it something I said?'
    return statement(bye_text)


if __name__ == '__main__':
    app.run(debug=True)
