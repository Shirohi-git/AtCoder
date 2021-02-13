from collections import Counter

n = int(input())
s = [input() for _ in range(n)]

no, ex = Counter(), Counter()
for si in s:
    if si[0] != '!':
        no[si] += 1
    elif si[0] == '!':
        ex[si[1:]] += 1

for si in no:
    if si in ex:
        exit(print(si))
print('satisfiable')
