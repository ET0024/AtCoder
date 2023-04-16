n = int(input())

diff = []
score = 0

for _ in range(n):
    a, b = map(int, input().split())
    score -= a
    diff.append(2 * a + b)

diff.sort(reverse=True)

ans = 0
for d in diff:
    score += d
    ans += 1
    if score > 0:
        break

print(ans)
