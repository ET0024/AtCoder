import string
n = int(input())
l = 1
for i in range(n):
    if n - 26 ** (i + 1) > 0:
        l += 1
        n -= 26 ** (i + 1)
    else:
        break

n -= 1
ans = ''
for i in range(l):
    if n > 0:
        ans = string.ascii_letters[n % 26] + ans
        n //= 26
    else:
        ans = 'a' + ans

print(ans)
