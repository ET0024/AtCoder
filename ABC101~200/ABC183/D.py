N, W = map(int, input().split())
T = [0] * int(2 * 1E5+1)

for _ in range(N):
    s, t, w = map(int, input().split())
    T[s] += w
    T[t] -= w

current = 0

for t in T:
    current += t
    if current > W:
        print("No")
        exit()

print("Yes")

# 以下、TLEのコード
# data = []
#
# for _ in range(N):
#     data.append(list(map(int, input().split())))
#
#
# data.sort(key=lambda x: x[0])
#
# t = 0
# wl = 0
# remained = []
#
# for i in range(N):
#     t = data[i][0]
#     wl += data[i][2]
#     remained.append(data[i])
#     remained_len = len(remained)
#     # print("debug: t, wl, remained=", t, wl, remained)
#
#     for i in range(remained_len):
#         target_index = remained_len - 1 - i
#         if remained[target_index][1] <= t:
#             wl -= remained[target_index][2]
#             remained.pop(target_index)
#
#     if wl > W:
#         print("No")
#         exit()
#
# print("Yes")
