from math import lcm

with open('inputs/day11.in', 'r') as infile:
    monkeys = {}
    paragraphs = infile.read().split('\n\n')
    all_divs = []
    for paragraph in paragraphs:
        l1, l2, l3, test, true, false = paragraph.splitlines()
        id = int(l1.split()[1][:-1])
        items = [int(i) for i in l2.split(':')[1].split(', ')]
        *_, op, val = l3.split()
        div = int(test.split()[-1])
        all_divs.append(div)
        true = int(true.split()[-1])
        false = int(false.split()[-1])
        monkeys[id] = [
            items, 0, ((op, val), div, true, false)]


def func(input, op, val):
    val = input if val == 'old' else int(val)
    if op == '+':
        return input + val
    elif op == '*':
        return input * val


# for round in range(20):
#     for i in sorted(monkeys.keys()):
#         items, _, props = monkeys[i]
#         pair, div, true, false = props
#         op, val = pair
#         length = len(items)
#         while items:
#             item = items.pop()
#             item = func(item, op, val)
#             item = int(item / 3)
#             if item % div == 0:
#                 monkeys[true][0].append(item)
#             else:
#                 monkeys[false][0].append(item)
#         monkeys[i][1] += length

# values = sorted(v[1] for v in monkeys.values())
# print(values[-1]*values[-2])

factor = lcm(*all_divs)
for round in range(10000):
    for i in sorted(monkeys.keys()):
        items, _, props = monkeys[i]
        pair, div, true, false = props
        op, val = pair
        length = len(items)
        while items:
            item = items.pop()
            item = func(item, op, val)
            if item % div == 0:
                monkeys[true][0].append(item % factor)
            else:
                monkeys[false][0].append(item % factor)
        monkeys[i][1] += length

values = sorted(v[1] for v in monkeys.values())
print(values[-1]*values[-2])
