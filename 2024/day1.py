from collections import defaultdict

with open("day1.in", "r") as infile:
    lines = infile.readlines()

    lst1 = []
    lst2 = []
    for line in lines:
        a, b = map(int, line.split())
        lst1.append(a)
        lst2.append(b)

    lst1.sort()
    lst2.sort()
    res = sum(abs(a - b) for a, b in zip(lst1, lst2))
    print(res)

with open("day1.in", "r") as infile:
    lines = infile.readlines()

    lst = []
    counts: dict[int, int] = defaultdict(lambda: 0)
    for line in lines:
        a, b = map(int, line.split())
        lst.append(a)
        counts[b] += 1

    res = sum(a * counts[a] for a in lst)
    print(res)
