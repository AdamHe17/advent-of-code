with open('inputs/day22.in') as infile:
    maze, directions = infile.read().split('\n\n')
    maze = maze.splitlines()
    rows, cols = len(maze), max(len(line) for line in maze)
    _map = [[' ']* cols for _ in range(rows)]
    for row, line in enumerate(maze):
        for col, value in enumerate(line):
            _map[row][col] = value
    directions = directions.replace('R',' R ').replace('L',' L ').split()
    directions = [int(dir) if dir.isdigit() else dir for dir in directions]

direction = 0
offset = [[0, 1], [1, 0], [0, -1], [-1, 0]]
start = [0]
for col, value in enumerate(_map[0]):
    if value == '.':
        start.append(col)
        break

print(start)

def maybe_set_new_direction(row, col, direction):
    # Each side is 50x50
    # directions are right=0, down=1, left=2, up=3
    res = (row, col, direction)
    if direction == 0:
        if row < 50 and col == 0:
            res = (149 - row, 99, 2)
        if 50 <= row < 100 and col == 100:
            res = (49, row + 50, 3)#
        if 100 <= row < 150 and col == 100:
            res = (149 - row, 149, 2)
        if 150 <= row < 200 and col == 50:
            res = (149, row - 100, 3)#
    elif direction == 1:
        if col < 50 and row == 0:
            res = (0, col + 100, 1)#
        if 50 <= col < 100 and row == 150:
            res = (col + 100, 49, 2)#
        if 100 <= col < 150 and row == 50:
            res = (col - 50, 99, 2)#
    elif direction == 2:
        if row < 50 and col == 49:
            res = (149 - row, 0, 0)
        if 50 <= row < 100 and col == 49:
            res = (100, row - 50, 1)#
        if 100 <= row < 150 and col == 149:
            res = (149 - row, 50, 0)
        if 150 <= row < 200 and col == 149:
            res = (0, row - 100, 1)#
    elif direction == 3:
        if col < 50 and row == 99:
            res = (col + 50, 50, 0)#
        if 50 <= col < 100 and row == 199:
            res = (col + 100, 0, 0)#
        if 100 <= col < 150 and row == 199:
            res = (199, col - 100, 3)#

    # if res != (row, col, direction):
    #     print('original', (row, col, direction))
    #     print('change  ', res)
    return res


for dir in directions:
    if isinstance(dir, int):
        rcurr, ccurr = start
        for _ in range(dir):
            roffset, coffset = offset[direction]
            rnext, cnext = (rcurr + roffset) % rows, (ccurr + coffset) % cols
            rnext, cnext, ndirection = maybe_set_new_direction(rnext, cnext, direction)
            if _map[rnext][cnext] == '.':
                rcurr, ccurr = rnext, cnext
                direction = ndirection
            else:
                break
        start = [rcurr, ccurr]
    else:
        direction = (direction + (1 if dir == 'R' else -1)) % 4

r, c = start
print(r + 1, c + 1, direction)
print(1000 * (r + 1) + 4 * (c + 1) + direction)