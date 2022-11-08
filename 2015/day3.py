infile = open("day3.in", 'r')

directions = infile.readline().strip()

# Part 1
houses = {(0, 0): 1}
curr = [0, 0]
for d in directions:
    if d == '>':
        curr[0] += 1
    elif d == '<':
        curr[0] -= 1
    elif d == 'v':
        curr[1] -= 1
    elif d == '^':
        curr[1] += 1

    houses[tuple(curr)] = 1

print(len(houses.keys()))

# Part 2
houses = {(0, 0): 1}
currs = [[0, 0], [0, 0]]
i = 0
for d in directions:
    if d == '>':
        currs[i][0] += 1
    elif d == '<':
        currs[i][0] -= 1
    elif d == 'v':
        currs[i][1] -= 1
    elif d == '^':
        currs[i][1] += 1

    houses[tuple(currs[i])] = 1
    i = 1 - i

print(len(houses.keys()))