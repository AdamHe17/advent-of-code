def get_lines(filename):
    with open(filename, 'r') as infile:
        lines = infile.readlines()
    
    return lines

def get_paragraphs(filename):
    with open(filename, 'r') as infile:
        paragraphs = infile.read().split('\n\n')
    
    return paragraphs

times, distances = get_lines('day6.in')
times = [int(i) for i in times.split(':')[1].split()]
distances = [int(i) for i in distances.split(':')[1].split()]

res = 1
for time, distance in zip(times, distances):
    ways = 0
    for i in range(1, time):
        curr = i * (time - i)
        if curr > distance:
            ways += 1
    res *= ways

print(res)