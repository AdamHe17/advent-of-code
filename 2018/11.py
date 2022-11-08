SERIAL = 9221
ROWS, COLS = 300, 300

grid = [[0 for _ in range(300)] for _ in range(300)]

for x in range(1, ROWS + 1):
    for y in range(1, COLS + 1):
        rack = x + 10
        power = rack * y
        power += SERIAL
        power *= rack
        if power < 100:
            power = 0
        else:
            power = (power // 100) % 10
        power -= 5
        grid[x - 1][y - 1] = power

_max = (-1, (-1, -1, -1))
for size in range(1, 300):
    print(size)
    for x in range(300 - size + 1):
        for y in range(300 - size + 1):
            res = 0
            for i in range(x, x + size):
                for j in range(y, y + size):
                    res += grid[i][j]
            if res > _max[0]:
                _max = (res, (x + 1, y + 1, size))

print(_max)
