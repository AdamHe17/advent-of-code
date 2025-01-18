with open("day17.in", "r") as infile:
    _regs, _program = infile.read().split("\n\n")

    parsed_regs = {}
    for line in _regs.split("\n"):
        _name, val = line.split(": ")
        parsed_regs[_name.split()[1].strip()] = int(val)

    program = [int(i) for i in _program.split(":")[1].split(",")]
    pointer = 0

    "2,4,1,2,7,5,4,5,1,3,5,5,0,3,3,0"
    for A in range(
        8**15 + 3 * 8**13 + 5 * 8**12 + 5 * 8**11 + 1 * 8**10 + 4 * 8**7 + 5 * 8**6,
        8**16,
    ):
        regs = parsed_regs.copy()
        regs["A"] = A
        pointer = 0

        def combo(op):
            if 0 <= op <= 3:
                return op
            elif 4 <= op <= 6:
                return regs["ABC"[op - 4]]
            else:
                return None

        outputs = []

        def instrs(pointer):
            instr, op = program[pointer], program[pointer + 1]
            if instr == 0:
                regs["A"] //= 2 ** combo(op)
            elif instr == 1:
                regs["B"] ^= op
            elif instr == 2:
                regs["B"] = combo(op) % 8
            elif instr == 3:
                if regs["A"] != 0:
                    pointer = op
                    pointer -= 2
            elif instr == 4:
                regs["B"] ^= regs["C"]
            elif instr == 5:
                outputs.append(combo(op) % 8)
            elif instr == 6:
                regs["B"] = regs["A"] // 2 ** combo(op)
            elif instr == 7:
                regs["C"] = regs["A"] // 2 ** combo(op)
            else:
                1 / 0

            return pointer + 2

        while pointer < len(program):
            pointer = instrs(pointer)

        if outputs:
            print(f"{A}: {','.join(map(str,outputs))}")
            if ",".join(map(str, outputs)) == "2,4,1,2,7,5,4,5,1,3,5,5,0,3,3,0":
                break
            # print(A, int("".join(map(str, outputs)), 8))
