from collections import deque, defaultdict
from functools import lru_cache

with open("day19.in", "r") as infile:
    _towels, _designs = infile.read().split("\n\n")

    towels = set(i.strip() for i in _towels.split(", "))
    designs = [i.strip() for i in _designs.split("\n")]

    @lru_cache
    def possible(design):
        if design == "":
            return 1

        i = 1
        res = 0
        while i < len(design) + 1:
            if design[:i] in towels:
                res += possible(design[i:])
            i += 1
        return res

    res = 0
    for design in designs:
        res += possible(design)

    print(res)
