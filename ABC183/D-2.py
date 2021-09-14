n, w = map(int, input().split())
wl = [0 for _ in range(2 * 10 ** 5 + 1)]

for _ in range(n):
    s, t, p = map(int, input().split())
    wl[s] += p
    wl[t] -= p

ac_wl = 0
for val in wl:
    ac_wl += val
    if ac_wl > w:
        print('No')
        exit()

print('Yes')
