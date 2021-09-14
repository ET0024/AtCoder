s1 = input()
s2 = input()
s3 = input()

d = {}
d['ABC'] = 0
d['ARC'] = 0
d['AGC'] = 0
d['AHC'] = 0
d[s1] += 1
d[s2] += 1
d[s3] += 1

for k, v in d.items():
    if v == 0:
        print(k)
        exit()
