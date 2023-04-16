from collections import defaultdict

n = int(input())
d = defaultdict(int)
for _ in range(n):
    d[input()] += 1

point = 0
winner = ''
for i, val in d.items():
    if val > point:
        point = val
        winner = i

print(winner)
