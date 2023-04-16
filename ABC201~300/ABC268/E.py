
# 人
# 0 1 2 3
#
# 料理
# 1 2 0 3 -> [1, 1, 2, 0] -> 4
# 3 1 2 0 -> [1, 0, 0, 1] -> 2
# 0 3 1 2 -> [0, 2, 1, 1] -> 4
# 2 0 3 1 -> [2, 1, 1, 2] -> 6
# 単調増加・減少のサイクルがある？二分探索か？



n = int(input())
p = list(map(int, input().split()))

score = [0 for _ in range(n)]

for position, meal in enumerate(p):
    target = meal - position
    score[(target - 1) % n] += 1
    score[target % n] += 1
    score[(target + 1) % n] += 1

print(max(score))
