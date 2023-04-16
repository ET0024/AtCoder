N = int(input())
S = [input() for _ in range(N)]
S2 = ['!'+S[i] for i in range(N)]

S = set(S)
S2 = set(S2)
S3  = S & S2

if len(S3) > 0:
    print(list(S3)[0][1:])
else:
    print('satisfiable')
