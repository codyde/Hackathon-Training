from flask import Flask
from flask_ask import Ask, statement, question
import time

app = Flask(__name__)
ask = Ask(app, "/hackathon")


@app.route('/')
def homepage():
    return 'Flask Server is Running Successfully'


@ask.launch
def start_skill():
    welcome_message = "Welcome to the VMworld hackathon, ask me a question and i'll give you some answers"
    return question(welcome_message)


@ask.intent('currentDateIntent')
def current_date():
    currentDate = time.strftime("%d/$m/%Y")
    return statement("The current date is " + currentDate)


@ask.intent("NoIntent")
def no_intent():
    bye_text = 'Was it something I said?'
    return statement(bye_text)


if __name__ == '__main__':
    app.run(debug=True)
