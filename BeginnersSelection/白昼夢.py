def trim_if_endswith(s, word):
    if s.endswith(word):
        return s[:-len(word)]
    else:
        return s

target = input()


while len(target)>0:

    init_len = len(target)
    target = trim_if_endswith(target, "dream")
    target = trim_if_endswith(target, "dreamer")
    target = trim_if_endswith(target, "erase")
    target = trim_if_endswith(target, "eraser")

    if len(target) == init_len:
        break

if len(target)==0:
    print("YES")
else:
    print("NO")
