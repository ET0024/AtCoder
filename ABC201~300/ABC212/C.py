n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

a_idx = 0
b_idx = 0

ans = float('inf')
while a_idx < len(a) and b_idx < len(b):
    tmp = abs(a[a_idx] - b[b_idx])
    if tmp < ans:
        ans = tmp

    if a[a_idx] > b[b_idx]:
        b_idx += 1
    elif a[a_idx] < b[b_idx]:
        a_idx += 1
    else:
        break

print(ans)
