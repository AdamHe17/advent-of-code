from collections import defaultdict


def blink(stones):
    res = []
    for stone in stones:
        if stone == 0:
            res.append(1)
        elif len(str(stone)) % 2 == 0:
            l = len(str(stone))
            res.extend([int(str(stone)[: l // 2]), int(str(stone)[l // 2 :])])
        else:
            res.append(stone * 2024)

    return res


def blink2(counts):
    res = defaultdict(lambda: 0)
    for val, count in counts.items():
        if val == 0:
            res[1] += count
        elif len(str(val)) % 2 == 0:
            s = str(val)
            l = len(s)
            left = int(s[: l // 2])
            right = int(s[l // 2 :])
            res[left] += count
            res[right] += count
        else:
            res[val * 2024] += count
    return res


with open("day11.in", "r") as infile:
    line = [int(i) for i in infile.readline().strip().split()]
    counts = {i: line.count(i) for i in line}

    for i in range(25):
        line = blink(line)

    print(len(line))

    for i in range(75):
        counts = blink2(counts)

    print(sum(v for v in counts.values()))
