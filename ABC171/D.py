n = int(input())
a = list(map(int, input().split()))
q = int(input())

total = sum(a)
count = [0 for _ in range(10 ** 5 + 1)]
for val in a:
    count[val] += 1

for _ in range(q):
    b, c = map(int, input().split())
    total += (c - b) * count[b]
    count[c] += count[b]
    count[b] = 0
    print(total)
