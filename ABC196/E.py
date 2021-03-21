def bin_search(lst, target):
    l = 0
    r = len(lst)

    while r - l > 1:
        mid = (l + r) // 2
        if lst[mid] < target:
            l = mid
        else:
            r = mid
    return l


n = int(input())
a = []
t = []
for _ in range(n):
    _a, _t = map(int, input().split())
    a.append(_a)
    t.append(_t)

q = int(input())
x = list(map(int, input().split()))

x_id = list(range(0, q))
zipped = zip(x, x_id)
zipped = sorted(zipped)
x, x_id = map(list, zip(*zipped))

offset = 0
left = 0
right = 0

for i in range(n):

    if t[i] == 1:
        offset += a[i]
    elif t[i] == 2:
        l = bin_search(x, a[i] - offset)
        x = x[l:]
        x[l] = a[i] - offset
        left += l
    elif t[i] == 3:
        r = bin_search(x, a[i] - offset)
        x = x[:r + 1]
        x[r] = a[i] - offset
        right += len(x) - r

x_ans = [x[0]] * left + x + [x[-1]] * right
zipped = zip(x_id, x)
zipped = sorted(zipped)
x_id, x = map(list, zip(*zipped))

for _x in x:
    print(_x + offset)
