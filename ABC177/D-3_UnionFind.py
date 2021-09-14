import sys

sys.setrecursionlimit(10 ** 9)


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            return self.find(self.par[x])

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        else:
            self.par[x] = y
            return


n, m = map(int, input().split())
uf = UnionFind(n)
for _ in range(m):
    a, b = map(int, input().split())
    uf.union(a - 1, b - 1)

count = [0 for _ in range(n)]

for i in range(n):
    count[uf.find(i)] += 1

print(max(count))
