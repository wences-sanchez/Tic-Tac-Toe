

class TicTacToe:
    BOARD_SIZE = 3

    def __init__(self):
        self.board = [['X', 'O', 'X'],
                      ['O', 'O', 'X'],
                      ['X', 'X', 'O']]

    def get_board(self):
        return self.board

    def __str__(self):
        out = ''
        for row in range(TicTacToe.BOARD_SIZE):
            for col in range(TicTacToe.BOARD_SIZE):
                out += self.board[row][col] + ' ' if col < TicTacToe.BOARD_SIZE - 1 else self.board[row][col]
            out += '\n' if row < TicTacToe.BOARD_SIZE - 1 else ''
        return out


if __name__ == '__main__':
    tic_tac_toe = TicTacToe()
    print(tic_tac_toe)
