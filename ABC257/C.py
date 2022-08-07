import bisect

n = int(input())
s = input()
w = list(map(int, input().split()))

adalt = []
child = []

for i, flag in enumerate(s):
    if flag == '0':
        child.append(w[i])
    else:
        adalt.append(w[i])
child.sort()
adalt.sort()
w.sort()
ans = 0
for weight in w:
    for d in [-1, 0, 1]:
        target = weight + d
        score = 0
        score += bisect.bisect_left(child, target)
        score += len(adalt) - bisect.bisect_left(adalt, target)

        # print('-------debug----------')
        # print(target)
        # print(child)
        # print(adalt)
        # print('child-part:', bisect.bisect_left(child, target))
        # print('adalt-part:', len(adalt) - bisect.bisect_left(adalt, target))
        # print(score)

        if score > ans:
            ans = score

print(ans)
