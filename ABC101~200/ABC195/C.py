n = int(input())

count = 0
for i in range(1, 6):
    count += max(n-1000**i+1, 0)

print(count)