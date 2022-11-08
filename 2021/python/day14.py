from collections import defaultdict

infile = open("inputs/day14.in", "r")
template, _rules = infile.read().split("\n\n")

rules = {}
for rule in _rules.split("\n"):
    pair, res = rule.split(" -> ")
    rules[pair] = res

memo = {}
for pair, res in rules.items():
    memo[(pair, 1)] = {pair[0]: 1}
    if res == pair[0]:
        memo[(pair, 1)][res] += 1
    else:
        memo[(pair, 1)][res] = 1


def merge_counts(counts1, counts2):
    res = defaultdict(int)
    res.update(counts1)
    for i in counts2:
        res[i] += counts2[i]

    return res


def get_counts(template, turns):
    res = {}
    for i in range(len(template) - 1):
        res = merge_counts(res, get_pairs(template[i : i + 2], turns))

    memo[(template, turns)] = res

    res[template[-1]] += 1

    return res


def get_pairs(template, turns):
    if (template, turns) in memo:
        return memo[(template, turns)]

    res = {}
    insert = rules[template]
    for t in [template[0] + insert, insert + template[1]]:
        res = merge_counts(res, get_pairs(t, turns - 1))

    memo[(template, turns)] = res
    return res


res = get_counts(template, 10).values()
print(max(res) - min(res))
res = get_counts(template, 40).values()
print(max(res) - min(res))
