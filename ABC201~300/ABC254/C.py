n, k = map(int, input().split())
a = list(map(int, input().split()))

sorted_list = []
for i in range(k):
    sorted_list.append(sorted(a[i::k]))

    if i > 0 and len(sorted_list[-1]) < len(sorted_list[0]):
        sorted_list[-1].append(10 ** 10)

prev = 0
curr = 0
for col in range(len(sorted_list[0])):
    for row in range(len(sorted_list)):
        prev = curr
        curr = sorted_list[row][col]
        if curr < prev:
            print('No')
            exit()

print('Yes')
