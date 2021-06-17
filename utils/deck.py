from .card import Card
from .player import Player

import random

class Deck():
    def __init__(self):
        self.cards = []

    def fill_deck(self):
        # Fill cards with every possible instance of cards
        possible_icon = ['♥', '♦', '♣', '♠']
        possible_values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K' ]
        
        for icon in possible_icon:
            for value in possible_values:
                card = Card(value, icon)
                self.cards.append(card)
        
    def shuffle(self):
        return random.shuffle(self.cards)

    def distribute(self, players : list):
        while self.cards:
            for player in players:
                player.cards.append(self.cards.pop())
                player.number_of_cards += 1