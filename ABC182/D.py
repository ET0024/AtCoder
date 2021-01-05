N = int(input())
A = list(map(int, input().split()))

maxs = []
fins = []

current_max = 0
current_fin = 0

for a in A:
    current_fin += a
    current_max = max(current_max, current_fin)
    maxs.append(current_max)
    fins.append(current_fin)

ans = 0
current = 0

for i in range(N):
    if current + maxs[i] > ans:
        ans = current + maxs[i]

    current += fins[i]

print(ans)