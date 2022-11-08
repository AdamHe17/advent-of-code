infile = open('day7.in', 'r')
instrs = infile.readlines()

ptrs = {}

for instr in instrs:
    left, right = instr.strip().split(' -> ')
    left = left.split()
    if len(left) == 1:
        arg1 = left[0]
        ptrs[right] = [arg1]
    elif len(left) == 2:
        _, arg1 = left
        ptrs[right] = ['~', arg1]
    elif len(left) == 3:
        arg1, sign, arg2 = left
        op = ['&', '|', '<<', '>>'][['AND', 'OR', 'LSHIFT',
                                     'RSHIFT'].index(sign)]
        ptrs[right] = [arg1, op, arg2]


def get_ptr(x):
    clause = ptrs[x]
    if len(clause) == 1:
        arg1 = clause[0]
        if arg1.isnumeric():
            res = int(arg1)
        else:
            res = get_ptr(arg1)
    elif len(clause) == 2:
        _, arg1 = clause
        if arg1.isnumeric():
            res = ~arg1
        else:
            res = ~get_ptr(arg1)
    else:
        arg1, op, arg2 = clause
        arg1 = int(arg1) if arg1.isnumeric() else get_ptr(arg1)
        arg2 = int(arg2) if arg2.isnumeric() else get_ptr(arg2)
        res = eval('{} {} {}'.format(arg1, op, arg2))

    ptrs[x] = [str(res)]
    return res


res = get_ptr('a')
print(res)