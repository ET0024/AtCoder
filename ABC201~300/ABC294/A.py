n = int(input())
a = list(map(int, input().split()))
a2 = []
for item in a:
    if item % 2 == 0:
        a2.append(item)

print(*a2)
