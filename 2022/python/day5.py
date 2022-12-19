with open('inputs/day5.in', 'r') as infile:
    start, _moves = infile.read().split('\n\n')
    *boxes, columns = start.split('\n')
    columns = int(columns.split()[-1])
    stacks = [[] for _ in range(columns)]
    for row in boxes:
        for i in range(columns):
            box = row[4 * i + 1]
            if box != ' ':
                stacks[i].append(box)

    for stack in stacks:
        stack.reverse()

    moves = []
    for row in _moves.split('\n'):
        _, count, _, source, _, dest = row.split()
        moves.append([int(count), int(source) - 1, int(dest) - 1])

for count, source, dest in moves:
    moving = []
    for _ in range(count):
        moving.append(stacks[source].pop())
    stacks[dest].extend(moving[::-1])

print(''.join(stack[-1] for stack in stacks))
