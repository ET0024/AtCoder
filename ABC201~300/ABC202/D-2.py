a, b, k = map(int, input().split())
L = a + b
ans = []
for i in range(L):
    if a == 0:
        ans.append('b')
        b -= 1
    elif b == 0:
        ans.append('a')
        a -= 1
    else:
        c = 1
        for r in range(1, b + 1):
            c *= a + b - r
            c //= r
        if k > c:
            ans.append('b')
            b -= 1
            k -= c
        else:
            ans.append('a')
            a -= 1

print(''.join(ans))
