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
os.system('clear')
os.system("cls")
print(logo)
print("Guess the word:")

while not end_of_game:

    print(dipsay_as_string(display))

    letter_from_user = input("\nGuess a letter: \n").lower()
    os.system('clear') #for OSX and Linux os.system('cls') for windows
    os.system("cls")
    print(stages[lives])
    # print(word_to_guess)
    
    if letter_from_user in word_to_guess: 
        for n in range(0, word_length):
            if letter_from_user == word_to_guess[n]:
                display[n] = letter_from_user

        if letter_from_user in used_letters :
            
            print("You alredy used this letter")
        
        if "_" not in display:
            end_of_game = True
            print("YOU WIN!")
        
        used_letters += letter_from_user
        print(f'Typed letters: {dipsay_as_string(used_letters)}')

    elif (lives > 0): 
        if letter_from_user in used_letters :
            print("You alredy used this letter")
            
        else:
            os.system('clear')
            os.system("cls")
            lives -= 1 
            print(stages[lives])
            print(f'The letter "{letter_from_user}" is not in the word.')
        
            if lives == 0:
                os.system('clear')
                os.system("cls")
                print(stages[lives])
                end_of_game = True
                print(f'The word was: {word_to_guess}')

        used_letters += letter_from_user
        print(f'Typed letters: {dipsay_as_string(used_letters)}')

