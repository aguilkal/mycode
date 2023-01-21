#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
import trivia_question

app = Flask(__name__)

question_answer_key = trivia_question.api_retriever()
question = question_answer_key["question"]
answer = question_answer_key["correct"]

@app.route("/correct")
def success():
    return render_template("answer.html")
@app.route("/incorrect")
def unsuccess():
    return render_template("unanswer.html")

@app.route("/")
def start():
    return render_template("challenge106.html", question_answer_key = question_answer_key)

@app.route("/login", methods = ["POST"])
def login():
        user_input = request.form.get("nm").upper()
        if question_answer_key[user_input] == answer :
                return redirect("/correct")
        else:
            return redirect("/incorrect")

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

