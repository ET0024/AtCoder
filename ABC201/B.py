n = int(input())

ts = []
for _ in range(n):
    _s, _t = input().split()
    ts.append((int(_t), _s))

ts.sort()
print(ts[-2][1])
