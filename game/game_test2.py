"""
This file is used for playing through the game
"""

from better_blackjack.preset_folder import presets
import random
from time import sleep


class Game:
    def __init__(self):
        self.player_chips = presets.player_chips
        self.deck = presets.deck
        self.bets = presets.list_of_bets
        self.payouts = {}
        self.player_cards = []
        self.dealer_cards = []
        self.index = 0

    def dealer_first_turn(self):
        self.dealer_cards.append(my_game.draw_card(2))

    def draw_card(self, num_cards):  # Draws random cards from deck and removes card
        cards_drawn = []
        for i in range(num_cards):
            card = random.choice(self.deck)
            cards_drawn.append(card)
            self.deck.remove(card)
        return cards_drawn

    @staticmethod
    def determine_hand_value(hand):

        """
        First gets list of values in hand
        then makes all face cards value = 10
        then makes all aces value = 1
        if we can take one of the aces out and change it to a 11 and still be less than or equal to 21
        that 1(ace) will change to a 11
        """
        if any(isinstance(sub, list) for sub in hand):

            values = [item[0] for item in hand]
        else:
            values = [hand[0]]

        for i in range(len(values)):
            if values[i] == 'jack' or values[i] == 'queen' or values[i] == 'king':
                values[i] = 10

            elif values[i] == 'ace':
                values[i] = 1

        if 1 in values:
            if (sum(values) - 1) + 11 <= 21:
                index = values.index(1)
                values[index] = 11

        return sum(values)

    def check_bust_or_21(self):

        if my_game.determine_hand_value(self.dealer_cards[0]) == 21 and \
                my_game.determine_hand_value(self.player_cards[self.index]) == 21:
            print('Hand', self.index + 1, 'Is A Push')
            self.payouts.update({self.index + 1: self.bets[self.index]})
            self.index += 1


        elif my_game.determine_hand_value(self.player_cards[self.index]) > 21:
            print('Player has busted on hand', self.index + 1)
            self.payouts.update({self.index + 1: 0})
            self.index += 1

        else:
            my_game.player_choice()

    def player_choice(self):
        choice_string = 'Hand', self.index + 1, 'Hit(h), Stand(s), Double Down(dd) ? '
        choice = input(choice_string)
        if choice == 'h':
            self.player_cards[self.index].append(*my_game.draw_card(1))

            print('\n Hand', self.index + 1, '\n',
                  *[item for sublist in self.player_cards[self.index] for item in sublist],
                  'Bet Amount: ',
                  self.bets[self.index], '\n Hand Value:', my_game.determine_hand_value(self.player_cards[self.index]),
                  '\n',
                  end=' ')
            my_game.check_bust_or_21()


        elif choice == 's':
            self.index += 1

        elif choice == 'dd':

            self.player_cards[self.index].append(*my_game.draw_card(1))

            self.bets[self.index] *= 2

            print('\n', 'Dealer Cards', '\n', *self.dealer_cards[0][0], '\n', 'Hand Value: ',
                  my_game.determine_hand_value(self.dealer_cards[0][0]), 'real value: ',
                  my_game.determine_hand_value(*[self.dealer_cards[0]]))
            print('\n Hand', self.index + 1, '\n',
                  *[item for sublist in self.player_cards[self.index] for item in sublist],
                  'Bet Amount: ',
                  self.bets[self.index], '\n Hand Value:', my_game.determine_hand_value(self.player_cards[self.index]),
                  '\n',
                  end=' ')
            print('DOUBLED DOWN HAND OVER... LOADING NEXT')
            sleep(2)
            self.index += 1

        else:
            print('Invalid Input... try again')

            my_game.check_bust_or_21()

    def display(self):
        while self.index <= len(self.bets) - 1:
            self.player_cards.append(my_game.draw_card(2))

            print('\n Hand', self.index + 1, '\n',
                  *[item for sublist in self.player_cards[self.index] for item in sublist],
                  'Bet Amount: ',
                  self.bets[self.index], '\n Hand Value:', my_game.determine_hand_value(self.player_cards[self.index]),
                  '\n',
                  end=' ')

            print('\n', 'Dealer Cards', '\n', *self.dealer_cards[0][0], '\n', 'Hand Value: ',
                  my_game.determine_hand_value(self.dealer_cards[0][0]))

            my_game.check_bust_or_21()

        my_game.dealer_turn()

    def dealer_turn(self):

        if my_game.determine_hand_value(self.dealer_cards[0]) < 17:
            self.dealer_cards[0].append(*my_game.draw_card(1))
            print('Dealer Flipping Card...')
            print(self.dealer_cards[0])
            my_game.dealer_turn()

        else:
            after_game.save_winnings(self.payouts, my_game.determine_hand_value(self.dealer_cards[0]),
                                     my_game.determine_hand_value(self.player_cards[0]), self.bets, self.player_cards,
                                     self.dealer_cards)
            print('Dealer Cards: ', self.dealer_cards[0])
            print('Dealer Value: ', my_game.determine_hand_value(self.dealer_cards[0]), "\n")


class afterGame:

    @staticmethod
    def check_win(player_value, dealer_value, index, payouts, bets, player_cards, dealer_cards):
        if my_game.determine_hand_value(dealer_cards[0]) == 21 and \
                my_game.determine_hand_value(player_cards[index]) == 21:
            print('Hand', index + 1, 'Is A Push')
            payouts.update({index + 1: bets[index]})
            index += 1

        elif my_game.determine_hand_value(dealer_cards[0]) > 21:
            print('Dealer has gone bust.')
            payouts.update({index + 1: bets[index] * 2})

        elif my_game.determine_hand_value(dealer_cards[0]) == 21:
            print('Dealer Wins Hand', index + 1)
            payouts.update({index + 1: 0})
            index += 1

        elif my_game.determine_hand_value(player_cards[index]) == 21:
            print('Player Wins Hand', index + 1)
            payouts.update({index + 1: bets[index] * 2})
            index += 1

        values = [player_value, dealer_value]
        if dealer_value > 21:
            payouts.update({index + 1: bets[index] * 2})
            return True
        else:
            winning_hand = values[min(range(len(values)),
                                      key=lambda i: abs(values[i] - 21))]

            if values.index(winning_hand) == 0:
                # player wins
                return True
            else:
                # dealer wins
                return False

    def save_winnings(self, payouts, dealer_value, player_value, bets, player_cards, dealer_cards):
        for i, char in enumerate(bets):
            if i + 1 in payouts:
                pass
            else:
                if after_game.check_win(player_value, dealer_value, i, payouts, bets, player_cards,
                                        dealer_cards):  # if player wins hand
                    payouts.update({i + 1: bets[i] * 2})
                else:
                    payouts.update({i + 1: 0})

        print('Total Winnings', sum(payouts.values()))
        winnings = sum(payouts.values())
        chips = presets.player_chips + winnings
        print(chips)
        with open("chips.txt", "w") as file:
            file.write(str(chips))





after_game = afterGame()
my_game = Game()
my_game.dealer_first_turn()
my_game.display()
