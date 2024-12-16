with open("day4.in", "r") as infile:
    lines = infile.readlines()
    padding = 1

    grid = ["." * padding + line.strip() + "." * padding for line in lines]
    width = len(grid[0])
    grid = ["." * width] * padding + grid + ["." * width] * padding
    res = 0
    # for line in grid:
    #     res += line.count("XMAS")
    #     res += line[::-1].count("XMAS")

    # for i in range(len(grid[0])):
    #     line = "".join(grid[j][i] for j in range(len(grid)))
    #     res += line.count("XMAS")
    #     res += line[::-1].count("XMAS")

    target = "MMSSMMSS"
    for r in range(padding, len(grid) - padding):
        for c in range(padding, len(grid[0]) - padding):
            if grid[r][c] == "A":
                sq = (
                    grid[r - 1][c - 1]
                    + grid[r - 1][c + 1]
                    + grid[r + 1][c + 1]
                    + grid[r + 1][c - 1]
                )
                if sq in target:
                    res += 1
            # a = (
            #     grid[r][c]
            #     + grid[r + 1][c + 1]
            #     + grid[r + 2][c + 2]
            #     + grid[r + 3][c + 3]
            # )
            # b = (
            #     grid[r][c]
            #     + grid[r + 1][c - 1]
            #     + grid[r + 2][c - 2]
            #     + grid[r + 3][c - 3]
            # )
            # d = (
            #     grid[r][c]
            #     + grid[r - 1][c - 1]
            #     + grid[r - 2][c - 2]
            #     + grid[r - 3][c - 3]
            # )
            # e = (
            #     grid[r][c]
            #     + grid[r - 1][c + 1]
            #     + grid[r - 2][c + 2]
            #     + grid[r - 3][c + 3]
            # )
            # res += a == "XMAS"
            # res += b == "XMAS"
            # res += d == "XMAS"
            # res += e == "XMAS"
    print(res)
