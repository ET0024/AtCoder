a, b = input().split()
a = int(a)
b = str(b)
b = int(b.replace('.', ''))

print(a * b // 100)
