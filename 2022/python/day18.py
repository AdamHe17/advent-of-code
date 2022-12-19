from collections import defaultdict, deque

with open('inputs/day18.in', 'r') as infile:
    cubes = set()
    for line in infile.read().splitlines():
        x, y, z = map(int, line.split(','))
        cubes.add((x, y, z))

directions = [
    [0, 0, 1],
    [0, 0, -1],
    [1, 0, 0],
    [-1, 0, 0],
    [0, 1, 0],
    [0, -1, 0]
]

# Part 1


def get_sa(cube):
    x, y, z = cube
    return sum((x+xoffset, y+yoffset, z+zoffset) not in cubes for xoffset, yoffset, zoffset in directions)


print(sum(map(get_sa, cubes)))

# Part 2
mins = [float('inf')]*3
maxs = [-1] * 3
for cube in cubes:
    for i in range(3):
        mins[i] = min(mins[i], cube[i])
        maxs[i] = max(maxs[i], cube[i])


def inside_bounds(cube, mins, maxs):
    return all(mins[i] <= cube[i] <= maxs[i] for i in range(3))


def get_neighbors(cube):
    x, y, z = cube
    return set((x+xoffset, y+yoffset, z+zoffset) for xoffset, yoffset, zoffset in directions)


def get_exterior_sa(cube):
    assert cube not in cubes
    x, y, z = cube
    return sum((x+xoffset, y+yoffset, z+zoffset) in cubes for xoffset, yoffset, zoffset in directions)


mins = [i - 1 for i in mins]
maxs = [i + 1 for i in maxs]
queue = deque([tuple(i for i in mins)])
total_exterior_sa = 0
visited = set()
while queue:
    curr = queue.popleft()
    if curr in cubes:
        continue

    if not inside_bounds(curr, mins, maxs):
        continue

    if curr in visited:
        continue
    visited.add(curr)

    total_exterior_sa += get_exterior_sa(curr)
    for neighbor in get_neighbors(curr):
        queue.append(neighbor)

print(total_exterior_sa)
