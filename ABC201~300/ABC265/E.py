from collections import defaultdict

n, m = map(int, input().split())
a, b, c, d, e, f = map(int, input().split())
obstacles = defaultdict(bool)
MOD = 998244353
for _ in range(m):
    x, y = map(int, input().split())
    obstacles[(x, y)] = True

dic = defaultdict(int)
dic[(0, 0)] = 1

for i in range(n):
    d_next = defaultdict(int)
    for (x, y), val in dic.items():
        for nx, ny in [(x + a, y + b), (x + c, y + d), (x + e, y + f)]:
            if not obstacles[(nx, ny)]:
                d_next[(nx, ny)] += val % MOD
                d_next[(nx, ny)] = d_next[(nx, ny)] % MOD
    dic = d_next
    # print('debug dic size:',len(dic))
    # print(dic)

ans = 0
for (x, y), c in dic.items():
    ans += c
    ans = ans % MOD
    # print(x, y, c)

print(ans)
