from collections import deque

s = input()
Q = int(input())
q = deque(s)

is_reversed = False

for _ in range(Q):
    query = input()
    if len(query) == 1:     # T==1
        is_reversed = not is_reversed
    else:  # T==2
        _, f, c = query.split()
        f = int(f)  # 1(prefix) or 2(postfix)

        if f == 1 and not is_reversed or f == 2 and is_reversed:
            q.appendleft(c)
        else:
            q.append(c)

if not is_reversed:
    print(''.join(q))
else:
    print(''.join(reversed(''.join(q))))
