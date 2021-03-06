def g1(x):
    return int("".join(sorted(str(x), reverse=True)))


def g2(x):
    return int("".join(sorted(str(x))))


def f(x):
    return g1(x) - g2(x)


n, k = map(int, input().split())
current = n

for _ in range(k):
    current = f(current)

print(current)
