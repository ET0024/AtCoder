n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

a2 = sorted(a)

for i in range(n):
    if a[i] == a2[-1]:
        print(a2[-2])
    else:
        print(a2[-1])
