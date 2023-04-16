x, y, a, b = map(int, input().split())

set_xy = set()
set_ab = set()

for dx, dy in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1,), (-2, -1)]:
    set_xy.add((x + dx, y + dy))
    set_ab.add((a + dx, b + dy))

set_new = set_xy.intersection(set_ab)
if len(set_new) > 0:
    print('Yes')
else:
    print('No')
