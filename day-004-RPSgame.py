import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
list = [rock, paper, scissors]
computer_choice = random.randint(0,2)
player_choice = int(input("What do you choose?\nType:\n0 for Rock, \n1 for Paper  \n2 for Scissors\n"))

if (player_choice >= 0 and player_choice <=2):
    print(list[player_choice])
    print("Computer choice: ")
    print(list[computer_choice])

    if ((list[player_choice] == rock) and (list[computer_choice] == scissors)) or ((list[player_choice] == paper) and (list[computer_choice] == rock)) or ((list[player_choice] == scissors) and (list[computer_choice] == paper)):
        print("YOU WIN")
    elif (player_choice == computer_choice):
        print("DRAW")
    else: 
        print("YOU LOOSE")
else: 
    print("You typed wrong number. You loose!")