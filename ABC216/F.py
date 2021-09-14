from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
MOD = 998244353

z = []
for i in range(n):
    z.append((a[i], b[i]))

z.sort()

for i in range(n):
    a[i] = z[i][0]
    b[i] = z[i][1]

ans = 0
d = defaultdict(int)
d[0] = 1
for i in range(n):
    target = a[i]
    bb = b[:i]
    b_fix = b[i]
    # target=1522, bb=[3919, 3558, 1156, 3383]
    # bbの部分集合の選び方で和がtarget以下になるものの数
    # ただしb_fixは必ず選ぶ -> bbで和がtarget-bfix以下になるものの数
    # sparseなのでdefaultdictでdp
    # さらにloopごとにdpテーブルを育てていく <- NEW

    keys = list(d.keys())
    if len(bb) > 0:
        for key in keys:
            d[(key + bb[-1]) % MOD] += d[key]
            d[(key + bb[-1]) % MOD] %= MOD
    # for x in bb:
    #     keys = list(d.keys())
    #     for key in keys:
    #         d[key + x] += d[key]
    #         d[key + x] %= MOD

    # 集計
    for key, val in d.items():
        if key <= target - b_fix:
            ans += val
            ans %= MOD

print(ans)
