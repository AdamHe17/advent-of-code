infile = open('inputs/day10.in', 'r')
lines = infile.read().split('\n')

get_error = lambda x: {')': 3, ']': 57, '}': 1197, '>': 25137}[x]
get_score = lambda x: ' )]}>'.index(x)
get_close = lambda x: ')]}>'['([{<'.index(x)]


def is_corrupt(line):
    stack = []
    for i in line:
        if i in '({[<':
            stack.append(i)
        else:
            if not stack or '({[<'.index(stack[-1]) != ')}]>'.index(i):
                return i
            else:
                stack = stack[:-1]

    return False


print(sum(get_error(is_corrupt(line)) for line in lines if is_corrupt(line)))


def get_stack(line):
    stack = []
    for i in line:
        if i in '({[<':
            stack.append(i)
        else:
            stack = stack[:-1]

    return stack


incomplete = [line for line in lines if not is_corrupt(line)]
scores = []
for line in incomplete:
    close = [get_close(i) for i in get_stack(line)][::-1]
    scores.append(int(''.join(str(get_score(i)) for i in close), 5))

scores.sort()
print(scores[len(scores) // 2])
