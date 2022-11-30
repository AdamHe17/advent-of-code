from collections import deque

my_stats = (50, 0, 500)  # hp, atk, mana
with open('inputs/day22.in', 'r') as infile:
    boss_stats = tuple([int(infile.readline().split(': ')[1]) for _ in range(2)] + [0])

print(my_stats, boss_stats)

spells = [  # cost, hp, dmg, armor, mana, turns
    [53, 0, 4, 0, 0, 1],
    [73, 2, 2, 0, 0, 1],
    [113, 0, 0, 7, 0, 6],
    [173, 0, 3, 0, 0, 6],
    [229, 0, 0, 0, 101, 5]
]

min_mana = float('inf')
queue = deque([(my_stats, boss_stats, [], 0)])
while queue:
    me, boss, active_effects, mana_spent = queue.popleft()
    if mana_spent > min_mana:
        continue

    # resolve effects
    new_effects = []
    for effect in active_effects:
        hp, dmg, armor, mana, turns = effect
        me[0] += hp
        boss[0] -= dmg
        me[2] += mana
        turns -= 1
        if turns > 0:
            new_effects.append(effect[:-1] + [turns])

    if boss[0] <= 0:
        min_mana = min(min_mana, mana_spent)
        continue

    # select spells
    for spell in spells:
        if spell[0] > me[2]:
            continue

        cost, *effect = spell
        curr_effects = new_effects[:]
        curr_effects.append(effect)

        # resolve effects again
        new_me = me[:]
        new_boss = boss[:]
        my_armor = 0
        newer_effects = []
        for effect in curr_effects:
            hp, dmg, armor, mana, turns = effect
            new_me[0] += hp
            new_boss[0] -= dmg
            my_armor += armor
            new_me[2] += mana
            turns -= 1
            if turns > 0:
                newer_effects.append(effect[:-1] + [turns])

        if new_boss[0] <= 0:
            min_mana = min(min_mana, mana_spent + cost)
            continue

        # resolve boss turn
        new_me[0] -= max(1, new_boss[1] - my_armor)
        if new_me[0] <= 0:
            continue

        queue.append((new_me, new_boss, newer_effects, mana_spent + cost))

print(min_mana)