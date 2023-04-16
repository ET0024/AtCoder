n = int(input())
w = list(input().split())
target = ["and", "not", "that", "the", "you"]

for word in w:
    if word in target:
        print('Yes')
        exit()

print('No')