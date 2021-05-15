n = int(input())
s = list(input())
q = int(input())

parity = 0

for i in range(q):
    t, a, b = map(int, input().split())

    if t == 1:
        if parity == 1:
            a, b = (a + n) % (2 * n), (b + n) % (2 * n)
        s[a - 1], s[b - 1] = s[b - 1], s[a - 1]

    elif t == 2:
        parity = int(abs(1 - parity))

if parity == 0:
    print(''.join(s))
else:
    print(''.join(s[n:2*n]+s[:n]))
