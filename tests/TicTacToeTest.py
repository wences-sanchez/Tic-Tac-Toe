import unittest

from parameterized import parameterized
from src.core.TicTacToe import TicTacToe


class TicTacToeTest(unittest.TestCase):
    def setUp(self):
        self.tic_tac_toe = TicTacToe('')

    def test_given_empty_build_default_board(self):
        tic_tac_toe = TicTacToe('')

        expected_board = [list('___')] * 3

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
    def test_given_board_should_tell_if_player_won(self, board, player,
                                                   expected):
        tic_tac_toe = TicTacToe(board)
        self.assertEqual(expected, tic_tac_toe.has_won(player))

    @parameterized.expand([
        ('XXOOXXXOO', True),
        ('OXOXXOXOX', True),
        ('XOX_XO_OX', False),
        ('_XO_OXO_X', False),
        ('_OO_OXX_X', False),
    ])
    def test_given_board_should_return_whether_is_a_draw(self, board,
                                                         expected):
        tic_tac_toe = TicTacToe(board)
        self.assertEqual(expected, tic_tac_toe.is_draw())

    @parameterized.expand([
        ('XXXOOOXOX', True),  # Both player won (impossible)
        ('XOOOOXXOO', True),  # Much more slots of one player (impossible)
        ('OXOOXOXOX', False),  # A not impossible game board
        ('_________', False),  # Another not impossible (empty) game board
        ('XXXO_O__O', False),
    ])
    def test_given_board_should_return_whether_is_impossible(self, board,
                                                             expected):
        tic_tac_toe = TicTacToe(board)
        self.assertEqual(expected, tic_tac_toe.is_impossible())

    @parameterized.expand([
        ('XXXO_O__O', 1, 1, 'X'),
        ('O__XXX_OO', 3, 2, 'O'),
        ('X_XO__O_O', 2, 3, '_'),
    ])
    def test_indexes_when_right_bounded(self, board, row, col, expected):
        tic_tac_toe = TicTacToe(board)
        self.assertEqual(expected,
                         tic_tac_toe.get_board()[row - 1][col - 1])

    @parameterized.expand([
        ('O_O__OXXX', 0, 1),
        ('XO_XO_X_O', -1, 1),
        ('XOX_O__OX', 4, 1),
        ('X_O_XOX_O', 3, 0),
        ('XOX_XO_OX', 3, -1),
        ('_XO_OXO_X', 3, 4),
    ])
    def test_indexes_when_out_of_bound(self, board, row, col):
        tic_tac_toe = TicTacToe(board)
        self.assertRaises(IndexError,
                          tic_tac_toe.set_value_in_cell, row, col, 'X'
                          )
        self.assertRaises(IndexError,
                          tic_tac_toe.get_board_cell, row, col
                          )

    def test_indexes_when_not_numbers(self):
        tic_tac_toe = TicTacToe('__O_X__OX')
        self.assertRaises(ValueError,
                          tic_tac_toe.set_value_in_cell, 'a', 1, 'O')
        self.assertRaises(ValueError,
                          tic_tac_toe.set_value_in_cell, 1, '_', 'X')
        self.assertRaises(ValueError,
                          tic_tac_toe.set_value_in_cell, 2, '', 'X')

    def test_whether_cell_is_filled(self):
        tic_tac_toe = TicTacToe('X_O_XOX_O')
        self.assertFalse(tic_tac_toe.is_empty_cell(3, 3))
        self.assertTrue(tic_tac_toe.is_empty_cell(1, 2))

    def test_set_value_in_board_cell(self):
        tic_tac_toe = TicTacToe('X_O_XOX_O')
        tic_tac_toe.set_value_in_cell(3, 2, 'X')
        self.assertEqual('X', tic_tac_toe.get_board_cell(3, 2))

        tic_tac_toe.set_value_in_cell(1, 2, 'O')
        self.assertEqual('O', tic_tac_toe.get_board_cell(1, 2))


if __name__ == '__main__':
    unittest.main()
