n, t = map(int, input().split())
a = list(map(int, input().split()))

track = sum(a)
t = t % track

for i, val in enumerate(a):
    t -= val
    if t <= 0:
        print(i + 1, val + t)
        exit()
