from collections import defaultdict, deque
from itertools import combinations


with open("day23.in", "r") as infile:
    lines = [line.strip() for line in infile.readlines()]

    connections = defaultdict(set)
    computers = set()
    for line in lines:
        a, b = line.split("-")
        connections[a].add(b)
        connections[b].add(a)
        computers.add(a)
        computers.add(b)

    lan: dict[tuple, set] = {}
    for a, b, c in combinations(computers, 3):
        if a in connections[b] and c in connections[b] and a in connections[c]:
            lan[(a, b, c)] = set.intersection(
                connections[a], connections[b], connections[c]
            )

    while len(lan) > 1:
        new_lan: dict[tuple, set] = {}
        visited = set()
        for t, cands in lan.items():
            for s in cands:
                k = tuple(sorted((*t, s)))
                if k in visited:
                    continue
                visited.add(k)
                new_lan[(*t, s)] = cands.intersection(connections[s])
        lan = new_lan
        if len(lan) == 1:
            print(",".join(k))
