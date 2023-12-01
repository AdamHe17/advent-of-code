with open("day1.in", "r") as infile:
    lines = infile.readlines()

digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

res = 0
for line in lines:
    ds = [(i, int(v)) for i, v in enumerate(line) if v.isdigit()]
    if ds:
        firstd, lastd = ds[0], ds[-1]

    first_spelled = [(line.find(i), digits[i]) for i in digits if line.find(i) > -1]
    if first_spelled:
        first_spelled = sorted(first_spelled)[0]

    last_spelled = [(line.rfind(i), digits[i]) for i in digits if line.rfind(i) > -1]
    if last_spelled:
        last_spelled = sorted(last_spelled)[-1]

    first = (
        firstd
        if ds and (not first_spelled or firstd[0] < first_spelled[0])
        else first_spelled
    )
    last = (
        lastd
        if ds and (not last_spelled or lastd[0] > last_spelled[0])
        else last_spelled
    )
    res += 10 * first[1] + last[1]

print(res)
