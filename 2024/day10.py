from collections import defaultdict
from itertools import combinations


def get_neighbors(coords):
    r, c = coords
    return set([(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)])


with open("day10.in", "r") as infile:
    lines = [line.strip() for line in infile.readlines()]

    grid = [[i for i in line] for line in lines]
    height = len(grid)
    width = len(grid[0])

    _map = defaultdict(lambda: -1)
    queue: list[tuple] = []
    ends = set()
    for r in range(height):
        for c in range(width):
            val = int(grid[r][c])
            _map[(r, c)] = val
            if val == 0:
                queue.append(((r, c), 0, []))
            elif val == 9:
                ends.add((r, c))

    start_to_end: set[tuple[tuple, tuple]] = set()

    res = 0
    while queue:
        curr = queue.pop()
        coords, val, visited = curr
        if coords in visited:
            continue

        visited.append(coords)
        if coords in ends:
            # if ((visited[0], coords)) not in start_to_end:
            res += 1
            # start_to_end.add((visited[0], coords))
            continue

        for new_coords in get_neighbors(coords):
            if _map[new_coords] == val + 1:
                queue.append((new_coords, val + 1, visited + [coords]))

    print(res)
