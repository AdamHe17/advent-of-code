infile = open('day6.in', 'r')

grid = [[0 for i in range(1000)] for j in range(1000)]


def turn_on(x, y):
    grid[x][y] += 1


def turn_off(x, y):
    grid[x][y] = max(0, grid[x][y] - 1)


def toggle(x, y):
    grid[x][y] += 2


for line in infile.readlines():
    line = line.split()
    start, end = line[-3], line[-1]
    sx, sy = map(int, start.split(','))
    ex, ey = map(int, end.split(','))

    if line[0] == 'toggle':
        func = toggle
    else:
        if line[1] == 'on':
            func = turn_on
        elif line[1] == 'off':
            func = turn_off

    for x in range(sx, ex + 1):
        for y in range(sy, ey + 1):
            func(x, y)

print(sum([sum(r) for r in grid]))
