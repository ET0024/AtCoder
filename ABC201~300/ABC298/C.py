from collections import defaultdict

n = int(input())
q = int(input())
box = [[] for _ in range(n)]
box_info = defaultdict(set)

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        i, j = query[1], query[2]
        box[j - 1].append(i)
        box_info[i].add(j)
    elif query[0] == 2:
        i = query[1]
        print(*sorted(box[i - 1]))
    else:
        i = query[1]
        print(*sorted(box_info[i]))
