import re


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
            self.board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

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
            return not self.has_free_places()
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

    def has_free_places(self):
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

    def is_empty_cell(self, row, col):
        return self.get_board_cell(row, col) == '_'

    def set_value_in_cell(self, row, col, value):
        if not re.match(r'^-*\d$', str(row)) or not re.match(r'^-*\d$', str(col)) or \
                type(row) is not int or type(col) is not int:
            raise ValueError

        if row < 1 or row > 3 or col < 1 or col > 3:
            raise IndexError
        else:
            self.board[row - 1][col - 1] = value

    def get_board(self):
        return self.board

    def get_board_cell(self, row, col):
        """
        Returns a position in the board with natural indexes
        :param row: An row input in [1,3]. Go transparent in low-level
        :param col: An column input in [1,3]. Go transparent in low-level
        :return: The position of the board with row and col specified
        """
        if row < 1 or row > 3 or col < 1 or col > 3:
            raise IndexError
        return self.board[row - 1][col - 1]

    def __str__(self):
        out = '-' * 9 + '\n'
        for row in range(TicTacToe.BOARD_SIZE):
            out += '| '
            for col in range(TicTacToe.BOARD_SIZE):
                out += self.board[row][col] + ' '
            out += '|\n'
        out += '-' * 9
        return out

    def __repr__(self):
        out = ''
        for row in range(TicTacToe.BOARD_SIZE):
            for col in range(TicTacToe.BOARD_SIZE):
                out += self.board[row][col]
        return out

    @staticmethod
    def make_movement(row, col, player):
        try:
            row, col = int(row), int(col)
            while row > 3 or row < 1 or col > 3 or col < 1:
                print('Coordinates should be from 1 to 3!')
                row, col = input('Enter the coordinates: ').split()
                row, col = int(row), int(col)
            # Keep asking until '_'
            while tic_tac_toe.get_board_cell(row, col) != '_' and \
                    (1 <= row <= 3 and 1 <= col <= 3):
                print('This cell is occupied! Choose another one!')
                row, col = input('Enter the coordinates: ').split()
                row, col = int(row), int(col)

                if row > 3 or row < 1 or col > 3 or col < 1:
                    print('Coordinates should be from 1 to 3!')
                if type(row) is not int or type(col) is not int:
                    print('You should enter numbers!')
        except IndexError:
            print('Coordinates should be from 1 to 3!')
        # Make the valid move
        tic_tac_toe.set_value_in_cell(row, col, player)


if __name__ == '__main__':
    # Output the initial game board
    tic_tac_toe = TicTacToe('')
    print(tic_tac_toe)
    player = 'X'
    while (not tic_tac_toe.has_won('X') and not tic_tac_toe.has_won('O')) \
            and not tic_tac_toe.is_draw():
        # Ask user to enter a move
        row, col = input('Enter the coordinates: ').split()
        tic_tac_toe.make_movement(row, col, player)
        # We show the board
        print(tic_tac_toe)
        # We toggle the player
        player = 'O' if player == 'X' else 'X'

    print(tic_tac_toe.get_status())
