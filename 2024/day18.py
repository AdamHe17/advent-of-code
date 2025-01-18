from collections import defaultdict, deque


def get_neighbors(coords):
    r, c = coords
    return set([(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)])


with open("day18.in", "r") as infile:
    lines = [line.strip() for line in infile.readlines()]

    _grid = defaultdict(lambda: None)

    width = 71
    height = 71
    fall = 1024

    for r in range(width):
        for c in range(height):
            _grid[(r, c)] = "."

    while True:
        grid = _grid.copy()
        for i, line in enumerate(lines):
            if i == fall:
                break
            c, r = map(int, line.split(","))
            grid[(r, c)] = "#"

        start = (0, 0)
        end = (height - 1, width - 1)

        queue = deque([(start, 0)])
        visited = set()
        res = -1
        while queue:
            curr, steps = queue.popleft()
            if curr == end:
                res = steps
                break

            if curr in visited:
                continue

            if grid[curr] == "#" or grid[curr] == None:
                continue

            visited.add(curr)
            for n in get_neighbors(curr):
                if n not in visited:
                    queue.append((n, steps + 1))

        # part 1
        if fall == 1024:
            print(res)

        # part 2
        if res > 0:
            fall += 1
        else:
            print(f"{c},{r}")
            break
