infile = open("day2.in", 'r')

dimens = infile.readlines()

total_paper = 0
total_ribbon = 0

for dimen in dimens:
    l, w, h = map(int, dimen.split('x'))
    total_paper += 2 * (l * w + w * h + h * l) + min(l * w, w * h, h * l)
    total_ribbon += 2 * (l + w + h - max(l, w, h)) + l * w * h

print(total_paper)
print(total_ribbon)
