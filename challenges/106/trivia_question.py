#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import random
import html
#global api url
URL= "https://opentdb.com/api.php?amount=1&category=9&type=multiple"

def api_retriever():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()
    
    for d in data["results"]:
        #created variables and stripped html syntax
        questions = html.unescape(d.get("question"))
        correct_answer = html.unescape(d.get("correct_answer"))
        incorrect_answers = html.unescape(d.get("incorrect_answers"))
        
        #created answer list
        answers = []
        answers.append(correct_answer)
        answers.extend(incorrect_answers)
        #shuffled the list so the correct answer is not always in the same spot
        random.shuffle(answers)
        #created a dictionary with questions and answers
        question_answer_key ={
                "question" : questions,
                "A" : answers[0],
                "B" : answers[1],
                "C" : answers[2],
                "D" : answers[3],
                "correct" : correct_answer
                }
        return question_answer_key
