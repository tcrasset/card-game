
from .deck import Deck

class Board():
    def __init__(self, players):
        self.players = players
        self.turn_count = 1
        self.active_cards = []
        self.history_cards = []


    def start_game(self):
        # Start the game and fill the deck
        deck = Deck()
        deck.fill_deck()
        deck.shuffle()

        # Distribute the cards of the Deck to the players
        deck.distribute(self.players)

        while True:
            # Make each player play a card
            for player in self.players:
                card = player.play()
                self.active_cards.append(card)


            # Print the turn count; list of active card and the number of cards
            # in history
            active_cards_string = [str(card) for card in self.active_cards]
            print(f"[{self.turn_count}] Active cards : {active_cards_string}, #Cards in history : {len(self.history_cards)}")

            self.history_cards.extend(self.active_cards)
            self.active_cards = []
            self.turn_count += 1

            if self._gameIsDone(self.players):
                print("Game is done. Congratulations")
                break
            else:
                continue


    def _gameIsDone(self, players):
        for player in players:
            if len(player.cards) != 0:
                return False
        return True



