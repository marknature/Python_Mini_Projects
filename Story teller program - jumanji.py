# Choose Your Own Adventure

name = input("Enter your name: ")
print("Welcome to Jumanji " + name + ", if you wish to leave the game, recover the jewel and call out its name!")

plot = "Upon starting it, the group is sucked into Jumanji, landing in a jungle as their chosen avatars – Spencer as "
"muscular archaeologist Dr. Xander 'Smolder' Bravestone, Fridge as zoologist Franklin 'Mouse' Finbar, Bethany "
"as male cartographer and paleontologist Professor Sheldon 'Shelly' Oberon, and Martha as sultry martial arts "
"expert Ruby Roundhouse. Three marks on their arms denote their lives in the game, making them afraid that if "
"they lose all three, they will actually die. The group's goal is to end a curse on Jumanji, brought about by "
"corrupt archaeologist Professor Van Pelt[b] after he stole a magical jewel called the Jaguar's Eye and gained "
"control of the jungle's animals. They must return the jewel to the shrine and call out Jumanji! to lift the "
"curse and leave the game."
print(plot)

actor_name = input("Please pick a character; Dr Smolder Bravestone, Mouse or Ruby Roundhouse. or just type Q to "
                   "quit: ").lower()
if actor_name == "dr smolder bravestone":
    print("You", name, "are now Dr. Xander 'Smolder' Bravestone. When he was a boy, Xander's parents were murdered by "
                       "the dastardly Jurgen the Brutal. Within the world of JUMANJI, Bravestone is an international "
                       "explorer and famed archaeologist, well known in both the realm of JUMANJI, and across the seven"
                       " continents for his courageous exploits. After he saved Franklin 'Mouse' Finbar's life from a "
                       "warlord in Peru, he has never left Dr. Bravestone's side. He was also a former colleague of "
                       "Professor Van Pelt. During the Jaguar Shine Adventure, after receiving a letter from the field "
                       "guide Nigel Billingsley, he arrived in JUMANJI with his companions to answer the call for aid"
                       " to lift the curse. When Jurgen the Brutal returned to steal the Falcon Jewel, Nigel sent Dr. "
                       "Bravestone a new letter to call for help, so that he and his crew would return to complete the "
                       "Mountain Fortress Adventure and save the land of JUMANJI, once again")
elif actor_name == "mouse":
    print("You", name, "are now Franklin 'Mouse' Finbar. Finbar is Dr. Smolder Bravestone's sidekick. According to "
                       "Nigel's information, he has never left Bravestone's side after Bravestone rescued him from the "
                       "clutches of a warlord in the jungles of Peru. He earned his nickname Mouse from his small "
                       "stature and apparent adorable personality.")
elif actor_name == "ruby roundhouse":
    print("You", name, "are now Ruby Roundhouse. Ruby Roundhouse's background before travelling to Jumanji is unknown, "
                       "but she is described as a killer of men. Her symbol on the player select screen is a karate "
                       "fighter, reflecting her role as a fighter.")
elif actor_name == "q":
    print("You, " + name + " ,and were captured during the transfer. You back in the MATRIX, we never met, GOODBYE!")
    quit()
else:
    print("If you wish to play the game choose a charactor")

start = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like "
              "to go left or right? ").lower()

