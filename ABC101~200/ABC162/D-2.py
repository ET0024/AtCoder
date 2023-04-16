from collections import defaultdict

n = int(input())
s = input()
rgb = ['R', 'G', 'B']
rgb_r = {'R': 0, 'G': 1, 'B': 2}
count = [defaultdict(int) for _ in range(n)]
count[n - 1][s[n - 1]] += 1

# 累積カウントを予め計算
for i in range(n - 2, -1, -1):
    for c in rgb:
        count[i][c] += count[i + 1][c]
        if c == s[i]:
            count[i][c] += 1

ans = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        if s[i] == s[j]:
            continue
        target = rgb[3 - rgb_r[s[i]] - rgb_r[s[j]]]
        ans += count[j + 1][target]

        # 等間隔のものを除外
        if j + (j - i) < n and s[j + (j - i)] == target:
            ans -= 1

print(ans)
