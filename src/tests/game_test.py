import unittest
import time
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

    def test_get_next_open_row(self):
        self.game.board[5][0] = 1
        self.game.board[4][0] = 1
        expected_row = 3
        self.assertEqual(self.game.get_next_open_row(0), expected_row)

    def test_is_valid_move(self):
        for i in range(7):
            self.assertTrue(self.game.is_valid_move(i))
        for j in range(6):
            self.game.board[j][0] = 1
        self.assertFalse(self.game.is_valid_move(0))

    def test_minmax(self):
        self.game.board[5][0] = 2
        self.game.board[5][1] = 2
        self.game.board[5][2] = 2
        _, score = self.game.minmax(1, float('-inf'), float('inf'), True)
        self.assertEqual(score, 50000)

    def test_evaluate_position(self):
        self.game.board[5][0] = 1
        self.game.board[5][1] = 1
        self.game.board[5][2] = 1
        self.game.board[5][3] = 0
        self.assertGreater(self.game.evaluate_position(), 0)

    def test_detect_immediate_threats(self):
        self.game.board[5][0] = 2
        self.game.board[5][1] = 2
        self.game.board[5][2] = 2
        self.game.board[5][3] = 0
        threats = self.game.detect_immediate_threats()
        self.assertEqual(threats[2], 50000)

    def test_preferred_column_order(self):
        expected_order = [3, 2, 4, 1, 5, 0, 6]
        self.assertEqual(self.game.preferred_cols, expected_order)

    def test_minmax_decision_making(self):
        self.game.board[5][3] = 1
        self.game.board[5][4] = 1
        self.game.board[5][5] = 1
        best_col, _ = self.game.minmax(1, float('-inf'), float('inf'), True)
        self.assertEqual(best_col, 6)

    def test_ai_move_full_column(self):
        for i in range(6):
            self.game.board[i][3] = 1
        self.assertFalse(self.game.is_valid_move(4))
        _, chosen_col = self.game.minmax(1, float('inf'), float('inf'), True)
        self.assertNotEqual(chosen_col, 4)

    def test_minmax_performance(self):
        start_time = time_time()
        _, _ = self.game.minmax(3, float('-inf'), float('inf'), True)
        duration = time.time() - start_time
        self.assertLess(duration, 2)

    def test_diagonal_edge_case(self):
        self.game.board[2][0] = 2
        self.game.board[3][1] = 2
        self.game.board[4][2] = 2
        self.game.board[5][3] = 2
        self.assertTrue(self.game.check_diagonal_win())
        







    

    
        



