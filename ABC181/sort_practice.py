import bisect

a = [1, 12, 23, 38, 54, 66, 76, 98]
a.sort(reverse=True)
print(a)

# a.insert(bisect.bisect_left(a, 25), 25)
bisect.insort(a, 25)
print(a)

ans = 1e10
print(ans)