with open('inputs/day17.in', 'r') as infile:
    instructions = infile.readline().strip()
    length = len(instructions)
    rocks = [
        [[0, 0], [1, 0], [2, 0], [3, 0]],
        [[1, 0], [0, 1], [1, 1], [2, 1], [1, 2]],
        [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2]],
        [[0, 0], [0, 1], [0, 2], [0, 3]],
        [[0, 0], [1, 0], [0, 1], [1, 1]]
    ]
    rock_peaks = [0, 4, 4, 3, 2]


def can_move_side(rock, rock_locations, direction):
    new_rock = [(x+(1 if direction == '>' else -1), y) for x, y in rock]
    return new_rock if all(0 <= rock[0] < 7 and rock not in rock_locations for rock in new_rock) else rock


def can_move_down(rock, rock_locations):
    return all(y-1 >= 0 and (x, y-1) not in rock_locations for x, y in rock)


def pprint(rock_locations):
    height = max(y for _, y in rock_locations) + 1
    graph = [['.']*7 for _ in range(height)]
    for x, y in rock_locations:
        graph[height - y - 1][x] = '#'
    print(*[''.join(row) for row in graph], sep='\n')


target = 1_000_000_000_000  # 1_000_000_000_000
q, r = divmod(target, 1730)
# q, r = divmod(target, 35)
print(q, r)
# print(2647 * (q) + 2845)
print(2647 * q + 212 + 1)
# 1/0

highest_rock = -1
curr_rock = 0
curr_instr = 0
last_highest = 0
last_rock_count = 0
rock_locations = set()
for rock_count in range(5330):
    # if rock_count == r + 4 * 1730:
    #     print(rock_count, rock_count - last_rock_count)
    #     last_rock_count = rock_count
    #     print(highest_rock, highest_rock - last_highest)
    #     last_highest = highest_rock
    #     print()
    #     print(r + q * 1730)
    #     print(2647 * (q-1) + 2845)
    #     1/0

    if rock_count % 1730 == 140:
        print(rock_count, rock_count - last_rock_count)
        last_rock_count = rock_count
        print(highest_rock, highest_rock - last_highest)
        last_highest = highest_rock
        print()
        # 1/0

    rock = [[x + 2, y + highest_rock + 4] for x, y in rocks[curr_rock]]
    while True:
        # if curr_rock == 0:
        #     print(rock_count, rock_count - last_rock_count)
        #     last_rock_count = rock_count
        #     print(highest_rock, highest_rock - last_highest)
        #     last_highest = highest_rock
        #     print()

        instr = instructions[curr_instr]
        rock = can_move_side(rock, rock_locations, instr)
        curr_instr = (curr_instr + 1) % length

        if can_move_down(rock, rock_locations):
            rock = [(x, y-1) for x, y in rock]
        else:
            break

    for x, y in rock:
        rock_locations.add((x, y))
    highest_rock = max(highest_rock, rock[rock_peaks[curr_rock]][1])
    curr_rock = (curr_rock + 1) % 5

print(highest_rock + 1)