if start == "left":
    river = input("You come to a river, you can walk around it or swim across (Type walk or swim): ").lower()
    if river == "walk":
        bridge = input("You are now by a wobbly bridge, do you want to cross it or head back (cross/back): ").lower()
        if bridge == "cross":
            print("The bridge breaks while you crossing and you fall. You survive, but then your devoured by hungry"
                  " jaguars. Game Over")
        else:
            print("You go back to the start and go right!")
            dessert = input(
                "You are now in the dessert, walk around it or drive across with the doom buggy you see in the "
                "distance (Type walk or drive): ").lower()
            if dessert == "drive":
                jungle = input("You are now in the jungle, and you drive till a wobbly bridge made of rope and twigs. "
                               "Do you want to cross it or drive around (cross/around):")
                if jungle == "cross":
                    MPC = input(
                        "You almost fall into an alligator filled river, but you make it across safely. You meet a "
                        "stranger with a map talk to them or just walk past? (talk/walk)").lower()
                    if MPC == "talk":
                        shelly = input(
                            "My name is Professor Sheldon 'Shelly' Oberon. He is an expert in the study of maps"
                            ", making him the only character who is able to read the Map of JUMANJI. Follow me to the"
                            " next level. Follow or run away (follow/run): ").lower()
                        if shelly == "follow":
                            print("Congratulations we know have a maps men, you can now continue to the next level.")
                            print("Alert: please download the next level with the link below.")
                            print("https//:www.jumanji.co.za/the_next_level")
                        else:
                            print(
                                "You run away and continue alone. You continue walking till you reach a dead end "
                                "and you are killed by the guys who stole the jewel. Game Over!")
                    else:
                        print(
                            "You continue walking till you reach a dead end and you are killed by the guys who stole "
                            "the jewel. Game Over!")
            else:
                print("While walking around the dessert edge, you were bitten by a king cobra. Game Over!")
    elif river == "swim":
        MPC = input("You are almost eaten by an alligator, but you make it across safely. You meet a stranger with a "
                    "map talk to them or just walk past? (talk/walk)")
        if MPC == "talk":
            shelly = input("My name is Professor Sheldon 'Shelly' Oberon. He is an expert in the study of maps"
                           ", making him the only character who is able to read the Map of JUMANJI. Follow me to the"
                           " next level. Follow or run away (follow/run): ").lower()
            if shelly == "follow":
                print("Congratulations we know have a maps men, you can now continue to the next level.")
                print("Alert: please download the next level with the link below.")
                print("https//:www.jumanji.co.za/the_next_level")
            else:
                print("You run away and continue alone. You continue walking till you reach a dead end and you are "
                      "killed by the guys who stole the jewel. Game Over!")
        else:
            print("You continue walking till you reach a dead end and you are killed by the guys who stole the jewel."
                  " Game Over!")
    else:
        print("That's an invalid response. Due to that, you were eaten by a hippo. Game Over!")

elif start == "right":
    dessert = input("You are now in the dessert, walk around it or drive across with the doom buggy you see in the "
                    "distance (Type walk or drive): ").lower()
    if dessert == "drive":
        jungle = input("You are now in the jungle, and you drive till a wobbly bridge made of rope and twigs. "
                       "Do you want to cross it or drive around (cross/around):")
        if jungle == "cross":
            MPC = input(
                "You almost fall into an alligator filled river, but you make it across safely. You meet a stranger "
                "with a map talk to them or just walk past? (talk/walk)")
            if MPC == "talk":
                shelly = input("My name is Professor Sheldon 'Shelly' Oberon. He is an expert in the study of maps"
                               ",making him the only character who is able to read the Map of JUMANJI. Follow me to the"
                               " next level. Follow or run away (follow/run): ").lower()
                if shelly == "follow":
                    print("Congratulations we know have a maps men, you can now continue to the next level.")
                    print("Alert: please download the next level with the link below.")
                    print("https//:www.jumanji.co.za/the_next_level")
                else:
                    print("You run away and continue alone. You continue walking till you reach a dead end and you are "
                          "killed by the guys who stole the jewel. Game Over!")
            else:
                print(
                    "You continue walking till you reach a dead end and you are killed by the guys who stole the jewel."
                    " Game Over!")
    else:
        print("While walking around the dessert edge, you were bitten by a king cobra. Game Over!")

else:
    print("That's an invalid response. Due to that, you were eaten by a black panther. Game over!")

print("By Nature. Thank you, for playing " + name + ". You the best!!! All credit to Jumanji: Welcome to "
                                                    "the Jungle (alternately known as 'JUMANJI 2') is a sequel to the "
                                                    "original 1995 film. The story follows four high school students"
                                                    " who discover JUMANJI.")
