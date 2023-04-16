from collections import defaultdict

N, C = map(int, input().split())
d_cost = defaultdict(int)

for _ in range(N):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    d_cost[a] += c
    d_cost[b + 1] -= c

d_cost2 = sorted(list(d_cost.items()))

current = d_cost2[0][0]
cost = d_cost2[0][1]

ans = 0
for i in range(1, len(d_cost2)):
    to = d_cost2[i][0]
    ans += min(cost, C) * (to - current)
    current = to
    cost += d_cost2[i][1]

print(ans)
