import re

with open("day3.in", "r") as infile:
    lines = infile.readlines()

    res = 0
    save = True
    for line in lines:
        ind = 0
        for i in re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", line):
            a, b = map(int, i[4:-1].split(","))
            res += a * b

    print(res)


with open("day3.in", "r") as infile:
    lines = infile.readlines()
    res = 0
    save = True
    for line in lines:
        lst = []
        for i in re.finditer("do\(\)", line):
            lst.append((i.start(), True))
        for i in re.finditer("don't\(\)", line):
            lst.append((i.start(), False))

        lst.sort(key=lambda x: x[0])
        ind = 0
        for i in re.finditer("mul\([0-9]{1,3},[0-9]{1,3}\)", line):
            start = i.start()
            while ind < len(lst) and start > lst[ind][0]:
                save = lst[ind][1]
                ind += 1

            if save:
                a, b = map(int, i[0][4:-1].split(","))
                res += a * b

    print(res)
