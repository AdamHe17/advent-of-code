with open('inputs/day14.in', 'r') as infile:
    reindeers = {}
    for line in infile.readlines():
        words = line.split()
        name = words[0]
        speed = int(words[3])
        duration = int(words[6])
        rest = int(words[-2])
        reindeers[name] = (speed, duration, rest)

time = 2503
traveled = {name: 0 for name in reindeers.keys()}
points = {name: 0 for name in reindeers.keys()}
for t in range(time):
    for name, (speed, duration, rest) in reindeers.items():
        if t % (duration + rest) < duration:
            traveled[name] += speed

    leader = max(traveled.values())
    for name, dist in traveled.items():
        if dist == leader:
            points[name] += 1

print(sorted(points.values(), key=lambda x: -x))
