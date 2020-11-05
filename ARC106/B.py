n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

edges = []
isolated_nodes = set(range(1, n + 1))

for i in range(m):
    _edge = tuple(map(int, input().split()))
    edges.append(_edge)
    isolated_nodes -= set(_edge)

is_rejected = False

for isolated_node in isolated_nodes:
    if a[isolated_node - 1] != b[isolated_node - 1]:
        is_rejected = True
        print("rejected in 1st cond")

for edge in edges:
    f, t = edge
    if a[f - 1] + a[t - 1] != b[f - 1] + b[t - 1]:
        is_rejected = True
        print("rejected in 2nd cond", f, t, a[f-1], a[t-1])

if is_rejected:
    print("No")
else:
    print("Yes")
