class MinMax:
    """Class for minimax-algorithm with alpha-beta-pruning
    """

    @staticmethod
    def find_optimal(position, depth, alpha, beta, ai_player):
        """Calculates the optimal moves for given depth and for each player in each position provided that 
        also human player makes the optimal moves

        Args:
            position (list): 2D-array presentation of the gameboard position
            depth (int): Describes the highest depth algorithm is going for to look for best moves
            alpha (int): Value for alpha-used in alpha-beta-pruning
            beta (int): Value for beta used in alpha-beta-pruning
            ai_player (boolean): Informs which player makes the next move

        Returns:
            int: Depending on the player whose turn it is, it either 
            returns minimum evaluation value for the node during human players turn or
            it return the maximum evaluation value for the node if it is ai-opponents turn
        """
        if depth == 0 or game_end in position:
            return state_evaluation

        if ai_player:
            maxEval = float("-inf")
            for child in position:
                eval = find_optimal(child, depth - 1, alpha, beta, false)
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return maxEval
        
        else:
            minEval = float("+inf")
            for child in position:
                eval = find_optimal(child, depth - 1, alpha, beta, true)
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return minEval

    @staticmethod
    def evaluate():
        '''Gives a node an integer value based on how good 
        the board position is in the state that the evaluate-function is used on

        '''
        pass

