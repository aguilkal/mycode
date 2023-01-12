#!/usr/bin/python3

import random

#create a list to choose from
rps = ["rock", "paper", "scissors"]

while True:
    #print rock paper scissors to screen and save user input. Convert it to lowercase
    print("!!! Lets play Rock, Paper, Scissors !!!")
    print('Enter ("rock", "paper", "scissors")')
    player = input("--> ").lower()


    #generate a random number 0 -2
    ran = random.randrange(3)

    #set the random number to the index of rps and save as variable
    computer = rps[ran]

    #if else game logic
    print(f"Boom!...Your choice: {player}...Computer's choice: {computer}")
 
    if player == computer:
        print("It's a Tie!")

    elif player == "rock" and computer == "paper":
        print("You lose!")

    elif player == "rock" and computer == "scissors":
        print("You Win!")

    elif player == "paper" and computer == "scissors":
        print("You Lose!")

    elif player == "paper" and computer == "rock":
        print("You Win!")

    elif player == "scissors" and computer == "paper":
        print("You Win!")

    elif player == "scissors" and computer == "rock":
        print("You Lose!")

    else:
        print("Invalid choice...please choose rock, paper, scissors")

    print("Would you like to play again? Y/N")
    exit = input("-->").upper()
    print(exit)
    if exit == "N":
        break
