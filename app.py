#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# tell our app which pages it will accept

# check conversation
# check slots
# imagine endpoint design -> /chatbot /conversation /slots /user


@app.route('/') # 'http://www.ourapi.com/' root directory
def home():
	return "Hello, world!"


app.run(port=8888)

