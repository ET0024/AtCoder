n = int(input())
child = [[] for _ in range(n)]

for i in range(n - 1):
    parent = int(input()) - 1
    child[parent].append(i + 1)

salary = [-1 for _ in range(n)]


def dfs(i):
    if salary[i] > 0:
        return salary[i]

    ch = child[i]
    if len(ch) == 0:
        salary[i] = 1
        return 1
    else:
        values = []
        for c in ch:
            values.append(dfs(c))

        salary[i] = max(values) + min(values) + 1
        return salary[i]


print(dfs(0))
