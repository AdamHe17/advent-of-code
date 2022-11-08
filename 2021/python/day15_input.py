infile = open("inputs/day15.in", "r")
lines = [[int(i) for i in line.strip()] for line in infile.readlines()]
new_lines = []
for i, line in enumerate(lines):
    new_line = []
    for inc in range(5):
        new_line += [(i - 1 + inc) % 9 + 1 for i in line]
        if i == 0:
            print([(i - 1 + inc) % 9 + 1 for i in line][:6])
    new_lines.append(new_line)

with open('inputs/day15_2.in', 'w') as outfile:
    for inc in range(5):
        for line in new_lines:
            outfile.write(
                ''.join(map(str, [(i - 1 + inc) % 9 + 1 for i in line])) + '\n')
