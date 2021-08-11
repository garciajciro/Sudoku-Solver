
bord = [
    [9, 0, 0, 3, 7, 0, 0, 8, 0],
    [0, 0, 4, 0, 8, 0, 0, 1, 0],
    [6, 8, 0, 0, 0, 2, 0, 3, 0],
    [0, 0, 0, 1, 0, 0, 8, 2, 0],
    [8, 0, 5, 4, 0, 9, 3, 0, 6],
    [0, 2, 9, 0, 0, 7, 0, 0, 0],
    [0, 6, 0, 2, 0, 0, 0, 5, 4],
    [0, 4, 0, 0, 5, 0, 7, 0, 0],
    [0, 9, 0, 0, 4, 1, 0, 0, 8]
]


def Sudoku_solver(board):
    vacio = empty_spot(board)
    if not vacio:
        return True
    else:
        row, col = vacio

    for i in range(1, 10):
        if ValidNumber(board, i, (row, col)):
            board[row][col] = i

            if Sudoku_solver(board):
                return True

            board[row][col] = 0


def ValidNumber(board, number, pos):

    # Check Column
    for rang in range(len(board[0])):
        if board[pos[0]][rang] == number and pos[1] != rang:
            return False

    # Check Row
    for rang in range(len(board[0])):
        if board[rang][pos[1]] == number and pos[0] != rang:
            return False

    # Check Smaller Squares

    square_x = pos[1] // 3
    square_y = pos[0] // 3

    for i in range(square_y*3, square_y*3 + 3):
        for j in range(square_x*3, square_x*3 + 3):
            if board[i][j] == number:
                return False

    return True


def empty_spot(board):
    for row in range(len(board[0])):
        for column in range(len(board[0])):
            if board[row][column] == 0:
                return (row, column)

    return None


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


Sudoku_solver(bord)
print_board(bord)
