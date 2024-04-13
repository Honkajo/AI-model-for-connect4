import unittest
from game import Connect4

class TestConnect4(unittest.TestCase):

    def setUp(self):
        self.game = Connect4()

    def test_initial_board(self):
        expected_board = [[0]*7 for _ in range(6)]
        self.assertEqual(self.game.board, expected_board)

    def test_make_move(self):
        self.game.make_move(1, "ai")  
        self.assertEqual(self.game.board[5][0], 1)

    def test_check_win_conditions(self):
        self.game.board[5] = [1, 1, 1, 1, 0, 0, 0]
        self.assertTrue(self.game.check_horizontal_win())
        
        for i in range(4):
            self.game.board[i][0] = 2
        self.assertTrue(self.game.check_vertical_win())

        for i in range(4):
            self.game.board[5-i][i] = 1
        self.assertTrue(self.game.check_diagonal_win())

    def test_game_over(self):
        self.assertFalse(self.game.is_game_over())
        self.game.board[5] = [1, 1, 1, 1, 0, 0, 0]
        self.assertTrue(self.game.is_game_over())

    

    
        



