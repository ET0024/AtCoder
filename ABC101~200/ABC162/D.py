from collections import defaultdict

n = int(input())
s = input()

rgb = {'R': 0, 'G': 1, 'B': 2}
rgb_r = {0: 'R', 1: 'G', 2: 'B'}

count = [defaultdict(int) for _ in range(n)]
count[n - 1][s[n - 1]] += 1

for i in range(n - 2, 0, -1):
    count[i]['R'] = count[i + 1]['R']
    count[i]['G'] = count[i + 1]['G']
    count[i]['B'] = count[i + 1]['B']
    count[i][s[i]] += 1

ans = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        if s[i] == s[j]:
            continue
        target = rgb_r[3 - rgb[s[i]] - rgb[s[j]]]
        ans += count[j + 1][target]

        if j + (j - i) < n and s[j + (j - i)] == target:
            ans -= 1

print(ans)
