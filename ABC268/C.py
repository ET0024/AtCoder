n = int(input())
p = list(map(int, input().split()))

score = [0 for _ in range(n)]

for position, meal in enumerate(p):
    target = meal - position
    score[(target - 1) % n] += 1
    score[target % n] += 1
    score[(target + 1) % n] += 1

print(max(score))
