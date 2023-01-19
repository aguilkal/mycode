#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import random
import html
URL= "https://opentdb.com/api.php?amount=3&category=15&type=multiple"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()

    for d in data["results"]:
        questions = d.get("question")
        print(html.unescape(questions))
        answers = []
        correct = []
        answers.append(d.get("correct_answer"))
        correct.append(d.get("correct_answer"))
        answers.extend(d.get("incorrect_answers"))
        random.shuffle(answers)
        print(*answers, sep="\n")
        user_input = input("==> ")
        if user_input in correct:
            print("Correct!")
        else:
            print(f"Incorrect...the correct answer was {correct}")

if __name__ == "__main__":
    main()

