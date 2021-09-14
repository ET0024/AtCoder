MOD = 998244353
n = int(input())
s = input()

ALL = 1 << 10
dp = [[[0] * 11 for _ in range(ALL)] for _ in range(n)]

s = s.replace('A', '0')
s = s.replace('B', '1')
s = s.replace('C', '2')
s = s.replace('D', '3')
s = s.replace('E', '4')
s = s.replace('F', '5')
s = s.replace('G', '6')
s = s.replace('H', '7')
s = s.replace('I', '8')
s = s.replace('J', '9')
s = list(map(lambda x: int(x), list(s)))

dp[0][1 << s[0]][s[0]] = 1
dp[0][0][10] = 1  # 10 accounts for no digit

for i in range(1, n):
    for pat in range(ALL):
        for last_digit in range(11):
            # s[i]が新しいpatternの場合
            if pat & 1 << s[i] == 0:
                # 加える
                dp[i][pat | 1 << s[i]][s[i]] += dp[i - 1][pat][last_digit]
                dp[i][pat | 1 << s[i]][s[i]] %= MOD

                # 加えない
                dp[i][pat][last_digit] += dp[i - 1][pat][last_digit]
                dp[i][pat][last_digit] %= MOD
            else:
                # 加える
                if last_digit == s[i]:
                    dp[i][pat][s[i]] += dp[i - 1][pat][last_digit]
                    dp[i][pat][s[i]] %= MOD
                # 加えない
                dp[i][pat][last_digit] += dp[i - 1][pat][last_digit]
                dp[i][pat][last_digit] %= MOD

count = 0
for r in dp[-1]:
    count += sum(r)

print((count - 1) % MOD)
