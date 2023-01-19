#!/usr/bin/python3
##Read in the content of the Dracule novel as a file object
with open("dracula.txt", "r") as novel:
    with open("vampytimes.txt", "w") as blood:
        ##counter
        count = 0
        ##Loop over every line print each line with "vampire"
        for line in novel:
            if "vampire" in line.lower():
                print(line)
                count +=1
                blood.write(line)
        print(f"Number of times vampire appears: {count}")         
