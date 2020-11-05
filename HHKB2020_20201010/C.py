n = int(input())
p_list = list(map(int, input().split()))

candidate_int = set(range(n))

for i in range(n):
    candidate_int -= set([p_list[i]])
    print(min(candidate_int))
    # print(min(candidate_int - set(p_list[0:i+1])))
