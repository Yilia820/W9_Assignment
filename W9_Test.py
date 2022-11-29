import unittest
import W9_Logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(W9_Logic.get_winner(board), 'X')

    def test_get_winner_board1(self):
        board = [
            ['O', None, 'X'],
            [None, 'O', None],
            ['X', 'O', 'X'],
        ]
        self.assertEqual(W9_Logic.get_winner(board), None)
    
    def test_get_winner_board2(self):
        board = [
            ['O', None, 'X'],
            ['O', None, None],
            ['O', 'O', 'X'],
        ]
        self.assertEqual(W9_Logic.get_winner(board), 'O')

    def test_other_player(self):
        self.assertEqual(W9_Logic.other_player('O'),'X')

    # TODO: Test all functions from logic.py!


if __name__ == '__main__':
    unittest.main()