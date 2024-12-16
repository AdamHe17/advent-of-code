from collections import defaultdict
from itertools import combinations


with open("day9.in", "r") as infile:
    lines = [line.strip() for line in infile.readlines()]

    line = lines[0]

    curr = 0
    system = []
    free = False
    values = 0
    sizes: dict[int, tuple[int, int]] = {}
    for i in line:
        char = curr if not free else "."
        for _ in range(int(i)):
            system.append((char, int(i)))
        if not free:
            sizes[curr] = (int(i), len(system) - int(i))
            curr += 1
            values += 1
        free = not free

    for id in range(values - 1, -1, -1):
        print(id)
        size, id_ind = sizes[id]
        for ind, (v, count) in enumerate(system):
            if v != ".":
                continue

            if count < size:
                continue

            for i in range(size):
                system[ind + i] = (id, size)
                system[id_ind + i] = (".", 0)
            for i in range(count - size):
                system[ind + size + i] = (".", count - size)
            break

    res = 0
    for ind, (v, _) in enumerate(system):
        if v == ".":
            continue
        res += ind * v
    print(res)
