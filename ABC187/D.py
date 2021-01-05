N = int(input())
A, B = [], []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

initial_diff = sum(A)
x = sorted([A[i] * 2 + B[i] for i in range(N)], reverse=True)
count = 0
score = 0

for i in range(N):
    if score > initial_diff:
        break

    score += x[i]
    count += 1

print(count)
