#!/usr/bin/python3

import random
#print rock paper scissors to screen and save user input
print("Lets play Rock, Paper, Scissors,")
player = input("--> ")

#convert input to lowercase
player.lower()

#create a list to choose from

rps = ["rock", "paper", "scissors"]

#generate a random number 0 -2
ran = random.randrange(3)

#set the random number to the index of rps and save as variable

computer = rps[ran]

#if else game logic
print(f"Boom!...Your choice: {player}...Computer's choice: {computer}")

if player == "rock" and computer == "paper":
    print("You lose!")

elif player == "rock" and computer == "scissors":
    print("You Win!")

elif player == "rock" and computer == "rock":
    print("Tie!")

elif player == "paper" and computer == "paper":
    print("Tie!")

elif player == "paper" and computer == "scissors":
    print("You Lose!")

elif player == "paper" and computer == "rock":
    print("You Win!")
elif player == "scissors" and computer == "paper":
    print("You Win!")

elif player == "paper" and computer == "scissors":
    print("You Lose!")

elif player == "paper" and computer == "paper":
    print("Tie!")
else:
    print("Invalid choice...please choose rock, paper, scissors")
