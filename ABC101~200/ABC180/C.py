n = int(input())

ans = []
# 約数列挙
for i in range(1, n + 1):
    if i ** 2 > n:
        break
    if n % i == 0:
        j = n // i
        ans.append(i)
        if j > i:
            ans.append(j)

ans.sort()
for val in ans:
    print(val)
