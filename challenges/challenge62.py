farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


#part 1

ne_animals = farms[0]['agriculture']

for animal in ne_animals:
    print(animal)

#part 2

print("Choose NE, W, or SE")
user_input = input("==>").lower()

if user_input == "ne":
    print(farms[0]['agriculture'])
elif user_input == "w":
    print(farms[1]['agriculture'])
else:
    print(farms[2]['agriculture'])

#part 3

veggies = ["carrots", "celery"]

for farm in farms:
    print("-", farm["name"])
print("Pick a farm")
user_input = input("==>")

for farm in farms:
    if farm["name"].lower() == user_input.lower():
        for item in farm["agriculture"]:
            if item not in veggies:
                print(item)
