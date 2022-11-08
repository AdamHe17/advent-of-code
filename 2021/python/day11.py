from itertools import product
from pprint import pprint

infile = open('inputs/day11.in', 'r')
lines = infile.readlines()
lines = [list(map(int, line.strip())) for line in lines]
lines2 = lines[:]


def get_neighbors(x, y, w=10, h=10):
    res = []
    for i, j in product([-1, 0, 1], [-1, 0, 1]):
        if 0 <= x + i < w and 0 <= y + j < h and (i, j) != (0, 0):
            res.append((x + i, y + j))

    return res


# Part 1

DAYS = 100
res = 0

for _ in range(DAYS):
    new_day = [[lines[i][j] + 1 for j in range(10)] for i in range(10)]

    flashes = [(i, j) for i, j in product(range(10), range(10))
               if new_day[i][j] == 10]
    while flashes:
        i, j = flashes.pop(0)
        new_day[i][j] = 0
        res += 1
        for n_i, n_j in get_neighbors(i, j):
            curr = new_day[n_i][n_j]
            if curr == 0 or curr == 10:
                continue
            else:
                new_day[n_i][n_j] += 1

            if new_day[n_i][n_j] == 10:
                flashes.append((n_i, n_j))

    lines = new_day

print(res)

# Part 2

res = 0

while sum(map(sum, lines2)) > 0:
    new_day = [[lines2[i][j] + 1 for j in range(10)] for i in range(10)]

    flashes = [(i, j) for i, j in product(range(10), range(10))
               if new_day[i][j] == 10]
    while flashes:
        i, j = flashes.pop(0)
        new_day[i][j] = 0
        for n_i, n_j in get_neighbors(i, j):
            curr = new_day[n_i][n_j]
            if curr == 0 or curr == 10:
                continue
            else:
                new_day[n_i][n_j] += 1

            if new_day[n_i][n_j] == 10:
                flashes.append((n_i, n_j))

    res += 1
    lines2 = new_day

print(res)