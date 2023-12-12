def get_lines(filename):
    with open(filename, 'r') as infile:
        lines = infile.readlines()
    
    return lines

def get_paragraphs(filename):
    with open(filename, 'r') as infile:
        paragraphs = infile.read().split('\n\n')
    
    return paragraphs

instrs, steps = get_paragraphs('day8.in')
instrs = instrs.strip()
_map = {}
for step in steps.split('\n'):
    name, lr = step.split(' = ')
    l, r = lr.split(', ')
    _map[name] = (l[1:], r[:-1])

starts = [i for i in _map.keys() if i[-1] == 'A']

steps = 0
while True:
    for i in instrs:
        if all(s[-1] == 'Z' for s in starts):
            1/0
        
        for ind, s in enumerate(starts):
            if s[-1] == 'Z':
                print(ind, steps, s)

        starts = [_map[s][0 if i == 'L' else 1] for s in starts]
        steps += 1
