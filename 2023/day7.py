with open("day6.in", "r") as infile:
    lines = infile.readlines()

ls = []
for line in lines:
    cards, point = line.split()
    ls.append((cards, int(point)))

cards = "AKQT98765432J"


def score(hand):
    us = set(hand)
    if "J" in us:
        l = list(us)
        l.sort(key=lambda x: [-hand.count(x), cards.index(x)])
        rep = ""
        print(l)
        if l[0] == "J":
            if len(l) == 1:
                return 1
            rep = l[1]
        else:
            rep = l[0]
        hand = hand.replace("J", rep)
    us = set(hand)
    if len(us) == 2:
        a, b = us
        if hand.count(a) == 4 or hand.count(b) == 4:
            return 1.5
    elif len(us) == 3:
        a, b, c = us
        if hand.count(a) == 3 or hand.count(b) == 3 or hand.count(c) == 3:
            return 2.5
    return len(us)


ls.sort(
    key=lambda x: (
        -score(x[0]),
        -cards.index(x[0][0]),
        -cards.index(x[0][1]),
        -cards.index(x[0][2]),
        -cards.index(x[0][3]),
        -cards.index(x[0][4]),
    )
)

print(ls)

res = 0
for i, v in enumerate(ls):
    res += (i + 1) * v[1]

print(res)
