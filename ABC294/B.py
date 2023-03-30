import string

h, w = map(int, input().split())
alphs = ['.'] + list(string.ascii_uppercase)

for _ in range(h):
    a = list(map(int, input().split()))
    ans = ''
    for num in a:
        ans += alphs[num]

    print(ans)
