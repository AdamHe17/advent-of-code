from collections import defaultdict, deque
from itertools import combinations


with open("day24.in", "r") as infile:
    _registers, _instrs = infile.read().split("\n\n")

    def eval(r1, op, r2):
        v1, v2 = memory[r1], memory[r2]
        if op == "AND":
            return 1 if v1 and v2 else 0
        elif op == "OR":
            return 1 if v1 or v2 else 0
        elif op == "XOR":
            return v1 ^ v2

    memory = {}
    for r in _registers.split("\n"):
        name, val = r.strip().split(": ")
        memory[name] = 0
    memory["x25"] = 1
    memory["y25"] = 1

    instrs = []
    instrs_d = {}
    for instr in _instrs.split("\n"):
        r1, op, r2, _, r3 = instr.strip().split()
        if r2 < r1:
            r1, r2 = r2, r1
        instrs.append((r1, op, r2, r3))
        instrs_d[r3] = (r1, op, r2)

    def get_instrs(reg):
        if instrs_d[reg][0].startswith("x"):
            return instrs_d[reg]
        else:
            r1, op, r2 = instrs_d[reg]
            return (get_instrs(r1), op, get_instrs(r2))

    print(get_instrs("z00"))
    print(get_instrs("z01"))
    print(get_instrs("z02"))
    print(get_instrs("z03"))

    # while instrs:
    #     new_instrs = []
    #     for r1, op, r2, r3 in instrs:
    #         try:
    #             memory[r3] = eval(r1, op, r2)
    #         except:
    #             new_instrs.append((r1, op, r2, r3))
    #     instrs = new_instrs

    # res = ""
    # keys = [k for k in memory if k.startswith("z")]
    # for k in sorted(keys, reverse=True):
    #     res += str(memory[k])

    # print(res)
    # print(int(res, 2))
