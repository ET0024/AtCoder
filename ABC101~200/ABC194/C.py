n = int(input())
a = list(map(int, input().split()))
a2 = [i ** 2 for i in a]

print(n * sum(a2) - sum(a) ** 2)
