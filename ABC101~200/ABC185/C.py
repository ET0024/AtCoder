L = int(input())

# ans = (L-1)_C_11

ans = 1
for i in range(1, 12):
    ans *= (L-i)
    ans //= i

print(ans)
