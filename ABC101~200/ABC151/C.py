n, m = map(int, input().split())

penalty = [0 for _ in range(n)]
completed = [False for _ in range(n)]

for _ in range(m):
    p, s = input().split()
    p = int(p) - 1
    if s == 'AC':
        completed[p] = True
    elif s == 'WA' and not completed[p]:
        penalty[p] += 1

ans_penalty = 0
ans_completed = 0
for i, b in enumerate(completed):
    if b:
        ans_completed += 1
        ans_penalty += penalty[i]

print(ans_completed, ans_penalty)
