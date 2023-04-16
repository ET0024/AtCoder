N, X = map(int, input().split())
S = input()

for s in S:
    if s == "x":
        if X > 0:
            X -= 1
    else:
        X += 1

print(X)
