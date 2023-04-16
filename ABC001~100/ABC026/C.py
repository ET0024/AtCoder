import sys

sys.setrecursionlimit(10 ** 6)
n = int(input())
child = [[] for _ in range(n)]
memo = [-1 for _ in range(n)]

for i in range(1, n):
    b = int(input())
    child[b - 1].append(i)


def salary(node):
    if len(child[node]) == 0:
        memo[node] = 1
        return 1
    elif memo[node] != -1:
        return memo[node]
    else:
        mx = -1
        mn = float('inf')
        for c in child[node]:
            s = salary(c)
            memo[c] = s
            if s > mx:
                mx = s
            if s < mn:
                mn = s
        return mx + mn + 1


print(salary(0))
