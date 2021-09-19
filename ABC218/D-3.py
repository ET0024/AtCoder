from collections import defaultdict

n = int(input())
d = defaultdict(list)
for _ in range(n):
    x, y = map(int, input().split())
    d[x].append(y)

ans = 0
for x1 in d.keys():
    for x2 in d.keys():
        if x1 >= x2:
            continue

        cnt = 0
        for y1 in d[x1]:
            if y1 in d[x2]:
                cnt += 1
        ans += cnt * (cnt - 1) // 2

print(ans)
