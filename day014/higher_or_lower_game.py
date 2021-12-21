from art import logo, vs
from game_data import data
import random
import os

def select_random(winner):
    if winner:
        random_choice_A = winner
    else: 
        random_choice_A = random.choice(data)
    while True:
        random_choice_B = random.choice(data)
        if random_choice_A != random_choice_B:
            break
    choices = []
    choices.append(random_choice_A)
    choices.append(random_choice_B)
    return choices

def format_choice(account):
    name = account["name"]
    descr = account["description"].lower()
    country = account["country"]
    return f'{name}, {descr}, from {country}'

def display_result(score):
    print(f"You're right! Current score: {score}.")

def check_answer(choice, random_choice_A, random_choice_B):
    followersA = random_choice_A["follower_count"]
    followersB = random_choice_B["follower_count"]
    
    if choice == "a":
        if followersA > followersB:
            return random_choice_A
        else: 
            return False
    elif choice == "b":
        if followersA < followersB:
            return random_choice_B
        else: 
            return False  

def display_final(score):
    print(f"\nSorry, that's wrong. Final score: {score}")

def play_game():
    score = 0
    winner = {}

    while True:
        os.system('clear')
        os.system("cls")
        print(logo)
        if score > 0:
            display_result(score)

        choices = select_random(winner)
        random_choice_A = choices[0]
        random_choice_B = choices[1]
            
        print(f'compare A: {format_choice(random_choice_A)}')
        print(vs)
        print(f'Compare B: {format_choice(random_choice_B)}')

        choice = input("\nWho has more followers? Tpye 'A' or 'B': ").lower()
        check = check_answer(choice, random_choice_A, random_choice_B)
        if check != False:
            score += 1
            winner = check
        else: 
            break

    display_final(score)
    continue_play = input("\nDo you want to play again? Type 'y' or 'n': ")
    if continue_play == 'y':
        play_game()

play_game()