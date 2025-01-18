from collections import defaultdict, deque


with open("day16.in", "r") as infile:
    lines = [line.strip() for line in infile.readlines()]

    _grid = [[i for i in line] for line in lines]
    height = len(_grid)
    width = len(_grid[0])
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    start = None
    end = None
    grid = defaultdict(lambda: "#")
    for r in range(height):
        for c in range(width):
            if _grid[r][c] == "S":
                start = (r, c)
            elif _grid[r][c] == "E":
                end = (r, c)
            grid[(r, c)] = _grid[r][c]

    queue = deque([[start, 0, 0, set([start])]])  # pos, dir, score, path
    visited = defaultdict(lambda: float("inf"))
    scores = defaultdict(list)
    while queue:
        pos, curr_dir, score, curr_path = queue.popleft()
        if pos == end:
            scores[score].append(curr_path)
            continue

        r, c = pos
        for ind, (dr, dc) in enumerate(dirs):
            nr, nc = r + dr, c + dc
            if grid[(nr, nc)] in ".E":
                if (nr, nc) in curr_path:
                    continue
                diff = abs(ind - curr_dir)
                turn = min(diff, 4 - diff)
                queue.append(
                    [
                        (nr, nc),
                        ind,
                        score + 1000 * turn + 1,
                        curr_path.union(set([(nr, nc)])),
                    ]
                )

    min_score = min(scores.keys())
    print(min_score)
    tiles = set()
    for path in scores[min_score]:
        tiles = tiles.union(set(path))

    print(len(tiles))
