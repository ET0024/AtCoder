from collections import deque

MOD = 998244353
Q = int(input())
q = deque()
q.append(1)
res = 1

mod_calc = [1]
for _ in range(10 ** 6):
    mod_calc.append((mod_calc[-1] * 10) % MOD)

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        q.append(x)
        res = (res * 10 + x) % MOD

    elif query[0] == 2:
        m = len(q) - 1
        x = q.popleft()

        res = (res - x * mod_calc[m]) % MOD
    else:
        print(res % MOD)
