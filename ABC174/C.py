k = int(input())

res = 0
for i in range(k):
    res = (res * 10 + 7) % k
    if res % k == 0:
        print(i + 1)
        exit()

print(-1)
