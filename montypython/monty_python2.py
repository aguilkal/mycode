#!/usr/bin/env python3

#Setting a counter to zero
round = 0


while True:
    #incrementing by one 
    round = round + 1
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    #saving user input
    answer = input("Your guess--> ")
    #comparing user input to if statement
    if answer.lower() == 'brian':
        print('Correct')
        break
    elif round == 3:
        print("Sorry, the answer was Brian.")
        break
    else:
        print("Sorry! Try again!")

