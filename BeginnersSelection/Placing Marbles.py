s = map(int, list(input()))

# map object is iterable and cannot be treated as a list !

count = 0
for value in s:
    count += value

print(count)