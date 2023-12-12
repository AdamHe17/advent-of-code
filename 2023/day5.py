def get_lines(filename):
    with open(filename, 'r') as infile:
        lines = infile.readlines()
    
    return lines

def get_paragraphs(filename):
    with open(filename, 'r') as infile:
        paragraphs = infile.read().split('\n\n')
    
    return paragraphs

paragraphs = get_paragraphs('day5.in')
seeds, *maps = paragraphs
seeds = [int(i) for i in seeds.split(':')[1].split()]
all_seeds = []
for i in range(len(seeds) // 2):
    all_seeds.append((seeds[2*i], seeds[2*i+1]))

all_maps = []
for m in maps:
    new = []
    _, *m = m.split('\n')
    min_src = float('inf')
    max_src = float('-inf')
    for line in m:
        dest, src, l = map(int, line.split())
        new.append((dest, src, l))
        min_src = min(min_src, src)
        max_src = max(max_src, src + l)
    new.sort(key=lambda x: x[1])
    all_maps.append((new, min_src, max_src))

from bisect import bisect_right

min_loc = float('inf')
for (start, _len) in all_seeds:
    print(start, _len)
    for i in range(_len):
        i = start + i
        for (m, min_src, max_src) in all_maps:
            if min_src <= i < max_src:
                ind = bisect_right([j[1] for j in m], i)
                (dest, src, l) = m[ind - 1]
                i = dest + (i - src)

        min_loc = min(min_loc, i)

print(min_loc)