n, m = map(int, input().split())
s = []
t = []
for _ in range(n):
    s.append(input())

for _ in range(m):
    t.append(input())

count = 0
for _s in s:
    for _t in t:
        if _s[3:] == _t:
            count += 1
            break

print(count)