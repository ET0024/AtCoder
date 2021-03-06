s=input()

for i, c in enumerate(s):
    if i%2==0 and str(c).isupper():
        print("No")
        exit()
    elif i%2==1 and str(c).islower():
        print("No")
        exit()

print("Yes")
