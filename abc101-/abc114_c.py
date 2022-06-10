from itertools import product

n = int(input())

tfs = set()
for i in range(1,10):
    tfs |= set(product(['3', '5', '7'], repeat=i))

cnt = 0
for l in tfs:
    if ('3' in l) and ('5' in l) and ('7' in l):
        num = int(''.join(l))
        if num <= n:
            cnt += 1
print(cnt)
