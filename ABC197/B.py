h, w, x, y = map(int, input().split())

x -= 1
y -= 1

s = []
for _ in range(h):
    s.append(input())

count = 1
for l in range(1, w+1):
    blocked = False
    if not blocked and y-l >= 0:
        nxt = s[x][y-l]
        if nxt == '#':
            blocked=True
            break
        else:
            count+=1

for r in range(1, w+1):
    blocked = False
    if not blocked and y+r < w:
        nxt = s[x][y+r]
        if nxt == '#':
            blocked=True
            break
        else:
            count+=1

for u in range(1, h+1):
    blocked = False
    if not blocked and x+u < h:
        nxt = s[x+u][y]
        if nxt == '#':
            blocked=True
            break
        else:
            count+=1

for d in range(1, h+1):
    blocked = False
    if not blocked and x-d >=0:
        nxt = s[x-d][y]
        if nxt == '#':
            blocked=True
            break
        else:
            count+=1

print(count)