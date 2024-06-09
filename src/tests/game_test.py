import unittest
from game import (minimax, iterative_deepening, full_board, is_valid_move, make_move, get_next_open_row, 
                  evaluate_position, valid_moves, is_game_over)

class TestGame(unittest.TestCase):

    def test_minimax(self):
        """
        Test minimax function
        """
        player_piece = 1
        ai_piece = 2
        depth = 3
        alpha = float("-inf")
        beta = float("inf")
        max_player = True
        
        board = [
            [2, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1],
            [1, 1, 2, 1, 2, 1, 2],
            [2, 1, 1, 2, 2, 1, 2],
            [2, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 1, 2]
        ]
        self.assertEqual(minimax(board, depth, alpha, beta, max_player, 
                                 player_piece, ai_piece, hash_map={}), (None, 0))
        board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [2, 2, 2, 0, 1, 1, 1]
        ]
        self.assertEqual(minimax(board, depth, alpha, beta, max_player, 
                                 player_piece, ai_piece, hash_map={}), (3, 1000))
        board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 2],
            [0, 1, 0, 0, 0, 0, 2]
        ]
        self.assertEqual(minimax(board, depth, alpha, beta, max_player, 
                                 player_piece, ai_piece, hash_map={}), (1, 2))
        
    def test_iterative_deepening(self):
        """
        Test iterative_deepening function
        """
        #Test to show that ai starts at the middle column
        player_piece = 1
        ai_piece = 2
        board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        alpha = float("-inf")
        beta = float("inf")
        max_player = True
        time_limit = 5
        self.assertEqual(iterative_deepening(board, alpha, beta, max_player, time_limit, player_piece, ai_piece), 3)

        #Start of board situation where Ai is 5 moves from winning

        board = [
            [0, 2, 0, 1, 2, 1, 0],
            [0, 1, 0, 2, 2, 2, 0],
            [0, 2, 0, 1, 1, 2, 0],
            [1, 1, 2, 2, 1, 1, 0],
            [2, 2, 1, 1, 2, 2, 1],
            [1, 1, 1, 2, 2, 1, 2]
        ]

        #Ai winning in 5 moves 
        #Ai move to column 6
        #player move to column 0
        
        self.assertEqual(iterative_deepening(board, alpha, beta, max_player, time_limit, player_piece, ai_piece), 6)

        board = [
            [0, 2, 0, 1, 2, 1, 0],
            [0, 1, 0, 2, 2, 2, 0],
            [1, 2, 0, 1, 1, 2, 0],
            [1, 1, 2, 2, 1, 1, 2],
            [2, 2, 1, 1, 2, 2, 1],
            [1, 1, 1, 2, 2, 1, 2]
        ]

        #Ai winning in 4 moves 
        #Ai move to column 0
        #player move to column 0
        self.assertEqual(iterative_deepening(board, alpha, beta, max_player, time_limit, player_piece, ai_piece), 0)
        
        board = [
            [1, 2, 0, 1, 2, 1, 0],
            [2, 1, 0, 2, 2, 2, 0],
            [1, 2, 0, 1, 1, 2, 0],
            [1, 1, 2, 2, 1, 1, 2],
            [2, 2, 1, 1, 2, 2, 1],
            [1, 1, 1, 2, 2, 1, 2]
        ]

        #Ai winning in 3 moves 
        #Ai move to column 2
        #player move to column 2
        
        self.assertEqual(iterative_deepening(board, alpha, beta, max_player, time_limit, player_piece, ai_piece), 2)
        
        board = [
            [1, 2, 0, 1, 2, 1, 0],
            [2, 1, 1, 2, 2, 2, 0],
            [1, 2, 2, 1, 1, 2, 0],
            [1, 1, 2, 2, 1, 1, 2],
            [2, 2, 1, 1, 2, 2, 1],
            [1, 1, 1, 2, 2, 1, 2]
        ]

        #Ai winning in 2 moves 
        #Ai move to column 2
        #player move to column 6
        
        self.assertEqual(iterative_deepening(board, alpha, beta, max_player, time_limit, player_piece, ai_piece), 2)
        
        board = [
            [1, 2, 2, 1, 2, 1, 0],
            [2, 1, 1, 2, 2, 2, 0],
            [1, 2, 2, 1, 1, 2, 1],
            [1, 1, 2, 2, 1, 1, 2],
            [2, 2, 1, 1, 2, 2, 1],
            [1, 1, 1, 2, 2, 1, 2]
        ]

        #Ai winning move 
        #Move to column 6
        self.assertEqual(iterative_deepening(board, alpha, beta, max_player, time_limit, player_piece, ai_piece), 6)

    def test_full_board(self):
        """Test that checks that the board is full
        """
        board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertFalse(full_board(board))
        for col in range(7):
            board[0][col] = 1
        self.assertTrue(full_board(board))

    def test_is_valid_move(self):
        """Test to show that move made into certain column is valid or not valid
        """
        board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertTrue(is_valid_move(board, 0))
        board[0][0] = 1
        self.assertFalse(is_valid_move(board, 0))

    def test_make_move(self):
        """Test to see if piece was placed to the right place after make_move function
        """
        board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        make_move(board, 5, 0, 1)
        self.assertEqual(board[5][0], 1)
        make_move(board, 4, 0, 2)
        self.assertEqual(board[4][0], 2)

    def test_get_next_open_row(self):
        """Test to see if piece was placed correctly to the lowest free spot on the column
        """
        board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(get_next_open_row(board, 0), 5)
        make_move(board, 5, 0, 1)
        self.assertEqual(get_next_open_row(board, 0), 4)

    def test_evaluate_position(self):
        """Checks that the value of board state is calculated correctly
        """
        board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 2, 2, 2, 0]
        ]
        score = evaluate_position(board, 1, 1, 2)
        self.assertEqual(score, 2)
        make_move(board, 5, 6, 1)
        score = evaluate_position(board, 1, 1, 2)
        self.assertEqual(score, 8)

    def test_valid_moves(self):
        """Checks that the list of valid moves is updated correctly
        """
        board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 2, 2, 2, 0]
        ]
        self.assertEqual(valid_moves(board), [3, 2, 4, 1, 5, 0, 6])
        make_move(board, 0, 3, 2)
        self.assertEqual(valid_moves(board), [2, 4, 1, 5, 0, 6])

    def is_game_over(self):
        """Checks winning conditions
        """
        #Test vertical win
        board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0]
        ]
        self.assertTrue(is_game_over(board, 3))
        #Test horizontal win
        board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 2, 2, 2, 0, 0, 0]
        ]
        self.assertTrue(is_game_over(board, 0))
        #Test diagonal win
        board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertTrue(is_game_over(board, 0))
        #Test should return False when there is no last move
        board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertFalse(is_game_over(board, None))