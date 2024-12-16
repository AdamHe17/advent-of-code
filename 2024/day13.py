from collections import defaultdict
import re

ADD = 10000000000000

with open("day13.in", "r") as infile:
    paragraphs = infile.read().split("\n\n")

    res = 0
    for paragraph in paragraphs:
        print(paragraph)
        A, B, prize = paragraph.split("\n")
        ax, ay = map(int, re.findall("X\+(\d+), Y\+(\d+)", A)[0])
        bx, by = map(int, re.findall("X\+(\d+), Y\+(\d+)", B)[0])
        px, py = map(int, re.findall("X=(\d+), Y=(\d+)", prize)[0])
        px, py = px + ADD, py + ADD
        cost = float("inf")
        for a in range(px // ax + 1):
            if (
                (px - (ax * a)) % bx == 0
                and (py - (ay * a)) % by == 0
                and ((px - (ax * a)) // bx == (py - (ay * a)) // by)
            ):
                b = (py - (ay * a)) // by
                if 0 <= a <= 100 and 0 <= b <= 100:
                    cost = min(cost, 3 * a + b)
                    break
        if cost != float("inf"):
            res += cost

    print(res)
