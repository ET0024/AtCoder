n, k = map(int, input().split())

s = []

for i in range(k):
    l, r = map(int, input().split())
    for j in range(l, r+1):
        s.append(j)

s.sort()
lst = [0]*n
lst[0] = 1

for i in range(n):
    for d in s:
        if i + d < len(lst):
            lst[i+d] += lst[i]
            # print("debug: from", i+1, "to", i+1+d)

print(lst[-1]%998244353)