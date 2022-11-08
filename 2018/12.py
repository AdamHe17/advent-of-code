infile = open("12.in", 'r')

INITIAL_STATE = infile.readline().split(": ")[1]
infile.readline()
RULES = [line.strip().split(" => ") for line in infile.readlines()]
rules = {}
for predicate, res in RULES:
    rules[predicate] = res

next = ""
