with open('inputs/day1.in', 'r') as infile:
    directions = infile.readline().split(', ')
    directions = [(d, int(''.join(v))) for d, *v in directions]

dirs = 'NESW'
offsets = [[0,1],[1,0],[0,-1],[-1,0]]

location = [0, 0]
visited = set()
curr_dir = 'N'
for d, val in directions:
    if d == 'R':
        curr_dir = dirs[(dirs.index(curr_dir)+1)%4]
    elif d == 'L':
        curr_dir = dirs[(dirs.index(curr_dir)-1)%4]

    a, b = offsets[dirs.index(curr_dir)]
    if a:
        for i in range(val):
            location[0] += 1 * a
            if tuple(location) in visited:
                print(sum(location))
                1/0
            visited.add(tuple(location))
    elif b:
        for i in range(val):
            location[1] += 1 * b
            if tuple(location) in visited:
                print(sum(location))
                1/0
            visited.add(tuple(location))

print(sum(location))