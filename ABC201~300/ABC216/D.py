from collections import deque

n, m = map(int, input().split())
k = []
a = []
for _ in range(m):
    k.append(int(input()))
    a.append(list(map(int, input().split())))
a = list(reversed(a))
k = list(reversed(k))

q = deque()
# 一番上の色と筒の番号を管理する
counter = [0 for _ in range(n)]
d = {}
for tube in range(m):
    if len(a[tube]) > 0:
        tmp = a[tube].pop()
        if tmp not in d:
            d[tmp] = [tube]
        else:
            d[tmp].append(tube)
            for t in d[tmp]:
                q.append(t)

while len(q) > 0:
    tube1 = q.popleft()
    tube2 = q.popleft()

    for tube in [tube1, tube2]:
        if len(a[tube]) > 0:
            tmp = a[tube].pop()
            if tmp not in d:
                d[tmp] = [tube]
            else:
                d[tmp].append(tube)
                for t in d[tmp]:
                    q.append(t)

for tube in range(m):
    if len(a[tube]) > 0:
        print('No')
        exit()

print('Yes')
