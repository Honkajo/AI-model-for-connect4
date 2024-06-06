import unittest
from game import minimax, iterative_deepening

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