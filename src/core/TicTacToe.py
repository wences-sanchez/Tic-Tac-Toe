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

    def get_status(self):
        if self.is_impossible():
            return 'Impossible'
        elif self.has_won('X'):
            return 'X wins'
        elif self.has_won('O'):
            return 'O wins'
        elif self.is_draw():
            return 'Draw'
        else:
            return 'Game not finished'

    def has_won(self, player):
        return self.is_player_in_whole_line(player)

    def is_draw(self):
        if not self.has_won('X') and not self.has_won('O'):
            # If it doesn't have free places,
            # then the game is draw
            return not self._has_free_places()
        else:
            # If any player won, then there is never a draw
            return False

    def is_impossible(self):
        if self.has_won('X') and self.has_won('O'):
            return True
        if abs(self.count_('X') - self.count_('O')) >= 2:
            return True
        return False

    def count_(self, player):
        count_ = 0
        for row in range(self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                if self.board[row][col] == player:
                    count_ += 1
        return count_

    def _has_free_places(self):
        for row in range(self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                if self.board[row][col] == '_':
                    return True
        return False

    def is_player_in_whole_line(self, player):
        # 1. Compare rows
        for row in range(self.BOARD_SIZE):
            if self.check_if_player_is_in_whole_row(row, player):
                return True

        # 2. Compare columns
        for col in range(self.BOARD_SIZE):
            if self.check_if_player_is_in_whole_column(col, player):
                return True

        # 3. Compare diagonals
        if self.check_if_player_is_in_whole_main_diag(player) or \
                self.check_if_player_is_in_whole_second_diag(player):
            return True
        return False

    def check_if_player_is_in_whole_row(self, row, player):
        for col in range(self.BOARD_SIZE):
            if self.board[row][col] != player:
                return False
        return True

    def check_if_player_is_in_whole_column(self, col, player):
        for row in range(self.BOARD_SIZE):
            if self.board[row][col] != player:
                return False
        return True

    def check_if_player_is_in_whole_main_diag(self, player):
        for i in range(self.BOARD_SIZE):
            if self.board[i][i] != player:
                return False
        return True

    def check_if_player_is_in_whole_second_diag(self, player):
        for i in range(self.BOARD_SIZE):
            if self.board[i][self.BOARD_SIZE - i - 1] != player:
                return False
        return True

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
    user_input = input('Enter cells: ')
    tic_tac_toe = TicTacToe(user_input)
    print(tic_tac_toe)
    print(tic_tac_toe.get_status())
