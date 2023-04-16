n = int(input())
s = []
t = []
for _ in range(n):
    _s, _t = input().split()
    s.append(_s)
    t.append(_t)

for i in range(n - 1):
    for j in range(i + 1, n):
        if s[i] == s[j] and t[i] == t[j]:
            print('Yes')
            exit()

print('No')
