#!/usr/bin/env python3

user_input = int(input("Enter a number: "))

if user_input > 100:
    print("That is too many beers")
else:
    for number in range(user_input, -1, -1):
        print(f"{number} bottles of beer on the wall!\n{number} bottles of beer on the Wall! {number} bottles of beer! You take one down, pass it around!")
