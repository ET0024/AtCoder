n, x = map(int, input().split())
pair = []
for _ in range(n):
    _a, _b = map(int, input().split())
    pair.append((_a, _b))

# dp[i=0..n][x=0..x+1]=True/False

dp = [set([0]) for _ in range(n + 1)]

for i in range(1, n + 1):
    a, b = pair[i - 1]
    new_set = set([0])
    for val in dp[i - 1]:
        for j in range(b + 1):
            new_set.add(min(val + j * a, x + 1))
    dp[i] = new_set

if x in dp[-1]:
    print('Yes')
else:
    print('No')
