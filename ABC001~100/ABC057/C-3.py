n = int(input())
ans = 10 ** 10
for i in range(1, n + 1):
    if i ** 2 > n:
        break
    if n % i == 0:
        j = n // i
        if len(str(j)) < ans:
            ans = len(str(j))

print(ans)
