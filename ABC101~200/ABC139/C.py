n = int(input())
h = list(map(int, input().split()))

current = h[0]
count = 0
ans = 0
for i in range(1, n):
    if h[i] <= current:
        current = h[i]
        count += 1
        if count > ans:
            ans = count
    else:
        if count > ans:
            ans = count
        current = h[i]
        count = 0

print(ans)
