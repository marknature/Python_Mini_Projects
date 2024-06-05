import random

name = input("What is your name? ")
job = input("What is your dream job? ")
gender = input("what is your gender? ")
birth_year = input("Enter your birth year: ")
age = 2023 - int(birth_year)

print("Hello, " + name + "!! Nice to meet you. You are " + str(age) + " years old, welcome to story teller.")
print("OHHH, love the dedication future " + job + ".")
print("...Let`s hope into the story. Right??????")
numbers = [1, 2, 3, "~ GO!"]
for item in numbers:
    print(item)

if gender == "male":
    pronoun = "He"
elif gender == "female":
    pronoun = "She"
else:
    pronoun = "It"

names = ["John", "Sam", "Marco", "Sandra", "Ben", "Simba", "Mezaan", "Tino"]
places = ["School", "Harare", "cape town", "shops", "market", "church", "hall", "lab"]
actions = ["kick", "run", "talk", "fly", "play", "cook", "eat", "jump"]
roles = ["doc", "enginneer", "chef", "athlete", "teacher", "driver"]

actor_name = random.choice(names)
actor_role = random.choice(roles)
quest = random.choice(actions)
magic_place = random.choice(places)

story = "Once upon a time, there was a " + job + " called " + name + ". " + \
        pronoun + " and some friends found themselves in the magic land called " + magic_place + "." + \
        " This land was ruled by " + actor_name + " the " + actor_role + "." + \
        " All of a sudden a mysterious voice spoke to them high in the sky and said you must " + quest + ". "\
        + name + " the " + job + " went to lift the curse of not being able to " + quest + "..." \
        + " THE " + job.upper() + " BECAME THE HERO OF " + magic_place.upper() + "."

print(story)
print("Thank you, for your time " + name.upper() + "." + " Story by NatureBoy!!")
