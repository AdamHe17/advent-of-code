with open('inputs/day24.in', 'r') as infile:
    weights = [int(line) for line in infile.readlines()]
    weights.sort()
    weights.reverse()
    target = sum(weights) // 4

min_size = 5
candidates = set()
def divide_gifts(curr, weights):
    global min_size, candidates
    if sum(curr) == target:
        if len(curr) < min_size:
            min_size = len(curr)
            candidates = set()

        if len(curr) == min_size:
            candidates.add(tuple(curr))

    if len(curr) >= min_size:
        return

    if not weights:
        return

    heaviest = weights[0]
    divide_gifts(curr + [heaviest], weights[1:])
    divide_gifts(curr, weights[1:])

divide_gifts([], weights)
print(candidates)
results = set()
for candidate in candidates:
    res = 1
    for i in candidate:
        res *= i
    results.add(res)
print(results)
print(min(results))