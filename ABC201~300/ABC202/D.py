a, b, k = map(int, input().split())


def ncr(n, r):
    ans = 1
    for i in range(1, r + 1):
        ans *= (n + 1 - i)
    for i in range(1, r + 1):
        ans //= i
    return ans


n = a + b

ans = []
for i in range(n):
    th = ncr(a + b - 1, a - 1)
    if k > th and b > 0:
        ans.append('b')
        b -= 1
        k -= th
    elif a > 0:
        ans.append('a')
        a -= 1

if b > 0:
    ans.append(''.join(['b'] * b))
    b = 0
print(''.join(ans))
