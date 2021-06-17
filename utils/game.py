from .deck import Deck
from typing import List
from .player import Player


class Board:
    def __init__(self, players: List[Player]):
        self.players = players
        self.turn_count = 1
        self.active_cards: List[Card] = []
        self.history_cards: List[Card] = []

    def start_game(self) -> None:
        deck = Deck()
        deck.fill_deck()
        deck.shuffle()
        deck.distribute_to_players(players=self.players)
        self._play()

    def _play(self) -> None:
        while True:
            self.active_cards = []
            self._play_turn()
            self._print_info()
            self.turn_count += 1

            if self._game_is_done(self.players):
                print("Game is done. Congratulations")
                return

    def _print_info(self) -> None:
        active_cards_string = [str(card) for card in self.active_cards]
        print(f"[{self.turn_count}] Active cards : {active_cards_string}.")
        print(f"[{self.turn_count}] Cards in history : {len(self.history_cards)}")

    def _play_turn(self) -> None:
        for player in self.players:
            card = player.play()
            self.active_cards.append(card)
        self.history_cards.extend(self.active_cards)

    def _game_is_done(self, players: List[Player]) -> bool:
        for player in players:
            if len(player.cards) != 0:
                return False
        return True
