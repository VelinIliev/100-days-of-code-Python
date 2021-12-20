import random
import os

EASY_LEVEL = 10
HARD_LEVEL = 5

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level.lower() == "easy":
        attempts = EASY_LEVEL
    elif level.lower() == 'hard':
        attempts = HARD_LEVEL
    return attempts

def check_answer(guessed_number, random_number):
    if guessed_number == random_number:
        print("You win")
        return 0
    elif guessed_number > random_number:
        print("Too high")
    elif guessed_number < random_number:
        print("Too low")

def play_game():
    random_number = random.randint(1, 100)
    os.system('clear')
    os.system("cls")
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    attempts = set_difficulty()
    print(random_number)

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number")
        guessed_number = int(input("Make a guess: "))
        if check_answer(guessed_number, random_number) == 0:
            break
        attempts -= 1
        if attempts == 0:
            print(f"You run out of attempts. You lose.\nThe number was: {random_number}")
            break

    continue_game = input("Do you want play another game? Type 'y' ot 'n': ")
    if continue_game == 'y':
        play_game()
    else: 
        print("Goodbye")
    
play_game()

