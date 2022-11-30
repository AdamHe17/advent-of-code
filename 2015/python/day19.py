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
        reversed_replacements[v] = k

total_steps = 0
while start != new_target:
    for k, v in reversed_replacements.items():
        index = start.find(k)
        while index > -1:
            total_steps += 1
            start = start[:index] + v + start[index + len(k):]
            index = start.find(k)

print(start, total_steps)