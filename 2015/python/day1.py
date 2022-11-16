infile = open("day1.in", 'r')

parens = infile.readline()

print(parens.count("(") - parens.count(")"))

i = 0
curr = 0
while i < len(parens):
    curr += [-1, 1][parens[i] == '(']
    if curr < 0:
        print(i + 1)
        break

    i += 1
