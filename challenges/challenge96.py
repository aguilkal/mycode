#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import random
import html
import crayons
URL= "https://opentdb.com/api.php?amount=3&category=15&type=multiple"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()

    for d in data["results"]:
        questions = html.unescape(d.get("question"))
        print(questions)

        answers = []
        correct = []
        answers.append(html.unescape(d.get("correct_answer")))
        answers.extend(html.unescape(d.get("incorrect_answers")))
        correct.append(html.unescape(d.get("correct_answer")))
        random.shuffle(answers)

        answer_dict ={
                "A" : answers[0],
                "B" : answers[1],
                "C" : answers[2],
                "D" : answers[3]
                }
        print(f" A. {answers[0]}\n B. {answers[1]}\n C. {answers[2]}\n D. {answers[3]}\n Choose [A,B,C,D]")
        
        user_input = input("==> ").upper()
        if user_input not in ["A","B","C","D"]:
            print("Please Choose [A,B,C,D]")
        elif answer_dict[user_input] == correct[0]:
            print(crayons.green("Correct!\n)"))
        else:
            print(crayons.red("Incorrect...the correct answer was...\n") + crayons.green(correct[0]) + "\n")

if __name__ == "__main__":
    main()

