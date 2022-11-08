from itertools import product

infile = open('inputs/day9.in', 'r')
lines = infile.read().split('\n')
lines = [[int(i) for i in line] for line in lines]
W, H = len(lines), len(lines[0])


def get_neighbors(x, y, w, h):
    return filter(lambda k: 0 <= k[0] < w and 0 <= k[1] < h, [(x + 1, y),
                                                              (x - 1, y),
                                                              (x, y + 1),
                                                              (x, y - 1)])


lowests = [(i, j) for i, j in product(range(W), range(H)) if all(
    lines[i][j] < lines[x][y] for x, y in get_neighbors(i, j, W, H))]

print("Part 1: {}".format(sum(lines[i][j] + 1 for i, j in lowests)))


def get_basin(lines, i, j):
    queue = [(i, j)]
    visited = set()
    size = 0
    while queue:
        curr = queue.pop(0)
        if curr in visited:
            continue

        visited.add(curr)
        size += 1
        queue.extend([(x, y) for x, y in get_neighbors(*curr, W, H)
                      if lines[x][y] < 9 and (x, y) not in visited])

    return size


basins = [get_basin(lines, i, j) for i, j in lowests]

*_, a, b, c = sorted(basins)
print("Part 2: {}".format(a * b * c))
