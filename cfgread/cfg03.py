#!/usr/bin/env python3

## counter for customization 4
line_count = 0
## create file object in "r"ead mode
with open("vlanconfig.cfg", "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)
for line in configlist:
    line_count += 1
print(f"Number of lines: {line_count}")
## each item of the list now has the "\n" characters back
print(configlist)

