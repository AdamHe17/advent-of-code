with open('inputs/day10.in', 'r') as infile:
    instructions = infile.read().splitlines()

# pointer = 0
# val = 1
# cycles = 0
# signal_strengths = 0

# def tick():
#     global cycles, val, signal_strengths
#     cycles += 1
#     if cycles % 40 == 20:
#         signal_strengths += val * cycles


# for i, instr in enumerate(instructions):
#     if instr == 'noop':
#         tick()
#     else:
#         tick()
#         tick()
#         _, add = instr.split()
#         val += int(add)

# print(signal_strengths)

pointer = 0
val = 1
cycles = 0
signal_strengths = 0
pixels = []


def tick():
    global cycles, val, signal_strengths
    cycles += 1
    l = len(pixels)
    if val - 1 <= l % 40 <= val + 1:
        pixels.append('#')
    else:
        pixels.append('.')


for i, instr in enumerate(instructions):
    if instr == 'noop':
        tick()
    else:
        tick()
        tick()
        _, add = instr.split()
        val += int(add)

for i in range(6):
    print(''.join(pixels[i*40:(i+1)*40]))
