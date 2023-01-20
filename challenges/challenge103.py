#!/usr/bin/env python3

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template

app= Flask(__name__)

##URL= "https://opentdb.com/api.php?amount=3&category=11&difficulty=medium&type=multiple"

##resp= request.get(URL).json()

@app.route("/")
def index():
    return render_template("challenge103.html")

@app.route("/correct")
def correct():
    return render_template("correct.html")

@app.route("/trivia", methods=["POST"])
def question():
    if request.form.get("answer") == "hearts":
         return redirect("correct")
    else:
        return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
