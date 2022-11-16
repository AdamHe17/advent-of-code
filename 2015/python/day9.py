from collections import deque

with open('inputs/day9.in', 'r') as infile:
    cities = set()
    distances = {}
    for line in infile.readlines():
        source, _, dest, _, dist = line.split()
        cities.add(source)
        cities.add(dest)
        distances[(source, dest)] = int(dist)
        distances[(dest, source)] = int(dist)

start = next(iter(cities))
queue = deque([[[start], []]])
loops = []
while queue:
    path, dists = queue.popleft()
    last_city = path[-1]
    if len(path) == len(cities):
        loops.append(dists + [distances[(last_city, start)]])
        continue

    for city in cities:
        if city in path:
            continue

        queue.append([path + [city], dists + [distances[(last_city, city)]]])

print(min(sum(i) - max(i) for i in loops))
print(max(sum(i) - min(i) for i in loops))
