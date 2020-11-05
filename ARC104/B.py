# def get_complementary(s):
#     s = s.replace("A", "x")
#     s = s.replace("T", "A")
#     s = s.replace("x", "T")
#     s = s.replace("C", "x")
#     s = s.replace("G", "C")
#     s = s.replace("x", "G")
#     return s


n, s = input().split()
n = int(n)

ans = 0

for i in range(n):

    at_count = 0
    cg_count = 0
    for j in range(i, n):
        if s[j] == "A":
            at_count += 1
        elif s[j] == "T":
            at_count -= 1
        elif s[j] == "C":
            cg_count += 1
        elif s[j] == "G":
            cg_count -= 1
        if at_count == 0 and cg_count == 0:
            ans += 1

print(ans)

# sc = get_complementary(s)
# count = 0
#
# for i in range(n-1):
#     for j in range(i+1, n+1):
#         # print(i,j)
#         # print(s[i:j])
#         if sorted(s[i:j])==sorted(sc[i:j]):
#             count += 1
#             # print("s:", s[i:j])
#             # print("sc:", sc[i:j])
#
# print(count)
# print(n, s)
# print(get_complementary(s))