from collections import deque

with open('inputs/day19.in', 'r') as infile:
    *_replacements, _, start = map(lambda x: x.strip(), infile.readlines())
    replacements = {}
    for r in _replacements:
        source, target = r.split(' => ')
        replacements.setdefault(source, set())
        replacements[source].add(target)


def find_all(string, substring):
    l = len(substring)
    i = 0
    while i < len(string) - l + 1:
        if string[i:i+l] == substring:
            yield i
        i += 1


all_iterations = set()
for source, targets in replacements.items():
    for index in find_all(start, source):
        for target in targets:
            all_iterations.add(start[:index]+target+start[index+len(source):])

print(replacements, start)
print(len(all_iterations))

new_target = 'e'
reversed_replacements = {}
for k, vs in replacements.items():
    for v in vs:
        reversed_replacements.setdefault(v, set())
        reversed_replacements[v].add(k)
queue = deque([(start, 0)])
seen = set()
total_steps = 0
while queue:
    curr, steps = queue.popleft()

    total_steps += 1
    if total_steps % 10000 == 0:
        print(f'total_steps={total_steps}')
        print(len(curr), steps)

    if curr == new_target:
        print(f'steps={steps}')
        print(f'total_steps={total_steps}')
        break

    if curr in seen:
        continue
    seen.add(curr)

    for source, targets in reversed_replacements.items():
        for index in find_all(curr, source):
            for target in targets:
                queue.append(
                    (curr[:index]+target+curr[index+len(source):], steps + 1))
