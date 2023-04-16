n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

ans = 0
for i in range(n - 1):
    ans += a[(i+1) // 2]

print(ans)
# try simulation
# current = [a[0]]
# for i , val in enumerate(a):
#     if i == 0:
#         continue
#     m = 0
#     x = -1
#     for j in range(len(current)):
#         if min(current[j-1], current[j]) > m:
#             x = j
#             m = min(current[j-1], current[j])
#     current.insert(x, val)
#     print(current, ', added=', m)