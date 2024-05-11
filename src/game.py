import random
import time

def print_board(board):
    """Prints the current state of the Connect4 board

    Args:
        board (list): game board as a 2D-list
    """
    print("1 2 3 4 5 6 7")
    print("-------------")
    for row in board:
        print(' '.join(str(cell) for cell in row))
    print("\n")

def full_board(board):
    """Checks if the board is completely filled

    Args:
        board (list): game board as a 2D-list

    Returns:
        bool: True if the board is full
    """
    for col in range(7):
        if board[0][col] == 0:
            return False
    return True

def iterative_deepening(board, alpha, beta, max_player, time_limit, player_piece, ai_piece):
    """Iterative deepening with minimax and alpha-beta-pruning to figure out the best move for ai

    Args:
        board (list): game board as a 2D-list
        alpha (float): Alpha value for alpha-beta-pruning
        beta (float): Beta value for alpha-beta-pruning
        max_player (bool): True if its ai's turn
        time_limit (int): maximum time to search for the best move
        player_piece (int): Number for player piece
        ai_piece (int): Number for ai piece

    Returns:
        int: Column number where ai plays its piece
    """
    hash_map = {}
    start_time = time.time()
    depth = 1
    while True:
        best_col, _ = minimax(board, depth, alpha, beta, max_player, player_piece, ai_piece, hash_map)
        if time.time() - start_time > time_limit:
            break
        depth += 1
    return best_col

def minimax(board, depth, alpha, beta, max_player, player_piece, ai_piece, hash_map): 
    """Minimax with alpha-beta-pruning to determine best move for ai

    Args:
        board (list): game board as a 2D-list
        depth (int): Current depth limit for the algorithm
        alpha (float): Alpha value for alpha-beta-pruning
        beta (float): Beta value for alpha-beta-pruning
        max_player (bool): True if its ai's turn
        player_piece (int): Number for player piece
        ai_piece (int): Number for ai piece
        hash_map (dict): storage for previously computed values for board states

    Returns:
        tuple: Contains the best column to play the move and evaluation score for that move
    """
    if full_board(board):
        return None, 0

    if depth == 0:
        return None, evaluate_position(board, ai_piece, player_piece, ai_piece)

    ordered_cols = sorted(valid_moves(board))

    if max_player: 
        value = float("-inf")
        column = 0
        board_key = str(board)
        best_col = hash_map.get(board_key)
        if best_col is not None:
            ordered_cols.remove(best_col)
            ordered_cols.insert(0, best_col)

        for i in ordered_cols:
            row = get_next_open_row(board, i)
            copy_board = [row[:] for row in board]
            make_move(copy_board, row, i, ai_piece)

            if is_game_over(copy_board, (row, i)):
                return i, 1000

            new_value = minimax(copy_board, depth - 1, alpha, beta, False,
                                player_piece, ai_piece, hash_map)[1]
            if new_value > value:
                value = new_value
                column = i

            alpha = max(value, alpha)
            if alpha >= beta:
                break

        hash_map[board_key] = column
        return column, value

    else:
        value = float("inf")
        column = 0

        board_key = str(board)
        best_col = hash_map.get(board_key)
        if best_col is not None:
            ordered_cols.remove(best_col)
            ordered_cols.insert(0, best_col)

        for i in ordered_cols:
            row = get_next_open_row(board, i)
            copy_board = [row[:] for row in board]
            make_move(copy_board, row, i, player_piece)

            if is_game_over(copy_board, (row, i)):
                return i, -1000

            new_value = minimax(copy_board, depth - 1, alpha, beta, True,
                                player_piece, ai_piece, hash_map)[1]
            if new_value < value:
                value = new_value
                column = i

            beta = min(value, beta)
            if alpha >= beta:
                break

        hash_map[board_key] = column
        return column, value

    
def is_game_over(board, last_move):
    """Determines if the game has ended to a winning position

    Args:
        board (list): game board as a 2D-list
        last_move (tuple): row and column numbers of the last move made

    Returns:
        bool: Returns True if the game is over
    """
    if last_move is None:
        return False
    x, y = last_move
    token = board[x][y]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                    (-1, -1), (1, 1), (1, -1), (-1, 1)]

    for dx, dy in directions:
        count = 1

        nx, ny = x + dx, y + dy
        while 0 <= nx < 6 and 0 <= ny < 7 and board[nx][ny] == token:
            count += 1
            nx += dx
            ny += dy
            if count >= 4:
                return True

        nx, ny = x - dx, y - dy
        while 0 <= nx < 6 and 0 <= ny < 7 and board[nx][ny] == token:
            count += 1
            nx -= dx
            ny -= dy
            if count >= 4:
                return True

        if count < 4:
            count = 1

    return False

def is_valid_move(board, column):
    """Checks if the move can be made into the spesified column

    Args:
        board (list): game board as a 2D-list
        column (int): Column number to check for valid move

    Returns:
        bool: True if move is valid
    """
    
    return board[0][column] == 0

