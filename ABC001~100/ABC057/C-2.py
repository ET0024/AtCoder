n = int(input())

ans = 10 ** 9
for i in range(1, n + 1):
    if i ** 2 > n:
        break
    if n % i == 0:
        j = n // i
        val = len(str(max(i, j)))
        if val < ans:
            ans = val

print(ans)
