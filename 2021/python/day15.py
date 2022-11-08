import heapq

infile = open("inputs/day15_2.in", "r")
lines = [[int(i) for i in line.strip()] for line in infile.readlines()]
shortest = [[float('inf') for i in range(len(lines))]
            for _ in range(len(lines))]


def get_neighbors(point, N=10):
    x, y = point
    candidates = [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
    return [(x, y) for x, y in candidates if 0 <= x < N and 0 <= y < N]


end = (len(lines) - 1, len(lines) - 1)

heap = [(0, [[0, 0]])]
while heap:
    dist, path = heapq.heappop(heap)
    tail = path[-1]
    x, y = tail

    if dist >= shortest[x][y]:
        continue
    shortest[x][y] = dist

    if tail == end:
        continue

    neighbors = get_neighbors(tail, N=len(lines))
    for neighbor in neighbors:
        if neighbor in path:
            continue

        x, y = neighbor
        heapq.heappush(heap, (dist + lines[x][y], path + [neighbor]))

print(shortest[-1][-1])
