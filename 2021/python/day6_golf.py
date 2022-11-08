f={i:open('inputs/day6.in').read().count(str(i))for i in range(9)}
for _ in'1'*256:f={i:f[(i+1)%9]+f[0]*(i==6)for i in f}
print(sum(f.values()))