import unittest
from game_loop import TicTacToeBoard
from game_conditions import GameLogic


class TestGame(unittest.TestCase):

    def test_check_win_chances(self):
        game1 = TicTacToeBoard()
        game2 = GameLogic()
        game1.board1 = [
            ["X", "O", "O"],
            ["X", "X", "O"],
            ["X", "O", "X"]
        ]
        winner = game2.check_win_chance(game1.board1)

        self.assertEqual(winner, "X")


if __name__ == '__main__':
    unittest.main()
