n = int(input())
h = list(map(int, input().split()))
target = max(h)

for i, _h in enumerate(h):
    if _h == target:
        print(i + 1)
