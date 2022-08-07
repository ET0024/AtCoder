from collections import defaultdict

vals = list(map(int, input().split()))
d= defaultdict(int)

for val in vals:
    d[val] += 1

if len(d) == 2:
    for k, v in d.items():
        if d[k] == 2:
            print('Yes')
            exit()

print('No')
