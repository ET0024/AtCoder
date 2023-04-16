n = int(input())
x = []
for _ in range(n):
    _a, _b = map(int, input().split())
    x.append((_b, _a))

x.sort()
current = 0
for b, a in x:
    if b - current < a:
        print('No')
        exit()
    else:
        current += a

print('Yes')
