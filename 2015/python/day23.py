with open('inputs/day23.in', 'r') as infile:
    instructions = []
    for line in infile.readlines():
        instruction, *args = line.split()
        if ',' in args[0]:
            args[0] = args[0][:-1]
        instructions.append((instruction, args))

a, b = 1, 0
pointer = 0
while 0 <= pointer < len(instructions):
    instr, args = instructions[pointer]
    if instr == 'hlf':
        exec(f'{args[0]}//=2')
        pointer += 1
    elif instr == 'tpl':
        exec(f'{args[0]}*=3')
        pointer += 1
    elif instr == 'inc':
        exec(f'{args[0]}+=1')
        pointer += 1
    elif instr == 'jmp':
        exec(f'pointer+={args[0]}')
    elif instr == 'jie':
        exec(f'pointer+={args[1]} if {args[0]}%2==0 else 1')
    else:
        exec(f'pointer+={args[1]} if {args[0]}==1 else 1')

print(a, b)