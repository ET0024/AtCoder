n, m = map(int, input().split())
s = []
t = set()
total_len = 0

for _ in range(n):
    tmp = input()
    s.append(tmp)
    total_len += len(tmp)

margin = 16 - total_len - n + 1

for _ in range(m):
    t.add(input())

print(s)
print(t)
print(margin)