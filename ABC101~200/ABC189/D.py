n = int(input())
s = [input() for i in range(n)]

dp_true = [0] * (n + 1)
dp_false = [0] * (n + 1)

dp_true[0] = 1
dp_false[0] = 1

for i in range(1, n + 1):
    if s[i - 1] == "AND":
        dp_true[i] = dp_true[i - 1]
        dp_false[i] = dp_true[i - 1] + dp_false[i - 1] * 2
    elif s[i - 1] == "OR":
        dp_true[i] = dp_true[i - 1] * 2 + dp_false[i - 1]
        dp_false[i] = dp_false[i - 1]

print(dp_true[n])

