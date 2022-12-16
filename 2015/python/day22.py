from collections import deque

class Player:
    def __init__(self, hp, atk, mana):
        self.hp = hp
        self.atk = atk
        self.mana = mana
        self.armor = 0
        self.mana_spent = 0

    def copy(self):
        player = Player(self.hp, self.atk, self.mana)
        player.mana_spent = self.mana_spent
        return player

    def take_damage(self, damage: int):
        damage_taken = max(damage - self.armor, 1)
        self.hp -= damage_taken

    def dead(self):
        return self.hp <= 0

    def __str__(self):
        return f'hp={self.hp},atk={self.atk},mana={self.mana},armor={self.armor}'

me = Player(50, 0, 500)
# me = Player(10, 0, 250)
with open('inputs/day22.in', 'r') as infile:
    boss = Player(*([int(infile.readline().split(': ')[1]) for _ in range(2)] + [0]))
difficulty = 'hard'
# boss.hp = 14
# boss.atk = 8
print(me, boss, difficulty)

spells = [  # id, cost, hp, dmg, armor, mana, turns
    [0, 53, 0, 4, 0, 0, 1],
    [1, 73, 2, 2, 0, 0, 1],
    [2, 113, 0, 0, 7, 0, 6],
    [3, 173, 0, 3, 0, 0, 6],
    [4, 229, 0, 0, 0, 101, 5]
]

def cast_spell(me: Player, boss: Player, spell, effects) -> bool:
    spell_id, mana_cost, *effect = spell
    if me.mana < mana_cost:
        return False

    me.mana -= mana_cost
    me.mana_spent += mana_cost
    if spell_id == 0:
        boss.hp -= 4
    elif spell_id == 1:
        boss.hp -= 2
        me.hp += 2
    else:
        effects.append([spell_id, effect])

    return True


def resolve_effects(me: Player, boss: Player, effects) -> None:
    me.armor = 0
    new_effects = []
    for spell_id, effect in effects:
        hp, dmg, armor, mana, turns = effect
        me.hp += hp
        boss.hp -= dmg
        me.armor += armor
        me.mana += mana
        turns -= 1
        if turns:
            new_effects.append([spell_id, [hp, dmg, armor, mana, turns]])
    return new_effects

min_mana = float('inf')
queue = deque([(me, boss, [], True)])
# iteration = 0
visited = set()
while queue:
    me, boss, active_effects, my_turn = queue.popleft()
    # iteration += 1
    # if iteration % 100_000 == 0:
        # print(f'i={iteration}, min_mana={min_mana}, hps={me.hp, boss.hp}')

    state = (me.hp, boss.hp, frozenset([(spell_id, effect[-1]) for spell_id, effect in active_effects]))
    if state in visited:
        continue
    visited.add(state)

    if me.mana_spent > min_mana:
        continue

    if difficulty == 'hard' and my_turn:
        me.hp -= 1
        if me.dead():
            continue

    # resolve effects
    new_effects = resolve_effects(me, boss, active_effects)
    if boss.dead():
        min_mana = min(min_mana, me.mana_spent)
        continue

    if my_turn:
        active_spells = set(spell_id for spell_id,_ in new_effects)
        possible_spells = [spell for spell in spells if spell[0] not in active_spells]
        for spell in possible_spells:
            new_me = me.copy()
            new_boss = boss.copy()
            effects_copy = new_effects[:]
            if not cast_spell(new_me, new_boss, spell, effects_copy):
                continue
            if new_boss.dead():
                min_mana = min(min_mana, new_me.mana_spent)
                continue

            queue.append((new_me, new_boss, effects_copy, not my_turn))
    else:
        me.take_damage(boss.atk)
        if me.dead():
            continue

        queue.append((me, boss, new_effects, not my_turn))


print(min_mana)