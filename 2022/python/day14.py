with open('inputs/day14.in', 'r') as infile:
    maze = [[0]*1000 for _ in range(1000)]
    lines = infile.read().splitlines()
    base_line = 0
    for line in lines:
        coords = []
        for coord in line.split(' -> '):
            x, y = map(int, coord.split(','))
            coords.append((x, y))
            base_line = max(base_line, y)

        for a, b in zip(coords, coords[1:]):
            x1, y1 = a
            x2, y2 = b
            if x1 == x2:
                y1, y2 = sorted([y1, y2])
                for i in range(y1, y2 + 1):
                    maze[i][x1] = 1
            else:
                x1, x2 = sorted([x1, x2])
                for i in range(x1, x2 + 1):
                    maze[y1][i] = 1

base_line += 2
for i in range(1000):
    maze[base_line][i] = 1


def trickle(x, y):
    if maze[y + 1][x] == 0:
        return x, y + 1
    elif maze[y + 1][x-1] == 0:
        return x - 1, y + 1
    elif maze[y + 1][x + 1] == 0:
        return x + 1, y + 1
    else:
        return x, y


start = (500, 0)
total = 0
while True:
    x, y = start
    while (x, y) != trickle(x, y):
        x, y = trickle(x, y)

    if (x, y) == start:
        break

    maze[y][x] = 2
    total += 1

print(total + 1)
