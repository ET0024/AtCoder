import heapq

# a = [-1, 3, 1, 10, 8, 4, 5, 6]
# a = [[1, "a"], [5, "b"],[3, "c"]]
a = [(1, "a"), (5, "b"), (3, "c")]
print(a)
heapq.heapify(a)
print(a)

while len(a)>0:
    print(heapq.heappop(a))
    print("len:", len(a))

