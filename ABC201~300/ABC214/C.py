n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

# s2[i] for s[i] + s[i+1] + ... + s[n-1]
s2 = [0 for _ in range(n)]
s2[n - 1] = s[n - 1]
for i in range(n - 2, -1, -1):
    s2[i] = s2[i + 1] + s[i]

ans = [float('inf') for _ in range(n)]
ans[0] = t[0]

for i in range(1, n):
    if t[i] + s2[i] < ans[0]:
        ans[0] = t[i] + s2[i]

print(ans[0])
for i in range(1, n):
    ans[i] = min(ans[i - 1] + s[i - 1], t[i])
    print(ans[i])
