infile = open('day8.in', 'r')

total = 0
for line in infile.readlines():
    line = line.strip()
    res = 4
    i = 0
    while i < len(line):
        if line[i] == '\\':
            if line[i + 1] == '\\' or line[i + 1] == '"':
                res += 2
                i += 1
            elif line[i + 1] == 'x':
                res += 1
                i += 3
        i += 1

    total += res

print(total)
