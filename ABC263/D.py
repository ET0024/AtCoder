n, l, r = map(int, input().split())
a = list(map(int, input().split()))

score_left = [0 for _ in range(n + 1)]
score_left_acc = [0 for _ in range(n + 1)]
score_right = [0 for _ in range(n + 1)]
score_right_acc = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    score_left[i] = score_left[i - 1] + l - a[i - 1]
    score_left_acc[i] = min(score_left_acc[i-1], score_left[i])
    score_right[i] = score_right[i - 1] + r - a[n - i]
    score_right_acc[i] = min(score_right_acc[i-1], score_right[i])

ans = 0
for i in range(n + 1):
   ans = min(ans, score_left_acc[i] + score_right_acc[n-i])

print(sum(a) + ans)

# print(score_left)
# print(score_left_acc)
# print(score_right)
# print(score_right_acc)