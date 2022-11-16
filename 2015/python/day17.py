with open('inputs/day17.in', 'r') as infile:
    containers = [int(i) for i in infile.readlines()]

fits_by_count = {}


def fits(total, containers, count=0):
    if total == 0:
        fits_by_count.setdefault(count, 0)
        fits_by_count[count] += 1
        return 1

    if total < 0:
        return 0

    if not containers:
        return 0

    res = 0
    for i, v in enumerate(containers):
        if v <= total:
            res += fits(total - v, containers[:i], count + 1)

    return res


total = 150
print(fits(total, sorted(containers)))
print(fits_by_count)
