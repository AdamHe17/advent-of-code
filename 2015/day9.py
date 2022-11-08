from collections import defaultdict

infile = open('day9.in', 'r')

lines = infile.readlines()

i = 1
while i * (i - 1) // 2 < len(lines):
    i += 1

cities = i
print(f'cities = {cities}')

city_map = defaultdict(lambda: [])
for line in lines:
    source, _, dest, _, dist = line.split()
    city_map[source].append((dest, dist))
    city_map[dest].append((source, dist))

cities = list(city_map.keys())

starting_city = cities[0]
print(f'starting city={starting_city}')
