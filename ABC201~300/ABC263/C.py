import itertools
n, m = map(int, input().split())

seq = [i + 1 for i in range(m)]
for c in itertools.combinations(seq, n):
    print(*c)

# # permutationsは正解の1組に対してn!の並び替えパターンを列挙してしまうので
# # TLEになるのも納得...
# lst = list(itertools.permutations(seq, n))
# for candidate in lst:
#     if list(candidate) == sorted(list(candidate)):
#         print(*candidate)
