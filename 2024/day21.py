from collections import defaultdict, deque
from itertools import combinations
from functools import lru_cache


with open("day21.in", "r") as infile:
    lines = [line.strip() for line in infile.readlines()]

    numpad = ("789", "456", "123", "#0A")
    num_to_pos = {}
    for r in range(len(numpad)):
        for c in range(len(numpad[0])):
            num_to_pos[numpad[r][c]] = (r, c)
    dpad = ("#^A", "<v>")
    d_to_pos = {}
    for r in range(len(dpad)):
        for c in range(len(dpad[0])):
            d_to_pos[dpad[r][c]] = (r, c)
    dirs = {(0, -1): "<", (0, 1): ">", (1, 0): "v", (-1, 0): "^"}
    r_dirs = {v: k for k, v in dirs.items()}

    def get_neighbors(coords):
        r, c = coords
        return set([(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)])

    def bfs(grid, start, end):
        height = len(grid)
        width = len(grid[0])
        queue = deque()
        queue.append((start, [start]))
        visited = set()
        shortest = None
        while queue:
            curr, path = queue.popleft()
            if curr == end:
                shortest = path
                break

            if curr in visited:
                continue
            visited.add(curr)

            for n in get_neighbors(curr):
                nr, nc = n
                if 0 <= nr < height and 0 <= nc < width:
                    queue.append((n, path + [n]))

        res = []
        for i in range(len(shortest) - 1):
            (ar, ac) = shortest[i]
            (br, bc) = shortest[i + 1]
            res.append(dirs[(br - ar, bc - ac)])

        path = "".join(sorted(res, key=lambda x: "<^v>".index(x)))
        curr = start
        passed = []
        for p in path:
            dr, dc = r_dirs[p]
            r, c = curr
            passed.append((r + dr, c + dc))
            curr = passed[-1]

        if (grid == numpad and (3, 0) in passed) or (grid == dpad and (0, 0) in passed):
            return path[::-1]
        return path

    num_paths = {}
    for start in num_to_pos.values():
        for end in num_to_pos.values():
            if start == end:
                continue
            num_paths[(start, end)] = bfs(numpad, start, end)
    d_paths = {}
    for start in d_to_pos.values():
        for end in d_to_pos.values():
            d_paths[(start, end)] = bfs(dpad, start, end)

    def instrs(paths, v_to_pos, line):
        return (
            "A".join(
                paths[(v_to_pos[i], v_to_pos[j])] for i, j in zip("A" + line, line)
            )
            + "A"
        )

    @lru_cache
    def get_lengths(instrs, levels):
        if levels == 0:
            return len(instrs)

        instrs = "A" + instrs + "A"

        res = 0
        for i, j in zip(instrs, instrs[1:]):
            res += get_lengths(d_paths[(d_to_pos[i], d_to_pos[j])], levels - 1)

        return res + len(instrs) - 2

    res = 0
    robots = 25
    for line in lines:
        a = instrs(num_paths, num_to_pos, line)
        b = a
        # for _ in range(robots):
        #     b = instrs(d_paths, d_to_pos, b)
        length = get_lengths(a, robots)
        print(len(b), length, int(line[:-1]))

        res += length * int(line[:-1])

    print(res)
