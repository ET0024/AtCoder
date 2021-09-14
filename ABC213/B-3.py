n = int(input())
a = list(map(int, input().split()))
a2 = [(val, i + 1) for i, val in enumerate(a)]
a2.sort()
print(a2[-2][1])
