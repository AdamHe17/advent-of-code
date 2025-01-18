from collections import defaultdict, deque

with open("day20.in", "r") as infile:
    lines = [line.strip() for line in infile.readlines()]

    _grid = [[i for i in line] for line in lines]
    height = len(_grid)
    width = len(_grid[0])

    def get_neighbors(coords):
        r, c = coords
        return set([(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)])

    def get_tunnels2(start, length):
        dists = defaultdict(lambda: float("inf"))
        r, c = start
        for dr in range(length + 1):
            for dc in range(length + 1):
                if 0 < dr + dc <= length:
                    for nn in [
                        (r + dr, c + dc),
                        (r - dr, c + dc),
                        (r + dr, c - dc),
                        (r - dr, c - dc),
                    ]:
                        if isinstance(grid[nn], int):
                            dists[nn] = min(dists[nn], dr + dc)

        return set((i, v) for i, v in dists.items())

    start = None
    end = None
    grid = defaultdict(lambda: "")
    for r in range(height):
        for c in range(width):
            if _grid[r][c] == "S":
                start = (r, c)
            elif _grid[r][c] == "E":
                end = (r, c)
            grid[(r, c)] = _grid[r][c]

    queue = deque()
    queue.append((end, 0))
    visited = set()
    while queue:
        curr, steps = queue.popleft()
        grid[curr] = steps
        if curr in visited:
            continue

        visited.add(curr)
        for n in get_neighbors(curr):
            if isinstance(grid[n], str) and grid[n] in ".ES":
                queue.append((n, steps + 1))

    print(grid[start])

    queue = deque()
    queue.append((end))
    visited = set()
    res = 0
    cheats = set()
    totals = defaultdict(lambda: 0)
    while queue:
        curr = queue.popleft()
        if curr in visited:
            continue
        visited.add(curr)

        for nn, length in get_tunnels2(curr, 20):
            saved = grid[curr] - grid[nn] - length
            if saved >= 100:
                totals[saved] += 1
                res += 1

        for n in get_neighbors(curr):
            if isinstance(grid[n], int):
                queue.append(n)

    print(res)
    for i in sorted(totals.keys()):
        print(i, totals[i])
