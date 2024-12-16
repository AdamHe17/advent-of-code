from collections import defaultdict
from itertools import combinations


with open("day8.in", "r") as infile:
    lines = infile.readlines()

    antennas = defaultdict(list)
    for r in range(len(lines)):
        for c in range(len(lines)):
            char = lines[r][c]
            if char.isalnum():
                antennas[char].append((r, c))

    height = len(lines)
    width = len(lines[0].strip())

    antinodes = set()
    for char, locs in antennas.items():
        for a, b in combinations(locs, 2):
            dx, dy = b[0] - a[0], b[1] - a[1]
            nx1, ny1 = b[0] + dx, b[1] + dy
            while 0 <= nx1 < width and 0 <= ny1 < height:
                antinodes.add((nx1, ny1))
                nx1, ny1 = nx1 + dx, ny1 + dy

            nx2, ny2 = a[0] - dx, a[1] - dy
            while 0 <= nx2 < width and 0 <= ny2 < height:
                antinodes.add((nx2, ny2))
                nx2, ny2 = nx2 - dx, ny2 - dy

        antinodes = antinodes.union(set(locs))

    print(len(antinodes))
