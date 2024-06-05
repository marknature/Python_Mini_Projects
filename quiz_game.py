print("Welcome to Nature's Quiz Game.")
play = input("Do you want yo play, Y/N? ")

if play.lower() != "y":
    quit()
print("Okay! Lets play, please answer in small letters.")
score = 0

answer = input("What is the color of the sky? ").lower()
if answer == "blue":
    print("Correct!")
    score += 1
else:
    print("Incorrect! ")

answer = input("How many planets are in our solar system? ").lower()
if answer == "8":
    print("Correct!")
    score += 1
else:
    print("Incorrect! ")

answer = input("Does nature illustrate God's ability? ").lower()
if answer == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect! ")

answer = input("What am I seeing, hearing, feeling, smelling & tasting? ").lower()
if answer == "things":
    print("Correct!")
    score += 1
else:
    print("Incorrect! ")

print("You got " + str(score) + "/5" + " questions correct!")
print("You got " + str(score/5 * 100) + "%")