def make_move(board, row, column, piece):
    """Place the piece into a spesified row and column

    Args:
        board (list): game board as a 2D-list
        row (int): row where to place the piece
        column (int): column where to place the piece
        piece (int): piece to place into the spesified row and column
    """
  
    board[row][column] = piece


def get_next_open_row(board, column):
    """Finds the lowest empty space in a column

    Args:
        board (list): game board as a 2D-list
        column (int): The column to check

    Returns:
        int: The row index where the piece can be placed
    """
    
    for row in range(5, -1, -1):
        if board[row][column] == 0:
            return row
    return None

def valid_moves(board):
    """Creates a list of valid columns where to place a piece

    Args:
        board (list): game board as a 2D-list

    Returns:
        list: list of column numbers where piece can be placed
    """

    return [col for col in PREFERRED_COLS if is_valid_move(board, col)]

def evaluate_position(board, piece, player_piece, ai_piece):
    """Evaluates the board and returns a score based on the board state

    Args:
        board (list): game board as a 2D-list
        piece (int): Current players piece type which is evaluated
        player_piece (int): The player's piece
        ai_piece (int): The AI's piece

    Returns:
        int: Evaluated score of the board from the view of the current player
    """

    value = 0
    opponent_piece = player_piece if piece == ai_piece else ai_piece

    for row in board:
        for col in range(4):
            if row[col:col+4].count(piece) == 4:
                value += 100
            elif row[col:col+4].count(piece) == 3 and row[col:col+4].count(0) == 1:
                value += 5
            elif row[col:col+4].count(piece) == 2 and row[col:col+4].count(0) == 2:
                value += 2
            if row[col:col+4].count(opponent_piece) == 3 and row[col:col+4].count(0) == 1:
                value -= 4
            elif row[col:col+4].count(opponent_piece) == 2 and row[col:col+4].count(0) == 2:
                value -= 2
            

    for col in range(7):
        for row in range(3):
            tokens = [board[row+i][col] for i in range(4)]
            if tokens.count(piece) == 4:
                value += 100
            elif tokens.count(piece) == 3 and tokens.count(0) == 1:
                value += 5
            elif tokens.count(piece) == 2 and tokens.count(0) == 2:
                value += 2
            if tokens.count(opponent_piece) == 3 and tokens.count(0) == 1:
                value -= 4
            elif tokens.count(opponent_piece) == 2 and tokens.count(0) == 2:
                value -= 2

    for row in range(3, 6):
        for col in range(4):
            tokens = [board[row-i][col+i] for i in range(4)]
            if tokens.count(piece) == 4:
                value += 100
            elif tokens.count(piece) == 3 and tokens.count(0) == 1:
                value += 5
            elif tokens.count(piece) == 2 and tokens.count(0) == 2:
                value += 2
            if tokens.count(opponent_piece) == 3 and tokens.count(0) == 1:
                value -= 4
            elif tokens.count(opponent_piece) == 2 and tokens.count(0) == 2:
                value -= 2

    for row in range(3):
        for col in range(4):
            tokens = [board[row+i][col+i] for i in range(4)]
            if tokens.count(piece) == 4: 
                value += 100
            elif tokens.count(piece) == 3 and tokens.count(0) == 1:
                value += 5
            elif tokens.count(piece) == 2 and tokens.count(0) == 2:
                value += 2
            if tokens.count(opponent_piece) == 3 and tokens.count(0) == 1:
                value -= 4
            elif tokens.count(opponent_piece) == 2 and tokens.count(0) == 2:
                value -= 2

    return value

"""Game loop for the Connect4 game"""

PLAYER_PIECE = 1
AI_PIECE = 2
PLAYERS = ["AI", "PLAYER"]
TURN = random.choice(PLAYERS)

BOARD = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]

PREFERRED_COLS = [3, 2, 4, 1, 5, 0, 6]

while True:
    if full_board(BOARD):
        print("It's a draw!")
        break

    if TURN == "PLAYER":
        print_board(BOARD)
        try:
            COLUMN = int(input("Choose your move(1-7):  ")) - 1
            if is_valid_move(BOARD, COLUMN - 1) and COLUMN >= 0 and COLUMN <= 7:
                row = get_next_open_row(BOARD, COLUMN)
                make_move(BOARD, row, COLUMN, PLAYER_PIECE)
                if is_game_over(BOARD, (row, COLUMN)):
                    print_board(BOARD)
                    print("Game over!")
                    print("You win!")
                    break
                TURN = "AI"
            else:
                print("Invalid move. Try again!")
        except IndexError:
            print("Please enter a number between 1 and 7")
        except ValueError:
            print("Please enter a number between 1 and 7")

    if TURN == "AI":
        COLUMN = iterative_deepening(
            BOARD, float('-inf'), float('inf'), True,
              5, PLAYER_PIECE, AI_PIECE)

        if is_valid_move(BOARD, COLUMN):
            row = get_next_open_row(BOARD, COLUMN)
            make_move(BOARD, row, COLUMN, AI_PIECE)
            if is_game_over(BOARD, (row, COLUMN)):
                print_board(BOARD)
                print("Game over!")
                print("You lose!")
                break
            TURN = "PLAYER"
