import hashlib

infile = open("day4.in", 'r')

key = infile.readline().strip()

i = 1
while True:
    combined_key = key + str(i)
    res = hashlib.md5(combined_key.encode()).hexdigest()
    if res.startswith('0' * 5):
        print(i)
        break
    i += 1

while True:
    combined_key = key + str(i)
    res = hashlib.md5(combined_key.encode()).hexdigest()
    if res.startswith('0' * 6):
        print(i)
        break
    i += 1
