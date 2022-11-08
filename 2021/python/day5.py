infile = open('inputs/day5.in', 'r')
lines = infile.readlines()

grid = {}

for line in lines:
    start, end = line.split(' -> ')
    x1, y1 = map(int, start.split(','))
    x2, y2 = map(int, end.split(','))

    if x1 != x2 and y1 != y2:
        continue

    if x1 == x2:
        if y1 > y2:
            x1, y1, x2, y2 = x2, y2, x1, y1

        for y in range(y1, y2 + 1):
            grid.setdefault((x1, y), 0)
            grid[(x1, y)] += 1

    if y1 == y2:
        if x1 > x2:
            x1, y1, x2, y2 = x2, y2, x1, y1

        for x in range(x1, x2 + 1):
            grid.setdefault((x, y1), 0)
            grid[(x, y1)] += 1

res = sum(1 for k, v in grid.items() if v >= 2)
print(res)

# Diagonal lines
for line in lines:
    start, end = line.split(' -> ')
    x1, y1 = map(int, start.split(','))
    x2, y2 = map(int, end.split(','))

    if y2 - y1 == x2 - x1:
        if x1 > x2:
            x1, y1, x2, y2 = x2, y2, x1, y1

        for i in range(x2 - x1 + 1):
            grid.setdefault((x1 + i, y1 + i), 0)
            grid[(x1 + i, y1 + i)] += 1

    if y2 - y1 == x1 - x2:
        if x1 > x2:
            x1, y1, x2, y2 = x2, y2, x1, y1

        for i in range(x2 - x1 + 1):
            grid.setdefault((x1 + i, y1 - i), 0)
            grid[(x1 + i, y1 - i)] += 1

res = sum(1 for k, v in grid.items() if v >= 2)
print(res)