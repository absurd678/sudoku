def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j

    return None


def valid(board, num, pos):
    for i in range(len(board)):  # Проверяю по линиям
        if board[pos[0]][i] == num and pos[1] != i:  # pos[0] - индекс списка в board (линия), pos[1] -
            # индекс элемента (стобец)
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3  # Начальный индекс для определения длины квадрата
    box_y = pos[0] // 3  # Тож самое, только это его высота
    for i in range(box_y*3, box_y*3 + 3):  # Шаримся в пределах 3х списков (3 линии чисел в этом квадрате)
        for j in range(box_x*3, box_x*3 + 3):  # Три слолбца в виде элементов списка
            if board[i][j] == num and (i, j) != pos:
                return False
    return True


def solve(board):  # НАЧАЛО
    empty = find_empty(board)  # Иду по очереди, при каждом вызове проверяю, где следующий ноль
    if not empty:
        return True  # Таблица заполнена
    else:
        row, column = empty
    for i in range(1, 10):
        if valid(board, i, (row, column)):  # Проверка, которая решит, подходит ли цифра при данном списке
            board[row][column] = i

            if solve(board):  # С вставленным значением повторяю функцию для списка с этим значением
                return True   # До этого дойдет, когда таблица заполнится, потом все предыдущие solve для
            # предыдущих значений начнут выдавать True

            board[row][column] = 0  # Если с новым значением не получилось, чекаю следующее
            # (при этом выше вызванная функция проверила в своем цикле, что возможных значений нет)
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
print("Результат:")
solve(b)
show(b)
print()
print("Список заполненный в функции", end="\n\n")
bl = fill()
show(bl)
print("Результат:", end="\n")
solve(bl)
show(bl)
print(bl)