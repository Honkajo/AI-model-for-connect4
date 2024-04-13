import random

class Connect4:
    """Class that creates a game of connect4
    """

    def __init__(self):
        """Initializes the start of the game
        """
        self.board = [[0, 0, 0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]]
        
        self.preferred_cols = [3, 2, 4, 1, 5, 0, 6]
        self.starting_player = None

    def get_next_open_row(self, col):
        """Used in minmax-function to find the next open row when evaluating next moves for ai

        Args:
            col (int): Column that is spesified to check from which row of the spesified column is open

        Returns:
            Row that is not full yet or if there are no free rows in that column, then it returns None
        """
        for row in range(6):
            if self.board[row][col] == 0:
                return row
        return None

    def minmax(self, depth, alpha, beta, maximizingPlayer):
        """Main algorithm that calculates the best moves for ai

        Args:
            depth (int): Spesifies the depth on which the algorithm calculates next moves
            alpha (float): Alpha-value for minmax algorithm
            beta (float): beta value for minmax-algorithm
            maximizingPlayer (boolean): Shows if it is ai-players turn or not

        Returns:
            Integer: returns best column for the move and max or min evaluation
        """
        valid_moves = [col for col in self.preferred_cols if self.is_valid_move(col)]
        if depth == 0 or self.is_game_over() or not valid_moves:
            return None, self.evaluate_position()
        
        if maximizingPlayer:
            max_eval = float('-inf')
            best_col = None
            for col in valid_moves:
                if self.is_valid_move(col):
                    row = self.get_next_open_row(col)
                    self.board[row][col] = 1
                    _, eval = self.minmax(depth-1, alpha, beta, False)
                    self.board[row][col] = 0
                    if eval > max_eval:
                        max_eval = eval
                        best_col = col
                    alpha = max(alpha, eval)
                    if alpha >= beta:
                        break
            return best_col, max_eval
        
        else:
            min_eval = float('inf')
            best_col = None
            for col in valid_moves:
                if self.is_valid_move(col):
                    row = self.get_next_open_row(col)
                    self.board[row][col] = 2
                    _, eval = self.minmax(depth-1, alpha, beta, True)
                    self.board[row][col] = 0
                    if eval < min_eval:
                        min_eval = eval
                        best_col = col
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return best_col, min_eval
        

    
    def print_board(self):
        """Prints the gameboard
        """
        for row in self.board:
            print(' '.join(str(cell) for cell in row))
        print("\n")
        
    def start_game(self):
        """Starts the game loop
        """
        
        self.print_board()
    
        players = ["ai", "human"]
        self.starting_player = random.choice(players)
        current_turn = self.starting_player
        print(f"Starting player: {self.starting_player}")
        
        while True:
            if self.is_game_over():
                if current_turn == "human":
                    print("Game over!")
                    print("You lose!")
                else:
                    print("Game over!")
                    print("You win!")

                break
            if current_turn == "ai":
                chosen_col, _ = self.minmax(3, float('-inf'), float('inf'), True)
                self.make_move(chosen_col + 1, "ai")
                print("AI has made its move:")
                self.print_board()
                current_turn = "human"

            else:
                try:
                    chosen_col = int(input(f"Choose your move(1-7):  "))
                    if self.is_valid_move(chosen_col - 1):
                        self.make_move(chosen_col, "human")
                        print("You made your move:")
                        self.print_board()
                        current_turn = "ai"
                    else:
                        print("Invalid move. Try again!")
                except ValueError:
                    print("Please enter a number between 1 and 7")

    def ai_move(self):
        """Used to make a random move for the ai-player
        """
        valid_move = False
        while not valid_move:
            chosen_col = random.randint(1, 7)
            if self.is_valid_move(chosen_col - 1):
                valid_move = True
        self.make_move(chosen_col, "ai")

    def is_valid_move(self, col):
        """Checks if move for the column is possible to make

        Args:
            col (int): Column number where to make a move

        Returns:
            Boolean: tells if move is possible or not
        """
        return self.board[0][col] == 0



    def make_move(self, col, player):
        """Function for making a move in Connect4
        """
        col -= 1
        for i in range(5, -1, -1):
            if self.board[i][col] == 0:
                 self.board[i][col] = 1 if player == "ai" else 2
                 break
            
    def check_horizontal_win(self):
        """Checks if a player has a winning position in horizontal direction

        Returns:
            Boolean: Either it is a win position or it is not
        """
        for row in self.board:
            for col in range(4):
                if row[col] == row[col + 1] == row[col +2] == row[col + 3] != 0:
                    return True
        return False
    def check_vertical_win(self):
        """Checks if a player has a winning position in vertical direction

        Returns:
            Boolean: Either it is a win position or it is not
        """
        for col in range(7):
            for row in range(3):
                if self.board[row][col] == self.board[row + 1][col] == self.board[row + 2][col] == self.board[row + 3][col] != 0:
                    return True
        return False
    
    def check_diagonal_win(self):
        """Checks if a player has a winning position in diagonal direction

        Returns:
            Boolean: Either it is a win position or it is not
        """
        for row in range(3, 6):
            for col in range(4):
                if self.board[row][col] == self.board[row - 1][col + 1] == self.board[row - 2][col + 2] == self.board[row - 3][col + 3] != 0:
                    return True
                
        for row in range(3, 6):
            for col in range(3, 7):
                if self.board[row][col] == self.board[row - 1][col - 1] == self.board[row - 2][col - 2] == self.board[row - 3][col - 3] != 0:
                    return True
                
    def is_game_over(self):
        """Checks if a game is over

        Returns:
            Boolean: Either it is true or not
        """
        if self.check_horizontal_win() or self.check_vertical_win() or self.check_diagonal_win():
            return True
        count = sum(cell != 0 for row in self.board for cell in row)
        if count == 42:
            return True
        return False

    def remove_ai_move(self, col):
        """Used to remove ai move when generating all possible moves for algorithm to choose from

        Args:
            col (int): Column number
        """
        col -= 1
        for i in range(6):
            if self.board[i][col] == 1:
                self.board[i][col] = 0
                break
    
    def horizontal_score(self):
        """Calculates chains of 2 or more same player tokens in horizontal direction

        Returns:
            Dictionary: Shows scores for 1s and 2s in the dictionary-form
        """
        scores = {1: 0, 2: 0}
        for row in self.board:
            current = 0
            count = 0
            for cell in row:
                if cell == current and cell != 0:
                    count += 1
                else:
                    if count >= 4:
                        scores[current] += 1000
                    elif count >= 2:
                        scores[current] += count
                    current = cell
                    count = 1
            if count >= 4:
                scores[current] += 1000
            elif count >= 2:
                scores[current] += count
        return scores
    
    def vertical_score(self):
        """Calculates chains of 2 or more same player tokens in vertical direction

        Returns:
            Dictionary: Shows scores for 1s and 2s in the dictionary-form
        """
        scores = {1: 0, 2: 0}
        for col in range(7):
            current = 0
            count = 0
            for row in range(6):
                cell = self.board[row][col]
                if cell == current and cell != 0:
                    count += 1
                else:
                    if count >= 4:
                        scores[current] += 1000
                    elif count >= 2:
                        scores[current] += count
                    current = cell
                    count = 1
            if count >= 4:
                scores[current] += 1000
            elif count >= 2:
                scores[current] += count
        return scores
    
    def evaluate_position(self):
        """Calculates horizontal and vertical scores together into dictionary keys for 1 and 2 and then substacts the score of player 2(human player) from score of player 1(ai player)
        to get the evaluation for the board position
        Returns:
            Integer: Shows value for the evaluated board position
        """
        horizontal_scores = self.horizontal_score()
        vertical_scores = self.vertical_score()

        combined_scores = {1: horizontal_scores[1] + vertical_scores[1], 2: horizontal_scores[2] + vertical_scores[2]}
        score_difference = combined_scores[1] - combined_scores[2]
        return score_difference



"""
    def diagonal_score(self):
        scores = {1: 0, 2: 0}
        handled_positive = set()
        handled_negative = set()

        def process_chain(cells, player, handled):
            if len(cells) >= 4:
                scores[player] += 1000
            elif len(cells) >= 2:
                scores[player] += len(cells)
            handled.update(cells)
        
        for row in range(6):
            print(scores)
            for col in range(7):
                current_player = self.board[row][col]
                if current_player != 0:

                    positive_slope = []
                    r, c = row, col
                    while r >= 0 and c < 7:
                        if self.board[r][c] == current_player and (r, c) not in handled_positive:
                            positive_slope.append((r, c))
                            r -= 1
                            c += 1
                        else:
                            break
                    if len(positive_slope) >= 2:
                        process_chain(positive_slope, current_player, handled_positive)


                    negative_slope = []
                    r, c = row, col
                    while r < 6 and c < 7:
                        if self.board[r][c] == current_player and (r, c) not in handled_negative:
                            negative_slope.append((r, c))
                            r += 1
                            c += 1
                        else:
                            break
                    if len(negative_slope) >= 2:
                        process_chain(negative_slope, current_player, handled_negative)

        return scores
"""



if __name__ =="__main__":
    game = Connect4()
    game.start_game()
















