n = int(input())
for_count = 0
for _ in range(n):
    vote = input()
    if vote == 'For':
        for_count += 1

if for_count > n // 2:
    print('Yes')
else:
    print('No')