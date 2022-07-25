"""
This file is used to build our deck
"""


class Deck:
    def __init__(self):
        self.deck = []
        self.suits = ['hearts', 'spades', 'clubs', 'diamonds']
        self.values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace"]

    def build_deck(self):
        for suit in self.suits:
            for i in self.values:
                self.deck.append([i, 'of', suit])


my_deck = Deck()
my_deck.build_deck()
deck = my_deck.deck  # This gets passed to presets.py
