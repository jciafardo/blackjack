from better_blackjack.preset_folder import build_deck
from os.path import exists
"""
This file is used to load all the things we need to run game.py (player_chips, deck, number of hands, bet amount)
"""

# EXPLANATION OF GLOBAL VARIABLES BELOW ---vvvv
"""
list_of_bets is global so we can access it from game.py in the game class since it is defined in get_bet_amount.

we declare player_chips as global in get_bet_amount() because it gets modified in the get_bet_amount function
and I dont want it to be local to that function 
"""

global list_of_bets


def get_num_hands():
    try:
        num_hands = (int(input('How many hands would you like ? ')))
        get_bet_amount(num_hands)

    except ValueError:
        print('Use a valid number.')
        get_num_hands()


def get_bet_amount(num_hands):
    global player_chips   # This will change
    global list_of_bets

    list_of_bets = []

    for i in range(1, num_hands+1):
        try:
            print('How much would you like to bet on hand', i, '   Balance', player_chips)
            bet_amount = int(input())
            if bet_amount < 1:
                print('Do not bet negative numbers or 0')
                get_bet_amount(num_hands)
                return None
            list_of_bets.append(bet_amount)
            player_chips = player_chips - bet_amount
            if player_chips < 0:
                print('Bets exceed player balance... Restarting betting process')
                player_chips = int(file_data)
                get_bet_amount(num_hands)
                return None  # ends func

        except ValueError:
            print('Please use numbers only !... Restarting betting process')
            player_chips = int(file_data)
            get_bet_amount(num_hands)
            return None  # ends func

if not exists('chips.txt'):
    with open('chips.txt', 'x') as f:
        f.write('')



with open("chips.txt", "r+") as file:

    file_data = file.read()
    if len(file_data) == 0:  # if there is nothing in chips.txt
        player_chips = 100  # This will get altered (live amount of chips)
        file.seek(0)
        file.write(str(player_chips))
        file.truncate()
    else:
        try:
            player_chips = int(file_data)

        except ValueError:
            print('Chips file corrupt resetting to 100...')
            file.seek(0)
            file.write('100')
            file.truncate()

with open("chips.txt", "r") as chips_file:
    player_chips = int(chips_file.read())


deck = build_deck.deck
get_num_hands()

"""
when we save we will overwrite everything then when we run again it will load from presets file
if game is not saved we will erase everything from text file
Num hands and bet amount is also a preset
"""