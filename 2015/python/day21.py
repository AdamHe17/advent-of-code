from math import ceil
from itertools import permutations

weapons = {(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)}
armors = {(0, 0, 0), (13, 0, 1), (31, 0, 2),
          (53, 0, 3), (75, 0, 4), (102, 0, 5)}
rings = {(0, 0, 0), (0, 0, 0), (25, 1, 0), (50, 2, 0), (100, 3, 0),
         (20, 0, 1), (40, 0, 2), (80, 0, 3)}

my_stats = [100, 0, 0]  # hp, atk, armor
with open('inputs/day21.in', 'r') as infile:
    boss_stats = [int(infile.readline().split(': ')[1]) for _ in range(3)]

print(my_stats, boss_stats)


def can_beat_boss(my_stats, boss_stats):
    if my_stats[1] - boss_stats[2] <= 0:
        return False

    if boss_stats[1] - my_stats[2] <= 0:
        return True

    turns_to_kill_boss = ceil(boss_stats[0]/(my_stats[1]-boss_stats[2]))
    turns_to_kill_me = ceil(my_stats[0] / (boss_stats[1] - my_stats[2]))
    return turns_to_kill_boss <= turns_to_kill_me


min_cost = 1e10
max_cost = -1
for wc, wd, wa in weapons:
    for ac, ad, aa in armors:
        for ((r1c, r1d, r1a), (r2c, r2d, r2a)) in permutations(rings, 2):
            new_stats = my_stats[:]
            new_stats[1] += wd + ad + r1d + r2d
            new_stats[2] += wa + aa + r1a + r2a
            if can_beat_boss(new_stats, boss_stats):
                min_cost = min(min_cost, wc + ac + r1c + r2c)
            else:
                max_cost = max(max_cost, wc + ac + r1c + r2c)

print(min_cost, max_cost)
