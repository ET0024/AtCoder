def get_mod(a, m):
    return (a*a) % m


n, x, m = map(int, input().split())

looped_mod_subset = [x]
first_looped_value = -1
a = x

for i in range(max(n, m)):
    a = get_mod(a, m)

    if a not in set(looped_mod_subset):
        looped_mod_subset.append(a)
    else:
        first_looped_value = a
        break

loop_index = looped_mod_subset.index(first_looped_value)
loop_len = len(looped_mod_subset)-loop_index

if n < loop_index:
    ans = sum(looped_mod_subset[0:n])
else:
    ans = sum(looped_mod_subset[0:loop_index])

    loop_times = int((n-loop_index)/loop_len)

    ans += loop_times * sum(looped_mod_subset[loop_index:])
    res_index = n-loop_times*loop_len-loop_index

    if res_index > 0:
        ans += sum(looped_mod_subset[loop_index:loop_index+res_index])

print(ans)
# print("debug:n",n)
# print("debug:m",m)
# print("debug:x",x)
# print("debug:loop_index",loop_index)
# print("debug:loop_val",first_looped_value)
# print("debug:loop_times",loop_times)
# print("debug:looped_sum", sum(looped_mod_subset[loop_index:]))
# print("debug:ans", ans)
# print("debug:loop_len",loop_len)
# print("debug:res_index", n-loop_times*loop_len-loop_index)
# print(looped_mod_subset)
