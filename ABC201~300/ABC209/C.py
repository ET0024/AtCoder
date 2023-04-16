n = int(input())
c = list(map(int, input().split()))
c.sort()
ans = 1
L = (10 ** 9 + 7)
for i, v in enumerate(c):
    ans *= (v  - i) % L
    ans = ans % L

print(ans % L)
