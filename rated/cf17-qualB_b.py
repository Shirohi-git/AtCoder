from collections import defaultdict

n = int(input())
d = list(map(int, input().split()))
m = int(input())
t = list(map(int, input().split()))

ddict = defaultdict(int)
for i in d:
    ddict[i] += 1

for j in t:
    if ddict[j] >= 1:
        ddict[j] -= 1
    else:
        print('NO')
        break
else:
    print('YES')
