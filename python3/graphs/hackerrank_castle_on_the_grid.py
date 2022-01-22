from collections import deque


def minimumMoves(matrix, start_x, start_y, goal_x, goal_y):
    def is_valid(matrix, x, y, counts):
        return (
            0 <= y < len(matrix)
            and 0 <= x < len(matrix)
            and matrix[x][y] != "X"
            and counts[x][y] == -1
        )

    def get_moves(matrix, x, y, counts):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        moves = []
        for d in directions:
            new_x, new_y = x + d[0], y + d[1]
            while is_valid(matrix, new_x, new_y, counts):
                moves.append((new_x, new_y))
                new_x, new_y = new_x + d[0], new_y + d[1]
        return moves

    D = deque()
    D.appendleft((start_x, start_y))
    counts = [[-1] * len(matrix) for _ in range(len(matrix))]
    counts[start_x][start_y] = 0

    while D:
        x, y = D.pop()
        c = counts[x][y]
        m = get_moves(matrix, x, y, counts)
        for new_x, new_y in m:
            if (new_x, new_y) == (goal_x, goal_y):
                return c + 1
            D.appendleft((new_x, new_y))
            counts[new_x][new_y] = c + 1

    return -1
