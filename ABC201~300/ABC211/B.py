s = []
s.append(input())
s.append(input())
s.append(input())
s.append(input())
s.sort()

answer = ['H', '2B', '3B', 'HR']
answer.sort()

for i in range(4):
    if answer[i] != s[i]:
        print('No')
        exit()

print('Yes')