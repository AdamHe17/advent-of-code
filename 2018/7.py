infile = open("7.in", 'r')

lines = [n.strip().split(' ') for n in infile.readlines()]
pairs = [[line[1], line[7]] for line in lines]

prereq, graph = {}, {}
for i in range(26):
    graph[chr(65 + i)] = []
    prereq[chr(65 + i)] = []

start_candidates = [0 for _ in range(26)]
for pair in pairs:
    a, b = pair
    start_candidates[ord(b) - 65] = 1
    graph[a].append(b)
    prereq[b].append(a)

start = chr(start_candidates.index(0) + 65)

queue = [start]
result = ""
while len(queue) > 0:
    curr = queue.pop(0)
    result += curr
    next = graph[curr]
    for n in next:
        prereq[n].remove(curr)
        if len(prereq[n]) == 0:
            queue.append(n)

    queue.sort()

print(result)
