import unittest
import tictactoe

class GameboardUnitTests(unittest.TestCase):
    # tests that you can only make move on a valid spot
    def test_spot_exists(self):
        b = tictactoe.Gameboard()
        self.assertEqual(True, b.spot_exists(1,1))
        self.assertEqual(False, b.spot_exists(4,4))

    # tests the board is full when it should be
    def test_is_full(self):
        b = tictactoe.Gameboard()
        b.board = [['X','O','X'],
                   ['X','O','O'],
                   ['O','X','-']]
        self.assertFalse(b.is_full())
        b.board = [['X','O','X'],
                   ['X','O','O'],
                   ['O','X','X']]
        self.assertTrue(b.is_full())

    # tests whether the game logic can detect a winner
    # None is returned if there is currently no winner
    # or if there is a draw
    def test_check_win(self):
        b = tictactoe.Gameboard()
        player = tictactoe.Player("X")
        b.board = [['X','X','X'],
                   ['X','O','O'],
                   ['O','O','X']]
        self.assertEqual(player, b.check_win(player))
        b.board = [['X','O','X'],
                   ['X','O','O'],
                   ['O','X','X']]
        self.assertEqual(None, b.check_win(player))



if __name__ == "__main__":
    unittest.main()