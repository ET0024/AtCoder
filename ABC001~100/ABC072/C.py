n = int(input())
a = list(map(int, input().split()))

count = [0 for _ in range(10 ** 5 + 1)]
for val in a:
    count[val] += 1
    count[val + 1] += 1
    if val > 0:
        count[val - 1] += 1

print(max(count))
