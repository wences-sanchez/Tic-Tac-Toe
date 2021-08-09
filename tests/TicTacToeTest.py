import unittest

from parameterized import parameterized
from src.core.TicTacToe import TicTacToe


class TicTacToeTest(unittest.TestCase):
    def test_given_empty_build_default_board(self):
        tic_tac_toe = TicTacToe('')

        expected_board = [['_' * 3] * 3]

        self.assertListEqual(expected_board, tic_tac_toe.get_board())

    def test_given_specified_input_then_build_board(self):
        tic_tac_toe = TicTacToe('XXXXXXXXX')

        expected_board = [list('XXX')] * 3
        self.assertListEqual(expected_board, tic_tac_toe.get_board())

        tic_tac_toe = TicTacToe('XO_X__OX_')
        expected_board = [['X', 'O', '_'], ['X', '_', '_'], ['O', 'X', '_']]
        self.assertListEqual(expected_board, tic_tac_toe.get_board())

        tic_tac_toe = TicTacToe('_X_O__OXX')
        expected_board = [['_', 'X', '_'], ['O', '_', '_'], ['O', 'X', 'X']]
        self.assertListEqual(expected_board, tic_tac_toe.get_board())

    @parameterized.expand([
        ('XXXO_O__O', 'X', True),  # Upper row
        ('O__XXX_OO', 'X', True),  # Central row
        ('O_O__OXXX', 'X', True),  # Bottom row
        ('XO_XO_X_O', 'X', True),  # Left column
        ('XOX_O__OX', 'O', True),  # Central column
        ('X_O_XOX_O', 'O', True),  # Right column
        ('XOX_XO_OX', 'X', True),  # Main diagonal
        ('_XO_OXO_X', 'O', True),  # Second diagonal
        ('XXXO_O__O', 'O', False),
        ('O_O__OXXX', 'O', False),
        ('XOX_O__OX', 'X', False),
        ('XOX_XO_OX', 'O', False),
        ('_XO_OXO_X', 'X', False),
    ])
    def test_given_board_should_tell_if_player_won(self, board, player, expected):
        tic_tac_toe = TicTacToe(board)
        self.assertEqual(expected, tic_tac_toe.has_won(player))

    @parameterized.expand([
        ('XXOOXXXOO', True),
        ('OXOXXOXOX', True),
        ('XOX_XO_OX', False),
        ('_XO_OXO_X', False),
        ('_OO_OXX_X', False),
    ])
    def test_given_board_should_return_whether_is_a_draw(self, board, expected):
        tic_tac_toe = TicTacToe(board)
        self.assertEqual(expected, tic_tac_toe.is_draw())

    @parameterized.expand([
        ('XXXOOOXOX', True),  # Both player won (impossible)
        ('XOOOOXXOO', True),  # Much more slots of one player (impossible)
        ('OXOOXOXOX', False),  # A not impossible game board
        ('_________', False),  # Another not impossible (empty) game board
        ('XXXO_O__O', False),
    ])
    def test_given_board_should_return_whether_is_impossible(self, board, expected):
        tic_tac_toe = TicTacToe(board)
        self.assertEqual(expected, tic_tac_toe.is_impossible())


if __name__ == '__main__':
    unittest.main()
