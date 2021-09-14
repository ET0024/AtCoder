from collections import defaultdict

s = input()

if len(s) <= 2:
    if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
        print('Yes')
    else:
        print('No')
    exit()

d = defaultdict(int)
for c in s:
    d[c] += 1

for i in range(0, 125):
    target = str(i * 8)
    while len(target) < 3:
        target = '0' + target

    if d[target[0]] >= target.count(target[0]) \
            and d[target[1]] >= target.count(target[1]) \
            and d[target[2]] >= target.count(target[2]):
        print('Yes')
        exit()

print('No')
