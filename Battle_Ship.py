board = []

for i in range(0, 6):
    board.append(["O"] * 6)
print(board)

def print_board(board):
    for x in board:
        print(" ".join(x))
print(print_board(board))

from random import randint

def random_row(board):
    return randint(1, len(board))
def random_col(board):
    return randint(1, len(board))

ship_row = random_row(board)
ship_col = random_col(board)
row_and_col = [ship_row, ship_col]
print(row_and_col)
print("You have 4 turns to Search my ship.")
print("Try and find my ship!")

for turn in range(0, 4):
    print("Turn:", turn + 1)
    guess_row = int(input("Guess the row: "))
    guess_col = int(input("Guess the col: "))
    def print_guessed_board(board):
        board[guess_row - 1][guess_col - 1] = 'X'
        return print_board(board)
    def Game_Over(board):
        if turn == 4 - 1:
            print("Game Over!")    
    
    if guess_row == ship_row and guess_col == ship_col:
        print("Woow! You won!")
        print_guessed_board(board)
        break
    
    
    else:
        if guess_row not in range(0, 6) or guess_col not in range(0, 6):
            print("You are not in the ocean")
      
        elif board[guess_row - 1][guess_col - 1] == 'X':
            print("You guessed that already!")
        
        else:
            print("You guess is mistake!")
        
        print_guessed_board(board)
        Game_Over(board)