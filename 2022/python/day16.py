from collections import deque

with open('inputs/day16.in', 'r') as infile:
    flows = {}
    graph = {}
    status = {}
    for line in infile.read().splitlines():
        a, b = line.split('; ')
        _, id, _, _, rate = a.split()
        rate = int(rate.split('=')[1])
        flows[id] = rate
        status[id] = False
        graph[id] = set()
        _, _, _, _, *tunnels = b.split(' ')
        for tunnel in tunnels:
            tunnel = tunnel.strip(',')
            graph[id].add(tunnel)


def path_len(id1, id2):
    queue = deque([[id1, 0]])
    visited = set()
    while queue:
        curr, dist = queue.popleft()
        if curr == id2:
            return dist

        if curr in visited:
            continue
        visited.add(curr)
        for neighbor in graph[curr]:
            queue.append((neighbor, dist+1))


valves = set(key for key in flows.keys() if flows[key])
weighted_graph = {}
for k in valves.union(set(['AA'])):
    for j in valves:
        dist = path_len(k, j)
        weighted_graph[(k, j)] = dist
        weighted_graph[(j, k)] = dist

minutes = 26
start = 'AA'
queue = deque([(start, minutes, start, minutes, set(), 0)])
visited = set()
max_flow = 0
while queue:
    me, cd, elephant, ecd, opened, total = queue.popleft()

    state = (tuple(sorted(opened)), total)
    if state in visited:
        continue
    visited.add(state)

    travel = False
    for valve in (valves - opened):
        dist = weighted_graph[(me, valve)] + 1
        if dist <= cd:
            travel = True
            queue.append((valve, cd - dist, elephant, ecd,
                          opened.union(set([valve])), total + (cd - dist) * flows[valve]))

        dist = weighted_graph[(elephant, valve)] + 1
        if dist <= ecd:
            travel = True
            queue.append((me, cd, valve, ecd - dist,
                          opened.union(set([valve])), total + (ecd - dist) * flows[valve]))

    if not travel:
        if total > max_flow:
            max_flow = total
            print(max_flow)

print(max_flow)
