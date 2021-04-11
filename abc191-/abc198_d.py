from collections import defaultdict
from itertools import permutations

s1, s2, s3 = input(), input(), input()

cset = set(list(s1 + s2 + s3))
if len(cset) > 10:
    exit(print('UNSOLVABLE'))
cdic = defaultdict(int)
for i, c in enumerate(cset):
    cdic[c] = i
s1 = [cdic[si] for si in s1]
s2 = [cdic[si] for si in s2]
s3 = [cdic[si] for si in s3]

for lst in permutations([str(i) for i in range(10)], len(cset)):
    n1 = ''.join([lst[si] for si in s1])
    n2 = ''.join([lst[si] for si in s2])
    n3 = ''.join([lst[si] for si in s3])
    if '0' in [n1[0], n2[0], n3[0]]:
        continue
    if int(n1) + int(n2) == int(n3):
        print(n1, n2, n3, sep='\n')
        break
else:
    print('UNSOLVABLE')
