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


# target = 2900000
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
queue = [(0, {})]
seen = set()
minimum_seen = 1e20
while queue:
    sigma_val, factors = heappop(queue)

    if product(factors) > minimum_seen:
        continue

    if sigma_val >= target:
        print(factors, sigma(factors), product(factors))
        minimum_seen = min(minimum_seen, product(factors))
        continue

    for prime in primes:
        new_factors = {k: v for k, v in factors.items()}
        new_factors.setdefault(prime, 0)
        new_factors[prime] += 1

        new_sigma = sigma(new_factors)
        prod = product(new_factors)
        if (prod, new_sigma) in seen:
            continue

        seen.add((prod, new_sigma))
        heappush(queue, (new_sigma, new_factors))
