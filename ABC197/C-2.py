n = int(input())
a = list(map(int, input().split()))

ALL = 1 << (n - 1)

# bit全探索
ans = float('inf')
for pattern in range(ALL):

    current = a[0]
    ors = []
    for i in range(n - 1):
        if pattern >> i & 1:
            ors.append(current)
            current = a[i + 1]
        else:
            current |= a[i + 1]
    ors.append(current)

    for i, val in enumerate(ors):
        if i == 0:
            x = val
        else:
            x ^= val

    if ans > x:
        ans = x

print(ans)
