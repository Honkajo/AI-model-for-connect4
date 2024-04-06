import random

class Connect4:
    '''Class that creates a game of connect4
    '''

    def __init__(self):
        '''Initializes the start of the game
        '''
        self.board = [[0, 0, 0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]]
        self.starting_player = None
    
    def print_board(self):
        for row in self.board:
            print(' '.join(str(cell) for cell in row))
        print("\n")
        
    def start_game(self):
        '''Starts the game by choosing starting player at random and creates the game loop. Algorithm not implemented yet for ai so ai moves are still random.
        '''
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
                self.ai_move()
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
        valid_move = False
        while not valid_move:
            chosen_col = random.randint(1, 7)
            if self.is_valid_move(chosen_col - 1):
                valid_move = True
        self.make_move(chosen_col, "ai")

    def is_valid_move(self, col):
        return self.board[0][col] == 0



    def make_move(self, col, player):
        '''Function for making a move in Connect4
        '''
        col -= 1
        for i in range(5, -1, -1):
            if self.board[i][col] == 0:
                 self.board[i][col] = 1 if player == "ai" else 2
                 break
            
    def check_horizontal_win(self):
        for row in self.board:
            for col in range(4):
                if row[col] == row[col + 1] == row[col +2] == row[col + 3] != 0:
                    return True
        return False
    def check_vertical_win(self):
        for col in range(7):
            for row in range(3):
                if self.board[row][col] == self.board[row + 1][col] == self.board[row + 2][col] == self.board[row + 3][col] != 0:
                    return True
        return False
    
    def check_diagonal_win(self):
        for row in range(3, 6):
            for col in range(4):
                if self.board[row][col] == self.board[row - 1][col + 1] == self.board[row - 2][col + 2] == self.board[row - 3][col + 3] != 0:
                    return True
                
        for row in range(3, 6):
            for col in range(3, 7):
                if self.board[row][col] == self.board[row - 1][col - 1] == self.board[row - 2][col - 2] == self.board[row - 3][col - 3] != 0:
                    return True
                
    def is_game_over(self):
        if self.check_horizontal_win() or self.check_vertical_win() or self.check_diagonal_win():
            return True
        count = sum(cell != 0 for row in self.board for cell in row)
        if count == 42:
            return True
        return False        



if __name__ =="__main__":
    game = Connect4()
    game.start_game()
















