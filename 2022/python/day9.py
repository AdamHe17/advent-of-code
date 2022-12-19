with open('inputs/day9.in', 'r') as infile:
    steps = []
    for line in infile.readlines():
        dir, val = line.strip().split()
        steps.append((dir, int(val)))


def is_close(a, b, x, y):
    return abs(x - a) <= 1 and abs(y - b) <= 1


def steps_towards(a, b, x, y):
    """
    Move a, b towards x, y

    Returns path and new position for a, b
    """
    if is_close(a, b, x, y):
        return [], a, b

    path = []
    if abs(x - a) > 1:
        if a < x:
            towards = 1
        else:
            towards = -1

        if b < y:
            b += 1
        elif b > y:
            b -= 1

        i = 1
        while not is_close(a + towards * i, b, x, y):
            path.append((a + towards * i, b))
            if b < y:
                b += 1
            elif b > y:
                b -= 1
            i += 1
        path.append((a + towards * i, b))
        return path, a + towards * i, b

    path = []
    if abs(y - b) > 1:
        if b < y:
            towards = 1
        else:
            towards = -1

        if a < x:
            a += 1
        elif a > x:
            a -= 1

        i = 1
        while not is_close(a, b + towards * i, x, y):
            path.append((a, b + towards * i))
            if a < x:
                a += 1
            elif a > x:
                a -= 1
            i += 1
        path.append((a, b + towards * i))
        return path, a,  b + towards * i


x, y = 0, 0
a, b = 0, 0
visited = set([(a, b)])
for dir, val in steps:
    if dir == 'U':
        y += val
    elif dir == 'D':
        y -= val
    elif dir == 'L':
        x -= val
    else:
        x += val

    path, a, b = steps_towards(a, b, x, y)
    for coord in path:
        visited.add(coord)

print(len(visited))

x, y = 0, 0
knots = [[0, 0] for _ in range(9)]
visited = set([(0, 0)])
for dir, val in steps:
    for _ in range(val):
        if dir == 'U':
            y += 1
        elif dir == 'D':
            y -= 1
        elif dir == 'L':
            x -= 1
        else:
            x += 1

        knots_with_head = [[x, y]] + knots
        for i in range(1, 10):
            a, b = knots_with_head[i]
            c, d = knots_with_head[i - 1]
            path, a, b = steps_towards(a, b, c, d)
            knots_with_head[i] = [a, b]
            if i == 9:
                for coord in path:
                    visited.add(coord)
        knots = knots_with_head[1:]
        a, b = knots[-1]


print(len(visited))
