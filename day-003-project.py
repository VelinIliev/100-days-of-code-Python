print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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
print()
choice1 = input("You're at a cross road. Where do you want to go? \nType \"left\" or \"right\"\n")
if choice1.lower() == "left":
    choice2 = input("\nYou've come to a lake. \nThere is an island in the middle of the lake. \nType \"wait\" to wait for a boat. \nType \"choice2\" to choice2 across.\n")
    if choice2.lower() == 'wait':
        choice3 = input("\nYou are in front of 3 doors. \nRed, yellow and blue. \nWich will you select?\n")
        if choice3.lower() == 'red':
            print("Burned by fire.\nGAME OVER")
        elif choice3.lower() == 'blue':
            print("Eaten by beasts.\nGAME OVER")
        elif choice3.lower() == 'yellow':
            print("YOU WIN!")
        else: 
            print("GAME OVER")
    else:
        print("Atracked by trout.\nGAME OVER")
else:
    print("Fall into a hole.\nGAME OVER")
