N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

ALL = 1 << N

# DP[pattern][current]
dp = [[float('inf')] * N for _ in range(ALL)]
dp[0][0] = 0


def has_bit(n, i):
    return (n >> i & 1) > 0


for pattern in range(ALL):
    for current in range(N):
        for next in range(N):
            if current == next or has_bit(pattern, next):
                continue
            dp[pattern | 1 << next][next] = min(dp[pattern | 1 << next][next], \
                                                dp[pattern][current] + A[current][next])

print(dp[-1][0])
