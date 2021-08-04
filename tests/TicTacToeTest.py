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
        ('XXXO_O__O', 'X', True),
        ('O_O__OXXX', 'X', True),
        ('XOX_O__OX', 'O', True),
        ('XOX_XO_OX', 'X', True),
        ('_XO_OXO_X', 'O', True),
        ('XXXO_O__O', 'O', False),
        ('O_O__OXXX', 'O', False),
        ('XOX_O__OX', 'X', False),
        ('XOX_XO_OX', 'O', False),
        ('_XO_OXO_X', 'X', False),
    ])
    def test_player_won(self, board, player, expected):
        tic_tac_toe = TicTacToe(board)
        self.assertEqual(expected, tic_tac_toe.has_won(player))

    def test_game_is_draw(self):
        tic_tac_toe = TicTacToe('XXOOXXXOO')
        self.assertTrue(tic_tac_toe.is_draw())

    def test_game_is_impossible(self):
        tic_tac_toe = TicTacToe('XXXOOOXOX')
        self.assertTrue(tic_tac_toe.is_impossible())


if __name__ == '__main__':
    unittest.main()
