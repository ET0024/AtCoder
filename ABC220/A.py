a, b, c = map(int, input().split())

target = c * (a // c)

if a <= target <= b:
    print(target)
    exit()
elif a <= target + c <= b:
    print(target + c)
else:
    print(-1)
