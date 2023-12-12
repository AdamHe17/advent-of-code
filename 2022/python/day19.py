from collections import defaultdict, deque, namedtuple
from math import ceil

with open('inputs/day19.in', 'r') as infile:
    paragraphs = infile.read().split('\n')
    blueprints = []
    for paragraph in paragraphs:
        paragraph = paragraph.replace(':', '.')
        _, ore, clay, obsidian, geode = map(
            lambda x: x.strip(), paragraph.split('. '))
        ore = (int(ore.split()[-2]), 0, 0, 0)
        clay = (int(clay.split()[-2]), 0, 0, 0)
        obsidian = (int(obsidian.split()[-5]), int(obsidian.split()[-2]), 0, 0)
        geode = (int(geode.split()[-5]), 0,  int(geode.split()[-2]), 0)
        blueprints.append((ore, clay, obsidian, geode))

print(blueprints)

State = namedtuple(
    "State", "ore_miners clay_miners obs_miners geode_miners ores clay obs geode time")


minutes = 24
total_quality = 0
for index, blueprint in enumerate(blueprints):
    print(blueprint)
    max_costs = list(max(cost[i] for cost in blueprint)
                     for i in range(3)) + [float('inf')]
    initial_state = State(1, 0, 0, 0, 0, 0, 0, 0, 0)
    queue = deque([initial_state])
    max_geodes = 0
    iters = 0
    max_seen = defaultdict(lambda: 0)
    while queue:
        iters += 1
        if iters % 1000000 == 0:
            print(iters, state)

        state = queue.popleft()
        # if state.geode < max_seen[state.time]:
        #     continue
        # max_seen[state.time] = max(max_seen[state.time], state.geode)

        if state.time == minutes:
            max_geodes = max(max_geodes, state.geode)
            continue

        for metal in range(4):
            if state[metal] >= max_costs[metal]:
                continue

            cost = blueprint[metal]
            if all(state[i] for i in range(4) if cost[i]):
                time = max(max(0, ceil((cost[i]-state[i+4])/state[i]))
                           for i in range(4) if cost[i])
                if state.time + time > minutes:
                    continue

                queue.append(State(state.ore_miners + (metal == 0), state.clay_miners + (metal == 1), state.obs_miners + (metal == 2), state.geode_miners + (metal == 3), state.ores +
                             state.ore_miners*time - cost[0], state.clay+state.clay_miners*time - cost[1], state.obs+state.obs_miners*time - cost[2], state.geode+state.geode_miners*time - cost[3], state.time + time))

    print(max_seen)
    print(max_geodes)
    total_quality += (index + 1) * max_geodes

print(total_quality)

# def could_purchase(state, blueprint, max_costs, time_left):
#     # prioritize building geode miners
#     if all(state[i + 4] >= blueprint[3][i] for i in range(4)):
#         return set([3])

#     res = set()
#     for metal in range(3):
# if state[metal] >= max_costs[metal]:
#     continue

# if state[metal] * time_left + state[metal + 4] >= max_costs[metal] * time_left:
#     continue

#         costs = blueprint[metal]
#         if all(state[i + 4] >= costs[i] for i in range(4)):
#             res.add(metal)

#     return res

# minutes = 32
# total_quality = 0
# for index, blueprint in enumerate(blueprints[:3]):
#     print(blueprint)
#     max_costs = list(max(cost[i] for cost in blueprint)
#                      for i in range(3)) + [float('inf')]
#     initial_state = State(1, 0, 0, 0, 0, 0, 0, 0)
#     states = set([initial_state])
#     for minute in range(minutes):
#         new_states = set()

#         for state in states:
#             no_buy_state = State(state.ore_miners, state.clay_miners, state.obs_miners, state.geode_miners, state.ores +
#                                  state.ore_miners, state.clay + state.clay_miners, state.obs + state.obs_miners, state.geode + state.geode_miners)
#             new_states.add(no_buy_state)

#             for miner_id in could_purchase(state, blueprint, max_costs, minutes - minute):
#                 cost = blueprint[miner_id]
#                 buy_state = State(state.ore_miners + (miner_id == 0), state.clay_miners + (
#                     miner_id == 1), state.obs_miners + (miner_id == 2), state.geode_miners + (miner_id == 3), no_buy_state.ores - cost[0], no_buy_state.clay - cost[1], no_buy_state.obs - cost[2], no_buy_state.geode - cost[3])

#                 new_states.add(buy_state)

#         max_geode = max(state.geode for state in new_states)
#         states = new_states
#         print(minute + 1, len(states), max_geode)

#     print(max_geode)
#     total_quality += (index + 1) * max_geode

# print(total_quality)
