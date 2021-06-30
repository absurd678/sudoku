def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j

    return None


def valid(board, num, pos):
    for i in range(len(board)):  # Checking the row
        if board[pos[0]][i] == num and pos[1] != i:  # pos[0] - row, pos[1] -
            # idx of elem (column)
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3  # Initial idx for square's length
    box_y = pos[0] // 3  # for height
    for i in range(box_y*3, box_y*3 + 3):  # Checking the elements in range of 3 rows (lists)
        for j in range(box_x*3, box_x*3 + 3):  # In range of 3 columns
            if board[i][j] == num and (i, j) != pos:
                return False
    return True


def solve(board):  # BEGINNING
    empty = find_empty(board)  # Searching the next zero 
    if not empty:
        return True  # Board is filled
    else:
        row, column = empty
    for i in range(1, 10):
        if valid(board, i, (row, column)):  # if the i fits instead of 0
            board[row][column] = i

            if solve(board):  # start solving with new board (with 0 switched to i)
                return True

            board[row][column] = 0  # If it hasn't solved with i, then we check the next
    return False


def show(board):
    for i in range(len(board)):

        if i % 3 == 0 and i != 0:
            print("-"*24)

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | " + str(board[i][j]), end=" ")
            else:
                print(board[i][j], end=" ")
        print()


def fill():
    import random
    l = []
    for i in range(9):
        l.append([random.randrange(1, 10) for e in range(9)])
    for i in range(len(l)):
        for j in range(len(l[0])):
            if not valid(l, l[i][j], (i, j)):
                l[i][j] = 0
    return l



b = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

show(b)
print("Result:")
solve(b)
show(b)
