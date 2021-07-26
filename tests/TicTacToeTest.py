import unittest

from src.core.TicTacToe import TicTacToe


class TicTacToeTest(unittest.TestCase):
    def test_given_empty_build_default_board(self):
        tic_tac_toe = TicTacToe('')

        expected_board = [['_' * 3] * 3]

        self.assertListEqual(expected_board, tic_tac_toe.get_board())

    def test_specified_input(self):
        tic_tac_toe = TicTacToe('XXXXXXXXX')

        expected_board = [list('XXX')] * 3
        self.assertListEqual(expected_board, tic_tac_toe.get_board())

        tic_tac_toe = TicTacToe('XO_X__OX_')
        expected_board = [['X', 'O', '_'], ['X', '_', '_'], ['O', 'X', '_']]
        self.assertListEqual(expected_board, tic_tac_toe.get_board())

        tic_tac_toe = TicTacToe('_X_O__OXX')
        expected_board = [['_', 'X', '_'], ['O', '_', '_'], ['O', 'X', 'X']]
        self.assertListEqual(expected_board, tic_tac_toe.get_board())


if __name__ == '__main__':
    unittest.main()
