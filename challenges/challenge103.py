#!/usr/bin/env python3

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template

app= Flask(__name__)

URL= "https://opentdb.com/api.php?amount=3&category=11&difficulty=medium&type=multiple"

resp= requests.get(URL).json()

@app.route("/")
def index():
    return render_template()
