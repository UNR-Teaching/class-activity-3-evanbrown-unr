import tictactoe

class TicTacToeIntegrationTest():

    # this tests the process of 2 players making a move
    # on the same board
    # this also tests the board function of marking a tile
    # since that is called inside of make_move()

    # this is the only part of the program where the objects rely on each other
    # no need for further integration testing because all other cases were covered
    # during unit testing
    def test_make_move(self):
        px = tictactoe.Player('X')
        po = tictactoe.Player('O')
        b = tictactoe.Gameboard()
        px.make_move(b)
        po.make_move(b)
        assert (not b.is_full())




def run_tests():
    integration_tests = TicTacToeIntegrationTest()
    integration_tests.test_make_move()


if __name__ == "__main__":
    run_tests()
    print("No assertions broken. All integration tests validated.")