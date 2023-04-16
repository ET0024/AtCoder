n, x = map(int, input().split())
a = list(map(int, input().split()))

aa = []
for el in a:
    if el != x:
        aa.append(el)

print(*aa)