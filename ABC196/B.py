x = input()

if '.' in x:
    print(x[:x.find('.')])
else:
    print(x)
