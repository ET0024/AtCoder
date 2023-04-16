s = list(input())

b = []
k = []
r = []
for i, c in enumerate(s):
    if c == 'B':
        b.append(i)
    elif c == 'K':
        k.append(i)
    elif c == 'R':
        r.append(i)

if (b[1] - b[0]) % 2 != 0 and r[0] < k[0] < r[1]:
    print('Yes')
else:
    print('No')
