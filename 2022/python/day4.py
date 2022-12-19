with open('inputs/day4.in', 'r') as infile:
    ranges = []
    for line in infile.readlines():
        range1, range2 = line.split(',')
        a, b = map(int, range1.split('-'))
        c, d = map(int, range2.split('-'))
        ranges.append([a, b, c, d])

covers = 0
for a, b, c, d in ranges:
    if a <= c and b >= d:
        covers += 1
    elif c <= a and d >= b:
        covers += 1

print(covers)

overlaps = 0
for a, b, c, d in ranges:
    if b < c or d < a:
        continue
    overlaps += 1

print(overlaps)
