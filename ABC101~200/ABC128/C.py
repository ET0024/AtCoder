from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)
for lb in range(m):
    tmp = list(map(int, input().split()))
    k = tmp[0]
    s = tmp[1:]
    for sw in s:
        d[sw - 1].append(lb)

p = list(map(int, input().split()))


# bit full search
ALL = 1 << n
ans = 0
for pattern in range(ALL):
    # print('======trying pattern', pattern, '======')
    state = [p[i] for i in range(m)]
    for sw in range(n):
        bit = pattern >> sw & 1
        if bit == 1:
            # print('switch no', sw, 'is on')
            for lb in d[sw]:
                state[lb] = (state[lb] + 1) % 2
                # print('lb no', lb, 'toggled')
    # print('state=', state)
    if state.count(0) == len(state):
        ans += 1
        # print('counted!!!!!')

print(ans)
