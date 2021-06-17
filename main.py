from utils.game import Board
from utils.player import Player


if __name__ == '__main__':
    player1 = Player("Tom")
    player2 = Player("Maxim")
    game = Board(players=[player1, player2])
    game.start_game()
