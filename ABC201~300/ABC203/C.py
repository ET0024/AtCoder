n, k = map(int, input().split())
friend = []

for _ in range(n):
    a, b = map(int, input().split())
    friend.append((a, b))

friend.sort()
life = k
current = 0

for a, b in friend:
    if life < a - current:
        print(current + life)
        exit()
    else:
        life = life - (a - current) + b
        current = a

print(current + life)
