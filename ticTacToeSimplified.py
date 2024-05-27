# Tarun Pokra
# CPSC 3750 - Assignment Two
# May 25th, 2024
# Programming Question - TicTacToe.
# Note, I've previously made this before in my spare time, but I simplified it, and added minimax algorithm, and alpha-beta pruning.

# alpha, beta stuff, importing library

import math

# these are constants
AI = 'O' # ai's move is display as O

HUMAN = 'X'# while the user's is displayed as X

EMPTY = ' ' # this shows the empty spaces on the board, like when it is initialized first.

# Create an empty board

# here I create 3 by 3 board, like a matrix.
def create_board():
    return [[EMPTY, EMPTY, EMPTY] for _ in range(3) ] # 3 then multiply by 3, total of 9 spaces.

# display the board to the user.
def print_board(board):
    for row in board:
        #borders basically

        print(' | '.join(row))
        # rows are spaced out with |


        print('-' * 10)
        # i had to fix this because it printed only halfway before, so i made this multiply from 5 to 10.

# see if theres a winner
def check_winner(board):

    # Rows, columns, and diagonalsl, 
    lines = [board[0], board[1], board[2], 
              # rows are defined, 
             [board[i][0] for i in range(3)], [board[i][1] for i in range(3)], [board[i][2] for i in range(3)], 
               # Columns defined
             [board[i][i] for i in range(3)], [board[i ][2 - i] for i in range(3)] ]   # Diagonals defined to see if winner, 3 total
    # for each
# these are stored in lines above to create a 3 space line to declre a winner. 
    for line in lines: #this for-loop shows if there are no lines connecting three spaces for a winner. 

        if line[0] == line[1] == line[2] != EMPTY:

            return line[0]
    return None # no winner

# board full?
# check it out
def is_full(board):
    return all(cell != EMPTY for row in board for cell in row)

# check moves that you have, that will work.
def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]
# like for example if the AI chosen (0 0) for row and col, then if you do that after it will tell the user
# to choose a different move because that space is not empty, it is taken. 

# minmax algorithm with Alpha-beta pruning here.

def minimax(board, depth, is_maximizing, alpha, beta):
    # shows whos winner, ai, user, or tie. 
    winner = check_winner(board)
    if winner == AI:
        return 1
    elif winner == HUMAN:
        return -1
    elif is_full(board): # tie.
        return 0

    if is_maximizing:
        #imported math library at the top for this.

        max_eval = -math.inf
        for (i, j) in get_available_moves(board):
            board[i][j] = AI
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[i][j] = EMPTY
            # mpty board, added 1
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            # logically beta cant be bigger than alpha, but it can be of equal value or less. 

            if beta <= alpha:
                break
        return max_eval # show max 
    
    else:

        min_eval = math.inf
        #grab the moves that you can still do on the board.

        for (i, j) in get_available_moves(board):

            board[i][j] = HUMAN
            
            eval = minimax(board, depth + 1, True, alpha, beta)
            # minimax for the depth + 1 is true for alpha and beta only for the user.

            
            board[i][j] = EMPTY # empty

            
            min_eval = min(min_eval, eval)

            # minimum value has paras of the evaluation, and the bare-minimum evaluation


            
            beta = min(beta, eval)
            # beta equals the min paras of beta it self, and the eval from above.

            
            if beta <= alpha:
                # same code i cut copied, and pasted here from above.

                break
        return min_eval #instead of max above, return min.

# the best move for ai

def best_move(board):
    # this helps establish the ai to make the best decision, or utlity action possible.

    # best value math library imported is used.

    best_val = -math.inf
    move = None

    for (i, j) in get_available_moves(board):

        
        board[i][j] = AI
        
        move_val = minimax(board, 0, False, -math.inf, math.inf)
        # here i put -math.inf, and mathinf to initialize alpha and beta.

        board[i][j] = EMPTY
        
        # determine the best action, or expected utility. 

        if move_val > best_val:
            best_val = move_val
            move = (i, j)

    return move

# Main 

# here the tic tac toe game runs. 
def play_game():

    board = create_board()

    print_board(board)
    while True:
        # user stuff for the choice of actions

        row, col = map(int, input("Enter your move with spaces, no comma (row col): ").split())

        if board[row][col] != EMPTY:
            print("Invalid move. Try again.")
            continue
        # this if statement checks if user enters a valid rol and col, thats not taken yet, and is on the board.
        # so if you type nonsense instead of 0 1 for example as row and col, you will get a display of invalid move.
        # prompt again.

        board[row][col] = HUMAN
        print_board(board)

        if check_winner(board) : # you win
            print("The user wins!!")
            break

        if is_full(board): # tie, dislay the result.
            print("It is a tie, oh well.")
            break
        
        # the AI's move
        ai_move = best_move(board)
        #determine the best move with pruning, minimax

        if ai_move:
            board[ai_move[0]][ai_move[1]] = AI

            print("AI moves:")
            # the AI's turn
            print_board(board)

            if check_winner(board):
                # the AI beats the user.
                print("The AI wins, now activating SkyNet. You are terminated!")
                break

            if is_full(board):
                print("It's a tie!") #if the board has run of spaces, or playable moves, its a tie.

                break

if __name__ == "__main__":
    play_game()
# main
# done. 
