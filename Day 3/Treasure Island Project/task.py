print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You are at a cross road. Where do you want to go?")

choice1 = input("Type 'left' or 'right'\n")

if choice1 == "left" or choice1 == "Left" or choice1 == "LEFT" or choice1 == "right" or choice1 == "Right" or choice1 == "RIGHT":
    if choice1 == "left" or choice1 == "Left" or choice1 == "LEFT":
        print("You have arrived at an old bridge. Do you want to cross the bridge or take the longer road.")
    elif choice1 == "right" or choice1 == "Right" or choice1 == "RIGHT":
        print("YOU DIED - you where attacked and eaten alive by cannibals.")
        raise SystemExit
else:
    print("YOU DIED - You typed the the wrong input.")
    raise SystemExit

choice2 = input("Type 'cross the bridge' or 'take the longer road'\n")

if choice2 == "take the longer road" or choice2 == "Take the longer road" or choice2 == "TAKE THE LONGER ROAD" or choice2 == "cross the bridge" or choice2 == "Cross the bridge" or choice2 == "CROSS THE BRIDGE":
    if choice2 == "take the longer road" or choice2 == "Take the longer road" or choice2 == "TAKE THE LONGER ROAD":
        print("You are now outside off an abandoned house, there are tree ways to get in, ether you enter using the front door, an open window, or through an hole in the roof using a ladder.")
    elif choice2 == "cross the bridge" or choice2 == "Cross the bridge" or choice2 == "CROSS THE BRIDGE":
        print("YOU DIED - the bridge collapsed and you fell into a lake and survived, but you were devoured by a crocodile.")
        raise SystemExit
else:
    print("YOU DIED - You typed the the wrong input.")
    raise SystemExit

choice3 = input("Type 'using the front door' or 'an open window' or 'through an hole in the roof'\n")

if choice3 == "through an hole in the roof" or choice3 == "Through an hole in the roof" or choice3 == "THROUGH AN HOLE IN THE ROOF" or choice3 == "using the front door" or choice3 == "Using the front door" or choice3 == "USING THE FRONT DOOR" or choice3 == "an open window" or choice3 == "An open window" or choice3 == "AN OPEN WINDOW":
    if choice3 == "through an hole in the roof" or choice3 == "Through an hole in the roof" or choice3 == "THROUGH AN HOLE IN THE ROOF":
        print("YOU WIN - you foud the treasure.")
    elif choice3 == "using the front door" or choice3 == "Using the front door" or choice3 == "USING THE FRONT DOOR":
        print("YOU DIED - you were killed by an unknown entity.")
    elif choice3 == "an open window" or choice3 == "An open window" or choice3 == "AN OPEN WINDOW":
        print("YOU DIED - you fell into a trap that smashed your hole body.")
else:
    print("YOU DIED - You typed the the wrong input.")
