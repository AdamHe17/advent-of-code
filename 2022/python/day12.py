from collections import deque

with open('inputs/day12.in', 'r') as infile:
    maze = []
    for row, line in enumerate(infile.read().splitlines()):
        maze.append(list(line))
        for col in range(len(line)):
            if line[col] == 'S':
                start = row, col
                maze[row][col] = 'a'
            elif line[col] == 'E':
                end = row, col
                maze[row][col] = 'z'

    height = len(maze)
    width = len(maze[0])


def get_neighbors(r, c, width, height):
    res = []
    for r, c in [[r, c+1], [r, c-1], [r+1, c], [r-1, c]]:
        if r < 0 or r >= height or c < 0 or c >= width:
            continue
        res.append([r, c])
    return res


queue = deque([(*start, 0)])
visited = {}
while queue:
    r, c, dist = queue.popleft()
    if (r, c) == end:
        print(dist)
        break

    if (r, c) in visited:
        continue
    visited[(r, c)] = dist

    # print(dist)
    for nr, nc in get_neighbors(r, c, width, height):
        if ord(maze[nr][nc]) - ord(maze[r][c]) <= 1:
            queue.append((nr, nc, dist + 1))


queue = deque([(*end, 0)])
visited = {}
while queue:
    r, c, dist = queue.popleft()
    if maze[r][c] == 'a':
        print(dist)
        break

    if (r, c) in visited:
        continue
    visited[(r, c)] = dist

    # print(dist)
    for nr, nc in get_neighbors(r, c, width, height):
        if -ord(maze[nr][nc]) + ord(maze[r][c]) <= 1:
            queue.append((nr, nc, dist + 1))
