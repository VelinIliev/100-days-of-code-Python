import os 

os.system('clear') #for OSX and Linux 
os.system("cls") #for windows

print('Welcome to the secret auction program.')
bid_players = {}
end_of_bid = False

def new_bid_player(name, bid):
    bid_players[name] = bid

def find_winner():
    find_max = 0
    for key in bid_players:
        if find_max < bid_players[key]:
            find_max = bid_players[key]
            winner = key
    print()
    print("*"*40)
    print()
    print(f'The winner is {winner.capitalize()}, with bid of {find_max:.2f}$')
    print()
    print("*"*40)
    print()

while not end_of_bid:
    name = input("What is your name?:\n")

    while True:
        try:
            bid = float(input("What is your bid?: \n$"))
        except ValueError:
            print("Please enter a number")
        else:
            break
    
    new_bid_player(name = name, bid = bid)
    
    while True:
        continue_bid = input("Are there any other bidders? Type 'yes' or 'no'\n")
        if continue_bid.lower() == "no":
            end_of_bid = True
            break
        elif continue_bid.lower() == "yes":
            break
        else: 
            print("Please enter 'yes' or 'no'.")
            
    os.system('clear') 
    os.system("cls")

find_winner()

