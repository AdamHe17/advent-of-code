with open("day15.in", "r") as infile:
    _grid, _moves = map(lambda x: x.split("\n"), infile.read().split("\n\n"))

    grid = [[i for i in line] for line in _grid]
    height = len(grid)
    width = len(grid[0])
    robot = None
    for r, row in enumerate(grid):
        if "@" in row:
            robot = [r, row.index("@")]
            break

    moves = "".join(i.strip() for i in _moves)
    dirs = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}

    for move in moves:
        dr, dc = dirs[move]
        curr_r, curr_c = robot
        shift = 1
        do_move = True
        while 0 <= curr_r + shift * dr < height and 0 <= curr_c + shift * dc < width:
            peek = grid[curr_r + shift * dr][curr_c + shift * dc]
            if peek == "O":
                shift += 1
            elif peek == "#":
                do_move = False
                break
            else:
                break

        # print(shift, do_move, robot)

        if do_move:
            for s in range(shift, 0, -1):
                grid[curr_r + s * dr][curr_c + s * dc] = grid[curr_r + (s - 1) * dr][
                    curr_c + (s - 1) * dc
                ]
            grid[curr_r][curr_c] = "."
            robot = [curr_r + dr, curr_c + dc]

        # print(f"Move {move}:")
        # print("\n".join("".join(row) for row in grid))
        # print("\n")

    res = 0
    for r in range(height):
        for c in range(width):
            if grid[r][c] == "O":
                res += 100 * r + c

    # print(res)


# Part 2
with open("day15.in", "r") as infile:
    _grid, _moves = map(lambda x: x.split("\n"), infile.read().split("\n\n"))

    grid = [
        [
            i
            for i in line.replace("#", "##")
            .replace("O", "[]")
            .replace(".", "..")
            .replace("@", "@.")
        ]
        for line in _grid
    ]
    height = len(grid)
    width = len(grid[0])
    robot = None
    for r, row in enumerate(grid):
        if "@" in row:
            robot = [r, row.index("@")]
            break

    moves = "".join(i.strip() for i in _moves)
    dirs = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}

    print("\n".join("".join(row) for row in grid))
    print("\n")

    def get_box(r, c, grid):
        if grid[r][c] == "[":
            return [[r, c], [r, c + 1]]
        elif grid[r][c] == "]":
            return [[r, c - 1], [r, c]]
        else:
            1 / 0

    for move in moves:
        dr, dc = dirs[move]
        curr_r, curr_c = robot
        do_move = True
        shifted_levels: list[list[list[int]]] = [[[curr_r, curr_c]]]

        if dc:
            while 0 <= curr_c + len(shifted_levels) * dc < width:
                last_r, last_c = shifted_levels[-1][0]
                peek = grid[last_r][last_c + dc]
                if peek in "[]":
                    shifted_levels.append([[last_r, last_c + dc]])
                elif peek == "#":
                    do_move = False
                    break
                else:
                    break
        elif dr:
            while 0 <= curr_r + len(shifted_levels) * dr < height:
                peeks = [grid[r + dr][c] for r, c in shifted_levels[-1]]
                if all(peek == "." for peek in peeks):
                    break
                elif any(peek == "#" for peek in peeks):
                    do_move = False
                    break
                else:
                    affected = []
                    for r, c in shifted_levels[-1]:
                        if grid[r + dr][c] in "[]":
                            for br, bc in get_box(r + dr, c, grid):
                                if [br, bc] not in affected:
                                    affected.append([br, bc])
                    shifted_levels.append(affected)

        # print(shifted_levels, do_move, robot)

        if do_move:
            for shiftees in shifted_levels[::-1]:
                for r, c in shiftees:
                    grid[r + dr][c + dc] = grid[r][c]
                    grid[r][c] = "."
            grid[curr_r][curr_c] = "."
            robot = [curr_r + dr, curr_c + dc]

        # print(f"Move {move}:")
        # print("\n".join("".join(row) for row in grid))
        # print("\n")

    res = 0
    for r in range(height):
        for c in range(width):
            if grid[r][c] == "[":
                res += 100 * r + c

    print(res)
