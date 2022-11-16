infile = open('day5.in', 'r')

banned = ['ab', 'cd', 'pq', 'xy']
vowels = ['a', 'e', 'i', 'o', 'u']


def nice_str(s):
    for ban in banned:
        if ban in s:
            return False

    if sum([s.count(v) for v in vowels]) < 3:
        return False

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True

    return False


def nice_str_2(s):
    p1 = False
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            p1 = True
            break

    p2 = False
    for i in range(len(s) - 3):
        if s[i:i + 2] in s[i + 2:]:
            p2 = True
            break

    return p1 and p2


res1 = 0
res2 = 0
for line in infile.readlines():
    if nice_str(line):
        res1 += 1
    if nice_str_2(line):
        res2 += 1

print(res1)
print(res2)