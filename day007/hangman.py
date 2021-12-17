import random
from hangman_words import word_list
from hangman_art import stages, logo
import os 

word_to_guess = random.choice(word_list)
word_length = len(word_to_guess)

display = []
for n in range(0, word_length):
    display += "_"

used_letters = []
end_of_game = False
lives = 6


def dipsay_as_string(display):
    display_str = " ".join(display)
    return display_str
    
def display_result(msg):
    os.system('clear') #for OSX and Linux os.system('cls') for windows
    os.system("cls")
    print(word_to_guess)
    print(stages[lives])
    if len(used_letters) == 0:
        print()
    else:
        print(f'Typed letters: {dipsay_as_string(used_letters)}')
    print(msg)
    if end_of_game == True:
        if msg == "YOU WIN!":
            end_msg = "You guessed the word:"
        else:
            end_msg = "The word was:"
        print()
        print("*"*30)
        print(f'{end_msg} {word_to_guess}')
        print("*"*30)
        print()

os.system('clear')
os.system("cls")
print(logo)
print("Guess the word:")

while not end_of_game:
    msg = ""
    print(dipsay_as_string(display))

    letter_from_user = input("\nGuess a letter: \n").lower()
    if (len(letter_from_user) > 1):
        msg = 'please enter only one letter'
    elif ord(str(letter_from_user)) < 97 or ord(str(letter_from_user)) > 122:
        msg = 'please enter a letter'    
    elif letter_from_user in word_to_guess: 
        for n in range(0, word_length):
            if letter_from_user == word_to_guess[n]:
                display[n] = letter_from_user

        if letter_from_user in used_letters :
            msg = "You alredy used this letter"
        
        elif "_" not in display:
            end_of_game = True
            msg = "YOU WIN!" 
        used_letters += letter_from_user

    elif (lives > 0): 
        if letter_from_user in used_letters :
            msg = "You alredy used this letter"
        else:
            lives -= 1 
            msg = f'The letter "{letter_from_user}" is not in the word.'
            used_letters += letter_from_user

            if lives == 0:
                end_of_game = True              

    display_result(msg)

