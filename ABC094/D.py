import bisect

n = int(input())
a = list(map(int, input().split()))
a.sort()

half_i = bisect.bisect_left(a, a[-1] // 2)
ans = a[half_i]
for d in range(-1, 2):
    nxt = half_i + d
    if nxt < 0 or nxt >= n - 1:
        continue
    if abs(ans - a[-1] // 2) > abs(a[nxt] - a[-1] // 2):
        ans = a[nxt]

if a[-1] == ans:
    ans = a[-2]
print(a[-1], ans)
