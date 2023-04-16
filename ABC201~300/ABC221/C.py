s = input()
L = len(s)
ALL = 1 << L

ans = 0
for pattern in range(ALL):
    g1 = []
    g2 = []
    for i in range(L):
        if pattern >> i & 1:
            g1.append(s[i])
        else:
            g2.append(s[i])
    g1.sort(reverse=True)
    g2.sort(reverse=True)
    if len(g1) == 0 or len(g2) == 0:
        continue
    elif g1[0] == '0' or g2[0] == '0':
        continue
    else:
        num1 = int(''.join(g1))
        num2 = int(''.join(g2))
        ans = max(ans, num1 * num2)

print(ans)
