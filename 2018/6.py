infile = open("6.in", 'r')

positions = [list(map(int, n.split(", "))) for n in infile.readlines()]

graph = {}

def manhattan_dist(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

_ord = 65
for i, pos in enumerate(positions):
    letter = chr(_ord + i)
    print(letter, pos)

    for y in range(max_y):
        for x in range(max_x):
            curr_score = graph[y][x][1]
            new_score = manhattan_dist(pos, [y, x])
            if new_score == curr_score:
                graph[y][x] = ('.', curr_score)
            elif new_score < curr_score:
                graph[y][x] = (letter, new_score)
