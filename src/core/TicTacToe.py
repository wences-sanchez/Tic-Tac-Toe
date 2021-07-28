

class TicTacToe:
    BOARD_SIZE = 3

    def __init__(self, str_input):
        if str_input:
            self.board = [
                list(str_input[:3]),
                list(str_input[3:6]),
                list(str_input[6:9])
            ]
        else:
            self.board = [['_' * TicTacToe.BOARD_SIZE] * TicTacToe.BOARD_SIZE]

    def get_board(self):
        return self.board

    def __str__(self):
        out = '-' * 9 + '\n'
        for row in range(TicTacToe.BOARD_SIZE):
            out += '| '
            for col in range(TicTacToe.BOARD_SIZE):
                out += self.board[row][col] + ' '
            out += '|\n'
        out += '-' * 9
        return out


if __name__ == '__main__':
    tic_tac_toe = TicTacToe('')
    print(tic_tac_toe)
