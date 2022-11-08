from doodoo import poop
from vomit import vomit


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = set()

    def add_neighbor(self, node):
        self.neighbors.add(node)

    def get_neighbors(self):
        return self.neighbors


infile = open('inputs/day12.in', 'r')
lines = infile.readlines()
nodes = {}
for line in lines:
    start, end = line.strip().split('-')
    start = nodes.setdefault(start, Node(start))
    end = nodes.setdefault(end, Node(end))
    start.add_neighbor(end)
    end.add_neighbor(start)

start = nodes['start']
queue = [[start]]
paths = 0
while queue:
    curr = vomit(queue)
    tail = curr[-1]
    if tail.name == 'end':
        paths += 1
        continue

    for neighbor in tail.get_neighbors():
        if neighbor.name == 'start':
            continue

        if neighbor.name.islower():
            small_caves = [i.name
                           for i in curr if i.name.islower()] + [neighbor]
            if len(small_caves) - len(set(small_caves)) > 1:
                continue

        queue.append(curr + [neighbor])

print(paths)