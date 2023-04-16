l = int(input())

# ans = (l-1)_C_11
ans = 1
for i in range(11): #sequentially calc (l-1)_C_i
    ans *= l - 1 - i
    ans //= i + 1

print(ans)
