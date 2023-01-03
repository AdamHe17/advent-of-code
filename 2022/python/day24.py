from collections import defaultdict

with open('inputs/day24.in') as infile:
    lines = infile.read().splitlines()

height = len(lines)
width = len(lines[0])
start = (0, 1)
end = (height - 1, width - 2)

def get_neighbors(pos):
    row, col = pos
    candidates = set([(row+1,col),(row-1,col),(row,col+1),(row,col-1)])
    res = set()
    for r, c in candidates:
        if (r, c) == start or (r, c) == end:
            res.add((r, c))
        elif 1 <= r < height - 1 and 1 <= c < width - 1:
            res.add((r, c))
    return res

winds = defaultdict(lambda: set())
for row in range(height):
    for col in range(width):
        winds[lines[row][col]].add((row, col))

rights, downs, lefts, ups = winds['>'], winds['v'], winds['<'], winds['^']
horizontal_winds = []
vertical_winds = []

for _ in range(width - 2):
    horizontal_winds.append(rights.union(lefts))
    rights = set((row, (col % (width - 2) + 1)) for row, col in rights)
    lefts = set((row, ((col - 2) % (width - 2) + 1)) for row, col in lefts)

for _ in range(height - 2):
    vertical_winds.append(ups.union(downs))
    ups = set((((row - 2) % (height - 2) + 1), col) for row, col in ups)
    downs = set(((row % (height - 2) + 1), col) for row, col in downs)

def get_travel_time(start, end, start_time=0):
    minute = start_time
    positions = set([start])
    while True:
        new_positions = set()
        winds = horizontal_winds[minute % (width - 2)].union(vertical_winds[minute % (height - 2)])
        for position in positions:
            if position == end:
                return minute - 1

            if position not in winds:
                new_positions.add(position)

            for neighbor in get_neighbors(position):
                if neighbor not in winds:
                    new_positions.add(neighbor)

        positions = new_positions
        minute += 1

first_stop = get_travel_time(start, end, start_time=0)
second_stop = get_travel_time(end, start, start_time=first_stop)
third_stop = get_travel_time(start, end, start_time=second_stop)
print(first_stop)
print(third_stop)