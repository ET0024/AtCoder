def calc(w, v, x):
    zipped = zip(v, w)
    zipped = sorted(zipped)
    v, w = map(list, zip(*zipped))
    x.sort()

    total = 0
    x_used_flag = [False] * len(x)
    while len(v):
        _v = v.pop()
        _w = w.pop()

        for i, _x in enumerate(x):
            if x_used_flag[i] is False and _x >= _w:
                total += _v
                x_used_flag[i] = True
                break

    return total


n, m, q = map(int, input().split())
w, v = [], []

for _ in range(n):
    _w, _v = map(int, input().split())
    w.append(_w)
    v.append(_v)
x = list(map(int, input().split()))

for _ in range(q):
    l, r = map(int, input().split())
    x_restricted = []
    for i, _x in enumerate(x):
        if i < l - 1 or r - 1 < i:
            x_restricted.append(_x)

    print(calc(w, v, x_restricted))
