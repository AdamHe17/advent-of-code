from heapq import heappush, heappop
import heapq

with open('inputs/day20.in', 'r') as infile:
    target = int(infile.readline()) // 10


def sigma(factors):
    res = 1
    for k, v in factors.items():
        res *= sum(k ** i for i in range(v + 1))
    return res


def product(factors):
    res = 1
    for k, v in factors.items():
        res *= k ** v
    return res


target = 29_000_000
houses = [11] * 1_000_000
for i in range(2, 1_000_000):
    j = i
    for _ in range(50):
        if j >= 1_000_000:
            break
        houses[j] += i * 11
        j += i

    if i % 10_000 == 0:
        print(i // 10_000)

for i, v in enumerate(houses):
    if v >= target:
        print(i)
        break