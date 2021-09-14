N = int(input())

A = [list(map(int, input().split())) for _ in range(N)]

# dp[visited_pattern][last_city]
ALL = 1 << N
dp = [[float('inf')] * N for _ in range(ALL)]
dp[0][0] = 0

def has_bit(n, i):
    return (n >> i) & 1 > 0


for pattern in range(ALL):
    for current in range(N):
        for nxt in range(N):
            if nxt == current or has_bit(pattern, nxt):
                continue
            else:
                dp[pattern | 1 << nxt][nxt] = min(dp[pattern | 1 << nxt][nxt], \
                                                  dp[pattern][current] + A[current][nxt])

print(dp[-1][0])
