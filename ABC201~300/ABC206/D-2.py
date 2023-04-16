from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


#
# # --- UnionFind study ---
# uf = UnionFind(10)
#
# # unite two groups by O(log(n))
# uf.union(1, 3)
# uf.union(1, 5)
# uf.union(2, 4)
# print(uf)
#
# # return root by O(log(n))
# print('print(uf.find(1))')
# print(uf.find(1))
#
# # complexity?????
# print('print(uf.size(1))')
# print(uf.size(1))
#
# # return if x, y belong to same group or not / O(log(n))
# print('print(uf.same(1, 3))')
# print(uf.same(1, 3))
# print('print(uf.same(2, 3))')
# print(uf.same(2, 3))
#
# # return members by O(n * log(n)) <- call find(x) * n times
# print('print(uf.members(3))')
# print(uf.members(3))
#
# # return root nodes by O(n)
# print('print(uf.roots())')
# print(uf.roots())
#
# # return # of groups by O(n)
# print('print(uf.group_count())')
# print(uf.group_count())
#
# # return all member info by O(n^2 * log(n)) <- call members * n times
# print('print(uf.all_group_members())')
# print(uf.all_group_members())
#
# # string expression implemented
# print('print(uf)')
# print(uf)
#

n = int(input())
a = list(map(int, input().split()))

uft = UnionFind(n)

# initial tree construction
hash_table = {}
for i, val in enumerate(a):
    if val not in hash_table.keys():
        hash_table[val] = i
    else:
        uft.union(i, hash_table[val])

# circular check
count = 0
for i in range(n // 2):
    left = i
    right = n - 1 - i

    if not uft.same(left, right):
        count += 1
        uft.union(left, right)

print(count)
