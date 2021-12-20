import random 
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(cards):
    calculate_score = 0
    for card in cards:
        calculate_score += card
    return calculate_score

def random_card():
    card = random.choice(cards)
    return card

def display_hand(player_cards, computer_cards):
    print(f"Your hand: {player_cards}, score is: {calculate_score(player_cards)}")
    print(f'Computer hand: [{computer_cards[0]}, ?]')

def win_or_lose(player_cards, computer_cards):
    if calculate_score(player_cards) > 21:
        return 'lose'
    elif calculate_score(computer_cards) > 21:
        return 'win'
    elif calculate_score(player_cards) == calculate_score(computer_cards):
        return 'draw'
    elif calculate_score(player_cards) > calculate_score(computer_cards):
        return 'win'
    elif calculate_score(player_cards) < calculate_score (computer_cards):
        return 'lose'
    
def play_blackjack():
    print(logo)
    
    player_first_card = random_card()
    player_second_card = random_card()
    player_cards = [player_first_card, player_second_card]

    computer_first_card = random_card()
    computer_second_card = random_card()
    computer_cards = [computer_first_card, computer_second_card]

    display_hand(player_cards, computer_cards)
    
    while True:
        next_card = input("Type 'y' to get another card, type 'n' to pass: ")   
        if next_card == 'y':
            player_next_card = random_card()
            player_cards.append(player_next_card)
            display_hand(player_cards, computer_cards)
            if calculate_score(player_cards) > 21:
                break
        else:
            break

    while calculate_score(computer_cards) < 17:
        computer_next_card = random_card()
        computer_cards.append(computer_next_card)
        

    print(f"Your final hand: {player_cards}, final score: {calculate_score(player_cards)}")
    print(f'Computer funal hand: {computer_cards}, final score: {calculate_score(computer_cards)}')

    win_or_lose(player_cards, computer_cards)
    if win_or_lose(player_cards, computer_cards) == 'draw':
        print("The hand is draw")
        play_blackjack()
    else: 
        print(f"You {win_or_lose(player_cards, computer_cards)}")

play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if play_game == 'y':
    play_blackjack()
else:
    print("Goodbye")