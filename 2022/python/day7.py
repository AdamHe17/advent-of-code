with open('inputs/day7.in', 'r') as infile:
    tokens = iter(infile.read().replace('\n', ' ').split(' '))

total = 0
dirs = {}
curr = []
for token in tokens:
    if token in '$ls':
        continue
    if token == 'cd':
        goto = tokens.__next__()
        curr.pop() if goto == '..' else curr.append(goto)
    else:
        full_path = '/'.join(curr)
        lst = dirs.setdefault(full_path, [0])
        name = tokens.__next__()
        if token.isdigit():
            lst[0] += int(token)
        else:
            lst.append(name)


def size(name):
    return dirs[name][0] + sum(size('/'.join([name, i])) for i in dirs[name][1:])


print(sum(size(k) for k in dirs if size(k) <= 1e5))
print(min([size(k) for k in dirs], key=lambda k: max(
    0, k + 4e7 - size('/')) or 1e9))
