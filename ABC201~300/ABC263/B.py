n = int(input())
ps = list(map(int, input().split()))

generation = [0 for _ in range(n)]

for i, p in enumerate(ps):
    i += 1
    generation[i] = generation[p - 1] + 1

print(generation[-1])