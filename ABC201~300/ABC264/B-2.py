r, c = map(int, input().split())

dist = max(abs(r - 8), abs(c - 8))
if dist % 2 == 0:
    print('white')
else:
    print('black')
