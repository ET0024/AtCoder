n = int(input())
a = list(map(int, input().split()))

count = [0 for i in range(200)]

for i in a:
    count[i % 200] += 1

ans = 0

for c in count:
    if c >= 2:
        ans += c * (c - 1) // 2

print(ans)
