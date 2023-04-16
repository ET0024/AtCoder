l, r = map(int, input().split())

ans = 2019
for i in range(l, min(r, l + 2019) + 1):
    for j in range(i + 1, min(r, i + 1 + 2019) + 1):
        if i * j % 2019 < ans:
            ans = i * j % 2019

print(ans)
