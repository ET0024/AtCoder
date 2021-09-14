from collections import defaultdict

s = list(input())
dp = [defaultdict(int) for _ in range(len(s) + 1)]
MOD = 10 ** 9 + 7
for i, c in enumerate(s):
    i += 1

    for t in list('chokudai'):
        dp[i][t] += dp[i-1][t]

    if c == 'c':
        dp[i]['c'] = (dp[i - 1]['c'] + 1) % MOD
    elif c == 'h':
        dp[i]['h'] = (dp[i - 1]['c'] + dp[i - 1]['h']) % MOD
    elif c == 'o':
        dp[i]['o'] = (dp[i - 1]['h'] + dp[i - 1]['o']) % MOD
    elif c == 'k':
        dp[i]['k'] = (dp[i - 1]['o'] + dp[i - 1]['k']) % MOD
    elif c == 'u':
        dp[i]['u'] = (dp[i - 1]['k'] + dp[i - 1]['u']) % MOD
    elif c == 'd':
        dp[i]['d'] = (dp[i - 1]['u'] + dp[i - 1]['d']) % MOD
    elif c == 'a':
        dp[i]['a'] = (dp[i - 1]['d'] + dp[i - 1]['a']) % MOD
    elif c == 'i':
        dp[i]['i'] = (dp[i - 1]['a'] + dp[i - 1]['i']) % MOD

print(dp[-1]['i'])

# for i, r in enumerate(dp):
#     print(i, r)
