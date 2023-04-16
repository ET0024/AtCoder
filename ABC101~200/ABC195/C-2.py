n = int(input())

ans = 0
for digit in range(1, 10):
    if n >= 10 ** (digit * 3):
        ans += n - 10 ** (digit * 3) + 1

print(ans)
