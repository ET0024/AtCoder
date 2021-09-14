n, k = map(int, input().split())
R, S, P = map(int, input().split())
t = input()

score = 0
for mod in range(0, k):
    s = []
    tmp = mod
    while tmp < n:
        s.append(t[tmp])
        tmp += k
    # print(mod, s)

    dp = [{'r': 0, 'p': 0, 's': 0} for _ in range(len(s))]
    if s[0] == 'r':
        dp[0]['p'] += P
    elif s[0] == 'p':
        dp[0]['s'] += S
    elif s[0] == 's':
        dp[0]['r'] += R

    for i in range(1, len(s)):
        if s[i] == 'r':
            dp[i]['r'] = max(dp[i - 1]['p'], dp[i - 1]['s'])
            dp[i]['p'] = max(dp[i - 1]['r'] + P, dp[i - 1]['s'] + P)
            dp[i]['s'] = max(dp[i - 1]['r'], dp[i - 1]['p'])
        elif s[i] == 'p':
            dp[i]['r'] = max(dp[i - 1]['p'], dp[i - 1]['s'])
            dp[i]['p'] = max(dp[i - 1]['r'], dp[i - 1]['s'])
            dp[i]['s'] = max(dp[i - 1]['r'] + S, dp[i - 1]['p'] + S)
        elif s[i] == 's':
            dp[i]['r'] = max(dp[i - 1]['p'] + R, dp[i - 1]['s'] + R)
            dp[i]['p'] = max(dp[i - 1]['r'], dp[i - 1]['s'])
            dp[i]['s'] = max(dp[i - 1]['r'], dp[i - 1]['p'])

    score += max(dp[-1]['r'], dp[-1]['p'], dp[-1]['s'])

print(score)
