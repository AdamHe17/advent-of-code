with open("day2.in", "r") as infile:
    lines = infile.readlines()



res = 0
for line in lines:
    maxs = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    game, cubes = line.split(': ')
    game = int(game.split()[1])
    cubes = cubes.split('; ')
    for cube in cubes:
        colors = cube.split(', ')
        colors = [color.split() for color in colors]
        for color in colors:
            if maxs[color[1]] < int(color[0]):
                maxs[color[1]] = int(color[0])
    res += maxs['red'] * maxs['green'] * maxs['blue']

print(res)