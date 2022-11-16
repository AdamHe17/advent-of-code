with open('inputs/day16.in', 'r') as infile:
    aunts = []
    for line in infile.readlines():
        props = line.split()[2:]
        res = {}
        for i in range(3):
            prop, value = props[i*2:i*2+2]
            res[prop[:-1]] = int(value) if value.isdigit() else int(value[:-1])
        aunts.append(res)

tape = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

for i in range(len(aunts)):
    for p, v in aunts[i].items():
        if p in ['cats', 'trees']:
            if v <= tape[p]:
                break
        elif p in ['pomeranians', 'goldfish']:
            if v >= tape[p]:
                break
        elif tape[p] != v:
            break
    else:
        print(i + 1)
