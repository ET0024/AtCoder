n = int(input())
a = list(map(int, input().split()))

b = [(val, i + 1) for i, val in enumerate(a)]
print(*list(map(lambda x: x[1], sorted(b))))
