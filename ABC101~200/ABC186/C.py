n = int(input())

count = 0
for i in range(1, n + 1):
    # print(i, oct(i))
    if '7' not in str(i) and '7' not in oct(i):
        count += 1

print(count)
