import math

# Constants for players
HUMAN = 'X'
AI = 'O'
EMPTY = ' '

# Initialize the board
def create_board():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

# Print the board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Check for a winner
def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None

# Check if the board is full
def is_full(board):
    for row in board:
        if EMPTY in row:
            return False
    return True

# Get available moves
def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.append((i, j))
    return moves

# Minimax algorithm with Alpha-Beta pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == AI:
        return 1
    elif winner == HUMAN:
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in get_available_moves(board):
            board[move[0]][move[1]] = AI
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move[0]][move[1]] = EMPTY
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(board):
            board[move[0]][move[1]] = HUMAN
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move[0]][move[1]] = EMPTY
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Find the best move for the AI
def best_move(board):
    best_val = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move[0]][move[1]] = AI
        move_val = minimax(board, 0, False, -math.inf, math.inf)
        board[move[0]][move[1]] = EMPTY
        if move_val > best_val:
            best_val = move_val
            best_move = move
    return best_move

# Main game loop
def play_game():
    board = create_board()
    print_board(board)
    while True:
        # Human move
        human_move = tuple(map(int, input("Enter your move (row col): ").split()))
        if board[human_move[0]][human_move[1]] != EMPTY:
            print("Invalid move. Try again.")
            continue
        board[human_move[0]][human_move[1]] = HUMAN
        print_board(board)
        if check_winner(board) == HUMAN:
            print("Human wins!")
            break
        if is_full(board):
            print("It's a tie!")
            break
        
        # AI move
        ai_move = best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = AI
            print("AI moves:")
            print_board(board)
            if check_winner(board) == AI:
                print("AI wins!")
                break
            if is_full(board):
                print("It's a tie!")
                break

if __name__ == "__main__":
    play_game()
    