# A program written to solve a sudoku problem using backtracking

test = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def print_board(board):
    # Prints the board.

    for i in range(9):
        for j in range(9):
            print(board[i][j], end=' ')
        print(f"\n")

def check_empty(board):
    # Checks if a coordinate in a board is empty (0).

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i,j)
    
    return None

def validate(board, num, row, col):
    # Checks if the number exists in its designated row, column, or 3x3 grid.

    # Check row.
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # Check column.
    for j in range(9):
        if board[j][col] == num:
            return False
            
    # Check 3x3 grid.
    r = row//3
    c = col//3
    for i in range(r*3, (r*3)+3):
        for j in range((c*3)+3, c*3 ):
            if board[i][j] == num:
                return False

    return True
    
def solve_board(board):
    # Solves the sudoku board.

    # Check an empty coordinate in the sudoku board.
    coordinate = check_empty(board)
    if not coordinate:
        return True
    x = coordinate[0]
    y = coordinate[1]
    
    # Test the values 1 to 9.
    for i in range(1, 10):
        # Validate if these numbers are safe to be assigned in the coordinate.
        if validate(board, i, x, y):
            board[x][y] = i
            # Return true if valid and successful.
            if solve_board(board):
                return True
            # If previous validate number disagrees with the current validated number, reset
            board[x][y] = 0
    # Initiate backtracking
    return False


        





print_board(test)
solve_board(test)
print(f"-------------------------------------------------------------")
print_board(test)


    





