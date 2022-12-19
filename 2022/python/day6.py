with open('inputs/day6.in', 'r') as infile:
    line = infile.readline().strip()

for i in range(len(line)):
    if len(line[i:i+4]) == len(set(line[i:i+4])):
        print(i+4)
        break

for i in range(len(line)):
    if len(line[i:i+14]) == len(set(line[i:i+14])):
        print(i+14)
        break
