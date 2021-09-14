n = int(input())

ans = 0
for i in range(n):
    if (i + 1) * (i + 2) / 2 >= n:
        ans = i + 1
        break

print(ans)
