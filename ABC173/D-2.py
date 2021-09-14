n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

ans = 0
for i in range(n - 1):
    ans += a[(i + 1) // 2]

print(ans)
# simulation
# current = [a[0]]
# for i, val in enumerate(a):
#     # currentに差し込んでスコアを更新する
#     if i == 0:
#         continue
#     score = 0
#     for j in range(len(current)):
#         if min(current[j-1], current[j]) > score:
#             score = min(current[j-1], current[j])
#             current.insert(j, val)
#             print(current, ', inserted val = ', val, ', score = ', score)
