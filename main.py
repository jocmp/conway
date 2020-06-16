
import itertools
import os
import time


def neighbors(point):
    x, y = point
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1
    yield x + 1, y + 1
    yield x + 1, y - 1
    yield x - 1, y - 1
    yield x - 1, y + 1


def advance(board):
    # Any live cell with two or three live neighbours survives.
    # Any dead cell with three live neighbours becomes a live cell.
    # All other live cells die in the next generation. Similarly, all other dead cells stay dead.

    next_state = set()
    next_neighbors = board | set(itertools.chain(*map(neighbors, board)))
    for point in next_neighbors:
        count = sum((neighbor in board) for neighbor in neighbors(point))
        if count == 3 or (count == 2 and point in board):
            next_state.add(point)

    return next_state


def format_board(board):
    x = 60
    y = 40
    (x_min, x_max) = (-1 * x, x)
    (y_min, y_max) = (-1 * y, y)
    output = ""
    for i in range(x_min - 1, x_max + 1):
        for j in range(y_min - 1, y_max + 1):
            if (i, j) in board:
                output += "o"
            else:
                output += " "
        output += "\n"

    return output


if __name__ == "__main__":
    board = set(  # seed
        [
            (0, 0), (1, 0), (2, 0), (0, 1), (1, 2),
            (10, 3), (10, 4), (10, 5), (10, 6), (11, 3),
            (-10, 10), (-10, 9), (-11, 10), (-9, 10), (-9, 11)
        ]
    )
    for i in range(1000):
        os.system("clear")
        board = advance(board)
        print(format_board(board))
        time.sleep(0.2)
