import random
import time

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
        self.hash_table = {}
        self.move_scores = {}                              

    def start_game(self):
        """Starts the game loop
        """
        self.print_board()
    
        players = ["ai", "human"]
        current_turn = random.choice(players)
        last_move = None
        
        print(f"Starting player: {current_turn}")
        
        while True:
            if self.is_game_over(last_move):
                if current_turn == "human":
                    print("Game over!")
                    print("You lose!")
                else:
                    print("Game over!")
                    print("You win!")
                break
            elif self.full_board():
                print("It's a draw!")
                break           
            
            if current_turn == "ai":
                chosen_col, _ = self.iterative_deepening(5, last_move)
                last_move = self.make_move(chosen_col + 1, "ai")
                print("AI has made its move:")
                print()
                self.print_board()
                current_turn = "human"
                for i in range(5):
                    if self.board[i][chosen_col] != 0:
                        last_move = [i, chosen_col]
                        break

            else:
                try:
                    chosen_col = int(input(f"Choose your move(1-7):  "))
                    if self.is_valid_move(chosen_col - 1) and chosen_col >= 1 and chosen_col <= 7:
                        last_move = self.make_move(chosen_col, "human")
                        print("You made your move:")
                        self.print_board()
                        current_turn = "ai"
                        for i in range(5):
                            if self.board[i][chosen_col] != 0:
                                last_move = [i, chosen_col]
                                break
                    else:
                        print("Invalid move. Try again!")
                except IndexError:
                    print("Please enter a number between 1 and 7")
                except ValueError:
                    print("Please enter a number between 1 and 7")
            

    def print_board(self):
        """Prints the gameboard
        """
        print("1 2 3 4 5 6 7")
        print("-------------")
        for row in self.board:
            print(' '.join(str(cell) for cell in row))
        print("\n")

    def full_board(self):
        for col in range(7):
            if self.board[0][col] == 0:
                return False
        return True

    
    
    def iterative_deepening(self, time_limit, move):
        """Calculates best moves until time limit or maximum depth is reached

        Args:
            time_limit (int): Maximum time for algorithm calculation

        Returns:
            int: Best column for the next move and evaluation score for that move
        """
        best_col = None
        best_eval = float('-inf')
        start_time = time.time()

        depth = 3

        while True: 
            if time.time() - start_time >= time_limit:
                break
            current_col, current_eval = self.minmax(depth, float('-inf'), float('inf'), True, move)
            if current_eval > best_eval:
                best_eval = current_eval
                best_col = current_col
                self.move_scores[best_col] = best_eval
            depth += 1
        
        return best_col, best_eval
    
        
    def minmax(self, depth, alpha, beta, maximizingPlayer, move):
        """Main algorithm that calculates the best moves for ai

        Args:
            depth (int): Spesifies the depth on which the algorithm calculates next moves
            alpha (float): Alpha-value for minmax algorithm
            beta (float): beta value for minmax-algorithm
            maximizingPlayer (boolean): Shows if it is ai-players turn or not

        Returns:
            Integer: returns best column for the move and max or min evaluation
        """
        last_move = move
        board_key = self.hash_board()
        if board_key in self.hash_table:
            return self.hash_table[board_key]

        valid_moves = self.sort_moves([col for col in self.preferred_cols if self.is_valid_move(col)])
        if depth == 0 or self.is_game_over(last_move) or not valid_moves:
            evaluation = self.evaluate_position()
            return None, evaluation
        
        if maximizingPlayer:
            max_eval = float('-inf')
            best_col = None
            for col in valid_moves:
                if self.is_valid_move(col):
                    row = self.get_next_open_row(col)
                    self.board[row][col] = 1
                    _, eval = self.minmax(depth-1, alpha, beta, False, last_move)
                    self.board[row][col] = 0
                    if eval > max_eval:
                        max_eval = eval
                        best_col = col
                    alpha = max(alpha, eval)
                    if alpha >= beta:
                        break
            self.hash_table[board_key] = (best_col, max_eval)
            return best_col, max_eval
        
        else:
            min_eval = float('inf')
            best_col = None
            for col in valid_moves:
                if self.is_valid_move(col):
                    row = self.get_next_open_row(col)
                    self.board[row][col] = 2
                    _, eval = self.minmax(depth-1, alpha, beta, True, last_move)
                    self.board[row][col] = 0
                    if eval < min_eval:
                        min_eval = eval
                        best_col = col
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            self.hash_table[board_key] = (best_col, min_eval)
            return best_col, min_eval
    
    def is_game_over(self, move):
        """Checks if a game is over

        Returns:
            Boolean: Either it is true or not
        """
        if move is None:
            return False
        x, y = move
        token = self.board[x][y]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (1, -1), (-1, 1)]

        for dx, dy in directions:
            count = 1

            nx, ny = x + dx, y + dy
            while 0 <= nx < 6 and 0 <= ny < 7 and self.board[nx][ny] == token:
                count += 1
                nx += dx
                ny += dy
                if count >= 4:
                    return True
            
            nx, ny = x - dx, y - dy
            while 0 <= nx < 6 and 0 <= ny < 7 and self.board[nx][ny] == token:
                count += 1
                nx -= dx
                ny -= dy
                if count >= 4:
                    return True

            if count < 4:
                count = 1
        
        return False

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
                 return (i, col)
                 
        
    def get_next_open_row(self, col):
        """Used in minmax-function to find the next open row when evaluating next moves for ai

        Args:
            col (int): Column that is spesified to check from which row of the spesified column is open

        Returns:
            Row that is not full yet or if there are no free rows in that column, then it returns None
        """
        for row in range(5, -1, -1):
            if self.board[row][col] == 0:
                return row
        return None
    
    def sort_moves(self, moves):
        """Sorts moves based on board evaluation scores after the move is done. These moves are sorted out so that the highest value evaluation score for the board after 
        the move is done is prioritized

        Args:
            moves (list): list of different valid moves

        Returns:
            list: sorted and reversed list based on board evaluation values
        """
        return sorted(moves, key=lambda col: self.move_scores.get(col, 0), reverse=True)
    
    def hash_board(self):
        """String form of board state

        Returns:
            String: board state as a string form
        """
        return str(self.board)
            
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
        return False
    
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
                    elif count == 3:
                        scores[current] += 100
                    elif count == 2:
                        scores[current] += 10
                    current = cell
                    count = 1
            if count >= 4:
                scores[current] += 1000
            elif count == 3:
                scores[current] += 100
            elif count == 2:
                scores[current] += 10
        
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
                    elif count == 3:
                        scores[current] += 100
                    elif count == 2:
                        scores[current] += 10
                    
                    current = cell
                    count = 1
            if count >= 4:
                scores[current] += 1000
            elif count == 3:
                scores[current] += 100
            elif count == 2:
                scores[current] += 10
            
        return scores
    
    def diagonal_score(self):
        """Calculates scores by chains of same tokens for both players in current board state
        """

        scores = {1: 0, 2: 0}
        handled_positive = set()
        handled_negative = set()

        def process_chain(cells, player, handled):
            if len(cells) >= 4:
                scores[player] += 1000
            elif len(cells) == 3:
                scores[player] += 100
            elif len(cells) == 2:
                scores[player] += 10
            handled.update(cells)
        
        for row in reversed(range(6)):
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
                            r -= 1
                            c -= 1
                        else:
                            break
                    if len(negative_slope) >= 2:
                        process_chain(negative_slope, current_player, handled_negative)

        return scores
    
    def detect_threats(self):
        """Finds chains of 3 same player tokens and evaluates them as immediate threats that should be blocked.


        Returns:
            Dictionary: shows scores for both players after all checks
        """
        scores = {1: 0, 2: 0}
        
        for row in self.board:
            for col in range(4):
                for player in [1, 2]:
                    if row[col:col+4].count(player) == 3 and row[col:col+4].count(0) == 1:
                        scores[player] += 100 
                    
                    elif row[col:col+4].count(player) == 2 and row[col:col+4].count(0) == 2:
                        scores[player] += 100 

        for col in range(7):
            for row in range(3):
                for player in [1, 2]:
                    tokens = [self.board[row+i][col] for i in range(4)]
                    if tokens.count(player) == 3 and tokens.count(0) == 1:
                        scores[player] += 100

                    elif tokens.count(player) == 2 and tokens.count(0) == 2:
                        scores[player] += 100

        for row in range(3, 6):
            for col in range(4):
                for player in [1,2]:
                    tokens = [self.board[row-i][col+i] for i in range(4)]
                    if tokens.count(player) == 3 and tokens.count(0) == 1:
                        scores[player] += 100 

                    elif tokens.count(player) == 2 and tokens.count(0) == 2:
                        scores[player] += 100
        
        for row in range(3):
            for col in range(4):
                for player in [1, 2]:
                    tokens = [self.board[row+i][col+i] for i in range(4)]
                    if tokens.count(player) == 3 and tokens.count(0) == 1:
                        scores[player] += 100 

                    elif tokens.count(player) == 2 and tokens.count(0) == 2:
                        scores[player] += 100

        return scores
    
    def evaluate_position(self):
        """Calculates horizontal and vertical scores together into dictionary keys for 1 and 2 and then substacts the score of player 2(human player) from score of player 1(ai player)
        to get the evaluation for the board position
        Returns:
            Integer: Shows value for the evaluated board position
        """
        horizontal_scores = self.horizontal_score()
        vertical_scores = self.vertical_score()
        diagonal_scores = self.diagonal_score()
        threats = self.detect_threats()

        combined_scores = {1: horizontal_scores[1] + vertical_scores[1] + diagonal_scores[1] + threats[1], 
                           2: horizontal_scores[2] + vertical_scores[2] + diagonal_scores[2] + threats[2]}
        score_difference = combined_scores[1] - combined_scores[2]
        return score_difference

if __name__ =="__main__":
    game = Connect4()
    game.start_game()
















