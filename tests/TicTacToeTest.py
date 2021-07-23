import unittest

from src.core.TicTacToe import TicTacToe


class TicTacToeTest(unittest.TestCase):
    def test_table_is_shown(self):
        tic_tac_toe = TicTacToe()

        expected_table = [['X', 'O', 'X'],
                          ['O', 'O', 'X'],
                          ['X', 'X', 'O']]
        self.assertListEqual(expected_table, tic_tac_toe.get_table())


if __name__ == '__main__':
    unittest.main()
