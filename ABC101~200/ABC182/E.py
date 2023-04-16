import bisect

H, W, N, M = map(int, input().split())

A = []
B = []
C = []
D = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
for _ in range(M):
    c, d = map(int, input().split())
    C.append(c)
    D.append(d)

A_asort, B_asort = zip(*sorted(zip(A, B)))
A_bsort, B_bsort = zip(*sorted(zip(B, A)))
C_csort, D_csort = zip(*sorted(zip(C, D)))
C_dsort, D_dsort = zip(*sorted(zip(D, C)))

for light in range(N):
    x, y = A[light], B[light]
    ind_x =