from collections import deque

with open('inputs/day13.in', 'r') as infile:
    names = set()
    happiness_map = {}
    for line in infile.readlines():
        words = line.split()
        p1 = words[0]
        p2 = words[-1][:-1]
        names.add(p1)
        names.add(p2)
        happiness = int(words[3]) * (1 if words[2] == 'gain' else -1)
        happiness_map[(p1, p2)] = happiness

for name in names:
    happiness_map[(name, 'lemonz')] = 0
    happiness_map[('lemonz', name)] = 0
names.add('lemonz')


first_person = next(iter(names))
queue = deque([[first_person]])
seats = []
while queue:
    path = queue.popleft()
    last_person = path[-1]
    if len(path) == len(names):
        seats.append(path)
        continue

    for person in names:
        if person in path:
            continue

        queue.append(path + [person])

print(max([sum(happiness_map[(p1, p2)] + happiness_map[(p2, p1)]
      for p1, p2 in zip(seat, seat[1:]+[seat[0]])) for seat in seats]))
