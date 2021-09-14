n = int(input())
h = list(map(int, input().split()))

nxt = h[n - 1]

for i in range(n - 2, -1, -1):
    if h[i] > nxt:
        h[i] -= 1

    if h[i] > nxt:
        print('No')
        exit()
    nxt = h[i]

print('Yes')
