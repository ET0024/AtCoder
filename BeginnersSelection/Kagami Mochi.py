n = int(input())

d = []
for i in range(n):
    d.append(int(input()))

print(len(set(d)))

# kagami = []
#
# for d in reversed(d):
#
#     print('debug: --------------------')
#     print('debug: currentKagami=', kagami)
#     print('debug: received=', d)
#
#     if len(kagami)==0:
#         kagami.append(d)
#         print('debug: append')
#     elif d > kagami[-1]:
#         kagami.append(d)
#         print('debug: append')
#     elif d < kagami[-1] & (len(kagami)>=2 & d > kagami[-2]):
#         kagami[-1] = d
#         print('debug: replaced')
#     else:
#         print('debug: skipped')
#         pass
#
#
# print(len(kagami))