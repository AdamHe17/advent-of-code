import re

with open("day14.in", "r") as infile:
    lines = [line.strip() for line in infile.readlines()]

    TEST = False
    MOVES = 10

    robots = []
    for line in lines:
        p0, p1, v0, v1 = map(
            int, re.findall("p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)[0]
        )
        robots.append((p0, p1, v0, v1))

    width = 11 if TEST else 101
    height = 7 if TEST else 103

    for MOVES in range(1000000):
        # end_pos = [[], [], [], []]
        image = [["."] * width for _ in range(height)]
        for c, r, dc, dr in robots:
            quadrant = 0
            end_r = (r + dr * MOVES) % height
            end_c = (c + dc * MOVES) % width

            # if end_r == height // 2 or end_c == width // 2:
            #     continue

            # if end_r > height // 2:
            #     quadrant += 2

            # if end_c > width // 2:
            #     quadrant += 1

            # end_pos[quadrant].append((end_r, end_c))
            image[end_r][end_c] = "#"

        # res = 1
        # for lst in end_pos:
        #     res *= len(lst)

        if any("##########" in "".join(row) for row in image):
            print(MOVES)
            print("\n".join(["".join(row) for row in image]))
            print(
                "\n\n----------------------------------------------------------------\n\n"
            )
            break

    # print(res)
