n, p = map(int, input().split())
a = list(map(int, input().split()))

count = 0
for val in a:
    if val < p:
        count += 1

print(count)
