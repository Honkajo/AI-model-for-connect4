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
        
    def start_game(self):
        '''Starts the game by choosing starting player at random and creates the game loop. Algorithm not implemented yet for ai so ai moves are still random.
        '''
        for row in self.board:
            print(row)
    
        players = ["ai", "human"]
        self.starting_player = random.choice(players)
        current_turn = self.starting_player

        while True:
        
            if current_turn == "ai":
                chosen_col = random.randint(1, 7)
                self.make_move(chosen_col)

            else:
                chosen_col = int(input(f"Choose your move(1-7):  "))
                self.make_move(chosen_col)



    def make_move(self, col):
        '''Function for making a move in Connect4
        '''
        i = 5
        while i >= 0:
            if self.board[i][col] == 0:
                if self.starting_player == "ai":
                    self.board[i][col] == 1
                else:
                    self.board[i][col] == 2
            else:
                i -= 1



















