with open('inputs/day18.in', 'r') as infile:
    grid = [list(line) for line in infile.readlines()]
grid[0][0] = '#'
grid[0][99] = '#'
grid[99][99] = '#'
grid[99][0] = '#'


def get_neighbors(r, c):
    dirs = ([0, 1], [0, -1], [1, 0], [-1, 0],
            [1, 1], [1, -1], [-1, -1], [-1, 1])
    candidates = [[r+x, c+y] for x, y in dirs]
    return [[r, c]for r, c in candidates if 0 <= r < 100 and 0 <= c < 100]


steps = 100
for _ in range(steps):
    new_grid = [['.']*100 for _ in range(100)]
    for r in range(100):
        for c in range(100):
            neighbors = [grid[x][y]
                         for x, y in get_neighbors(r, c)].count('#')
            if grid[r][c] == '#' and 2 <= neighbors <= 3:
                new_grid[r][c] = '#'
            elif grid[r][c] == '.' and neighbors == 3:
                new_grid[r][c] = '#'
    grid = new_grid
    grid[0][0] = '#'
    grid[0][99] = '#'
    grid[99][99] = '#'
    grid[99][0] = '#'

print(sum(row.count('#') for row in grid))
