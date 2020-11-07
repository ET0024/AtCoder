import bisect

N, M = map(int, input().split())
H = list(map(int, input().split()))
W = list(map(int, input().split()))

H.sort()

if N == 1:
    cost = 1e20
    for w in W:
        if abs(w-H[0]) < cost:
            cost = abs(w-H[0])
    print(cost)
    exit()

H_diff = [H[i + 1] - H[i] for i in range(0, N - 1)]
H_diff_a = [0] * (N - 1)
H_diff_a[0] = H_diff[0]
H_diff_a[-1] = H_diff[-1]

if N >= 3:
    for i in range(2, N - 1, 2):
        H_diff_a[i] = H_diff_a[i - 2] + H_diff[i]
if N >= 4:
    for i in range(-1, -N, -2):
        H_diff_a[i] = H_diff_a[i + 2] + H_diff[i]

H_diff_a.append(0)
H_diff_a.append(0)

ans = 1E20

for w in W:
    index = bisect.bisect_left(H, w)

    cost = ans
    if index % 2 == 1:
        cost = H_diff_a[index - 3] + abs(w - H[index - 1]) + H_diff_a[index]
    else:
        cost = H_diff_a[index - 2] + abs(H[index] - w) + H_diff_a[index + 1]

    if cost < ans:
        ans = cost

print(ans)
