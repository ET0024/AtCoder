n = int(input())
w = set(input().split())
ans = set(["and","not","that","the","you"])
if len(ans.intersection(w)) > 0:
    print("Yes")
else:
    print("No")
