from collections import defaultdict, deque
from itertools import combinations
from functools import lru_cache
from math import log10


with open("day22.in", "r") as infile:
    lines = [line.strip() for line in infile.readlines()]

    secrets = [int(i) for i in lines]

    def mix(secret, val):
        return secret ^ val

    def prune(secret):
        return secret % 16777216

    def next_secret(secret):
        val = secret * 64
        secret = mix(secret, val)
        secret = prune(secret)

        val = secret // 32
        secret = mix(secret, val)
        secret = prune(secret)

        val = secret * 2048
        secret = mix(secret, val)
        secret = prune(secret)

        return secret

    def digits(n):
        return n % 10

    prices = defaultdict(dict)
    for seller, s in enumerate(secrets):
        diff_window = deque()
        for _ in range(2000):
            ns = next_secret(s)
            diff_window.append(digits(ns) - digits(s))
            if len(diff_window) >= 4:
                d = prices[tuple(diff_window)]
                if seller not in d:
                    d[seller] = digits(ns)
                diff_window.popleft()
            s = ns

    print(max(sum(d.values()) for d in prices.values()))
