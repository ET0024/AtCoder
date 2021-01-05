N = int(input())

a = list(map(int, input().split()))

gcd = 0
ans = 0

for k in range(2, 1001):
    count = 0

    for item in a:
        if item % k == 0:
            count += 1

    if count > gcd:
        ans = k
        gcd = count

print(ans)