def countLuck(matrix, k):
    def is_valid(matrix, row, col):
        return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])

    def neighbors(matrix, r, c):
        indices = [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]
        return [
            (row, col)
            for row, col in indices
            if is_valid(matrix, row, col)
            and (
                matrix[row][col] == "."
                or matrix[row][col] == "*"
                or matrix[row][col] == "M"
            )
        ]

    def find(s):
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if col == s:
                    return (i, j)

    def backtrace(parent, start, end):
        path = [end]
        while path[-1] != start:
            path.append(parent[path[-1]])
        path.reverse()
        return path

    def count_points(coords):

        count = 0
        for row, col in coords:
            if (row, col) == end:
                continue
            nbs = neighbors(matrix, row, col)
            lim = 1 if (M == (row, col)) else 2

            if len(nbs) > lim:
                count += 1
        return count

    M = find("M")
    end = find("*")

    visited = set()
    parent = {}
    queue = [M]
    while queue:
        r, c = queue.pop()
        visited.add((r, c))
        if matrix[r][c] == "*":
            path = backtrace(parent, M, end)
            p = count_points(path)
            break
        nbs = neighbors(matrix, r, c)
        for row, col in nbs:
            if (row, col) not in visited:
                queue.append((row, col))
                parent[(row, col)] = (r, c)

    if p == k:
        return "Impressed"
    else:
        return "Oops!"
