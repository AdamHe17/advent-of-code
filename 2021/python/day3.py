infile = open('inputs/day3.in', 'r')

lines = infile.readlines()
lines = list(map(lambda x: x.strip(), lines))
lines2 = lines.copy()

ind = 0
while len(lines) > 1:
    zeros = sum(1 for i in lines if i[ind] == '0')
    ones = sum(1 for i in lines if i[ind] == '1')

    more = '0' if zeros > ones else '1'

    lines = list(filter(lambda x: x[ind] == more, lines))

    ind += 1

most = lines[0]

lines = lines2
ind = 0
while len(lines) > 1:
    zeros = sum(1 for i in lines if i[ind] == '0')
    ones = sum(1 for i in lines if i[ind] == '1')

    less = '1' if ones < zeros else '0'

    lines = list(filter(lambda x: x[ind] == less, lines))

    ind += 1

least = lines[0]

print(int(most, 2) * int(least, 2))
