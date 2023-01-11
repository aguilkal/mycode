#!/usr/bin/env python3

##save users input to variable
char_name = input(" Which character do you want to know about? (Starlord, Mystique, Hulk)").lower()

char_stat = input(" What statistic do you want to know about? (real name, powers, archenemy)").lower()

marvelchars= {
"starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }
result = marvelchars[char_name][char_stat]
print(f" {char_name}'s {char_stat} is: " + result.title())


