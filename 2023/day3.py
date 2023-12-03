with open("day3.in", "r") as infile:
    lines = map(lambda x: x.strip(), infile.readlines())

# row = 0
# symbols = {}
# numbers = {}
# for line in lines:
#     curr = ""
#     start = -1
#     for i, v in enumerate(line):
#         if not v.isdigit() and v != ".":
#             symbols[(row, i)] = v

#         if v.isdigit():
#             curr += v
#             if start < 0:
#                 start = i
#         else:
#             if start > -1:
#                 numbers[(row, start)] = int(curr)
#                 curr = ""
#                 start = -1

#     if start > -1:
#         numbers[(row, start)] = int(curr)
#         curr = ""
#         start = -1

#     row += 1


def neighbors(coord):
    r, c = coord
    return (
        (r - 1, c - 1),
        (r - 1, c),
        (r - 1, c + 1),
        (r, c - 1),
        (r, c + 1),
        (r + 1, c - 1),
        (r + 1, c),
        (r + 1, c + 1),
    )


# res = 0
# for i, v in numbers.items():
#     r, c = i
#     l = len(str(v))
#     for j in range(l):
#         if any(n in symbols for n in neighbors((r, c + j))):
#             break
#     else:
#         continue

#     res += v

# print(res)

# Part 2

row = 0
gears = {}
numbers = {}
for line in lines:
    curr = ""
    start = -1
    for i, v in enumerate(line):
        if v == "*":
            gears[(row, i)] = v

        if v.isdigit():
            curr += v
            if start < 0:
                start = i
        else:
            if start > -1:
                numbers[(row, start)] = int(curr)
                curr = ""
                start = -1

    if start > -1:
        numbers[(row, start)] = int(curr)
        curr = ""
        start = -1

    row += 1

gear_parts = {}
for i, v in numbers.items():
    r, c = i
    l = len(str(v))
    for j in range(l):
        ns = neighbors((r, c + j))
        if any(n in gears for n in ns):
            for n in gears:
                if n in ns:
                    gear_parts.setdefault(n, [])
                    gear_parts[n].append(v)
            break
    else:
        continue

res = 0
for gear, nums in gear_parts.items():
    if len(nums) == 2:
        res += nums[0] * nums[1]

print(res)
