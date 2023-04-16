n, x = map(int, input().split())
a = set(map(int, input().split()))
a2 = set([val + x for val in a])

if len(a.intersection(a2))>0:
    print('Yes')
else:
    print('No')
