n, k = map(int, input().split())
score = []
s_sum = []
for _ in range(n):
    score.append(list(map(int, input().split())))
    s_sum.append(sum(score[-1]))

thr = sorted(s_sum)[-k]

for val in s_sum:
    # print(val)
    # print(thr)
    if val + 300 >= thr:
        print('Yes')
    else:
        print('No')
