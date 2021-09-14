t = int(input())

for _ in range(t):
    n = int(input())
    intervals = []
    for _ in range(n):
        l, r = map(int, input().split())
        intervals.append((r, l))

    # sort by r
    intervals.sort()
    intervals = list(map(lambda x: (x[1], x[0]), intervals))

    # sort by l
    intervals.sort()
    print('sorted=', intervals)
    current = -1
    possible = True
    for l, r in intervals:
        current = max(current + 1, l)
        print(current, '-pushed')
        if current > r:
            possible = False
            print('False here!')

    if possible:
        print('Yes')
    else:
        print('No')
