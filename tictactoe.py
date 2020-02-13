
# class for gameboard structure and logic
class Gameboard():
    def __init__(self):
        self.board = [['-','-','-'],
                      ['-','-','-'],
                      ['-','-','-']]

    def show(self):
        for i in range(len(self.board)):
            print(self.board[i])

    def spot_exists(self, row, col):
        if (row < 0 or row > 2 or col < 0 or col > 2):
            return False
        if (self.board[row][col] == '-'):
            return True
        return False

    def mark_spot(self, row, col, player):
        if (self.spot_exists(row, col)):
            self.board[row][col] = player.mark
            return True
        return False

    def is_full(self):
        for i in range(len(self.board)):
            if ('-' in self.board[i]):
                return False
        return True

    def check_win(self, player):
        for i in range(3):
            if (player.mark==self.board[i][0]==self.board[i][1]==self.board[i][2]):
                return player
            if (player.mark==self.board[0][i]==self.board[1][i]==self.board[2][i]):
                return player
        if (player.mark==self.board[1][1]):
            if (self.board[0][0]==self.board[1][1]==self.board[2][2]):
                return player
            if (self.board[0][2]==self.board[1][1]==self.board[2][0]):
                return player
        return None


# class for player of tictactoe
class Player():
    def __init__(self, mark):
        self.mark = mark

    def make_move(self, board):
        print("Player",self.mark,"turn!")
        while (True):
            row = int(input("Enter row: "))-1
            col = int(input("Enter col: "))-1
            if (board.mark_spot(row, col, self)): break


# main game class and wrapper for other components
class TicTacToe():
    def __init__(self):
        self.gameboard = Gameboard()
        self.player_x = Player('a')
        self.player_o = Player('b')

    def gameover(self, winner):
        if (winner):
            print("Congratulations! Player",winner.mark,"won!")
        else: print("Draw!")

    # contains main game loop
    def play(self):
        winner = None
        self.gameboard.show()
        while (True):
            self.player_x.make_move(self.gameboard)
            self.gameboard.show()
            winner = self.gameboard.check_win(self.player_x)
            if (winner or self.gameboard.is_full()): break
            self.player_o.make_move(self.gameboard)
            self.gameboard.show()
            winner = self.gameboard.check_win(self.player_o)
            if (winner or self.gameboard.is_full()): break
        self.gameover(winner)


if __name__ == "__main__":
    tictactoe = TicTacToe()
    tictactoe.play()
