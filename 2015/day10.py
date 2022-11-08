infile = open('day10.in', 'r')

N = infile.readline().strip()


def gen(n):
    res = ''
    i = 0
    j = 1
    curr = n[0]
    while j < len(n):
        if n[j] != curr:
            res += str(j - i)
            res += n[i]
            curr = n[j]
            i = j
        j += 1

    res += str(j - i)
    res += n[i]
    return res


for _ in range(40):
    N = gen(N)
print(len(N))

for _ in range(10):
    N = gen(N)
print(len(N))