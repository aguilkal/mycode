#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests

URL= "https://opentdb.com/api.php?amount=3&category=15&type=multiple"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()

    for d in data["results"]:
        print(d.get("question"))

        answers = []
        answers.append(d.get("correct_answer"))
        answers.extend(d.get("incorrect_answers"))
        print(*answers, sep="\n")

if __name__ == "__main__":
    main()

