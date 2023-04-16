s = list(input())
b = []
r = []

for i, c in enumerate(s):
    if c == 'B':
        b.append(i)
    elif c == 'R':
        r.append(i)
    elif c == 'K':
        k = i

if b[0] % 2 != b[1] % 2 and r[0] < k < r[1]:
    print('Yes')
else:
    print('No')
