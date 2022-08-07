n = int(input())
s = list(map(int, input().split()))

cand = set()
for a in range(1, 700):
    for b in range(1, 700):
        cand.add(4 * a * b + 3 * a + 3 * b)

count = 0
for pred in s:
    if pred not in cand:
        count += 1

print(count)
