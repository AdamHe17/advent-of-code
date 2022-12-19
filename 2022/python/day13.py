from functools import cmp_to_key

with open('inputs/day13.in', 'r') as infile:
    pairs = []
    _pairs = infile.read().split('\n\n')
    for pair in _pairs:
        a, b = map(eval, pair.split('\n'))
        pairs.append([a, b])


def comp_list(p1, p2):
    i = 0
    while i < len(p1):
        if i >= len(p2):
            return 1

        diff = comp_int(p1[i], p2[i])
        if diff != 0:
            return diff
        i += 1

    return i - len(p2)


def comp_int(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    if isinstance(a, int):
        a = [a]
    if isinstance(b, int):
        b = [b]
    return comp_list(a, b)


# Part 1
res = 0
for i, pair in enumerate(pairs):
    if comp_list(*pair) < 0:
        res += i + 1
print(res)

# Part 2
lst = [[[2]], [[6]]]
for a, b in pairs:
    lst.append(a)
    lst.append(b)

lst.sort(key=cmp_to_key(comp_list))
a = lst.index([[2]]) + 1
b = lst.index([[6]]) + 1
print(a * b)
