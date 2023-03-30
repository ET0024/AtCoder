from collections import defaultdict

s = list(input())
ans = 'atcoder'
d = defaultdict(int)
for i, c in enumerate(list(ans)):
    d[c] = i

for i, c in enumerate(list(s)):
    s[i] = d[c]

# bubble sort
count = 0
for i in range(len(s)):
    for j in range(len(s) - 1):
        if s[j] > s[j + 1]:
            s[j], s[j + 1] = s[j + 1], s[j]
            count += 1

print(count)
