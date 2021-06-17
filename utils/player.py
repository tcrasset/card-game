from .card import Card

import random


class Player:
    def __init__(self, name: str):
        self.cards = []
        self.turn_count = 1
        self.number_of_cards = 0
        self.history = []
        self.name = name

    def play(self):
        # Randomly pick a card in cards
        card = random.choice(self.cards)
        self.cards.remove(card)
        # Add card to the Players history
        self.history.append(card)

        # Print {PLAYER_NAME} {TURN_COUNT} played: {CARD_NUMBER} {CARD_SYMBOL_ICON}
        print(f"[{self.turn_count}] {self.name}  played: {card.value} {card.icon}")

        self.turn_count += 1
        self.number_of_cards -= 1

        # return the card
        return card

    def __str__(self):
        return f"{self.name}"
