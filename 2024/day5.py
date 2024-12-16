from collections import defaultdict

with open("day5.in", "r") as infile:
    _rules, _updates = infile.read().split("\n\n")

    rules = defaultdict(set)
    for rule in _rules.split("\n"):
        a, b = map(int, rule.split("|"))
        rules[b].add(a)

    p1 = 0
    p2 = 0
    for _update in _updates.split("\n"):
        update = [int(i) for i in _update.split(",")]
        middle = update[len(update) // 2]
        update_dict = {i: ind for ind, i in enumerate(update)}

        works = True
        for i, ind in update_dict.items():
            if rules[i]:
                if any(update_dict[j] > ind for j in rules[i] if j in update):
                    works = False
                    break
        if works:
            p1 += middle
            continue

        lst = []
        choices = set(update)
        new_choices = set(update)
        while choices:
            choices = new_choices
            for i in choices:
                if all(j not in choices for j in rules[i]):
                    lst.append(i)
                    new_choices = set([k for k in choices if k != i])
                    continue

        p2 += lst[len(lst) // 2]

    print(p1)
    print(p2)
