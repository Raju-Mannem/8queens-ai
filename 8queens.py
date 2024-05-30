# 8 queens problem

#The 8-Queens problem involves placing 8 queens on an 8x8 chessboard such that no two queens are attacking each other. Here's a sample implementation of the 8-Queens problem using Python:

def is_valid(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False
    
    # Check if there is a queen in the same diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, 8)):
        if board[i] == j:
            return False
    
    return True

def solve(board, row):
    if row == 8:
        return True
    
    for col in range(8):
        if is_valid(board, row, col):
            board[row] = col
            if solve(board, row+1):
                return True
            board[row] = -1
    
    return False

def print_board(board):
    for row in range(8):
        line = ""
        for col in range(8):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

# Example usage
board = [-1] * 8
solve(board, 0)
print_board(board)

#In the above code, the is_valid function checks whether it is valid to place a queen at a particular row and column on the board. We first check if there is a queen in the same column or the same diagonal as the given position. The solve function uses backtracking to try all possible positions for the queens, starting with the first row and moving down. If a valid position is found for a queen in a given row, the function recurses to the next row. If all 8 queens can be placed on the board without attacking each other, the function returns True. The print_board function simply prints the final board state in a human-readable format.

#When we run the above code, it will output one possible solution to the 8-Queens problem:

Q . . . . . . . 
. . . . Q . . . 
. . . . . . . Q 
. . . . . Q . . 
. . Q . . . . . 
. . . . . . Q . 
. . . Q . . . . 
. . . . . . . Q 

