from itertools import product

n = int(input())
a = list(map(int, input().split()))

dic = {}
for bit in product([0, 1], repeat=min(n, 8)):
    if sum(bit) == 0:
        continue
    num = sum(ai*bi for ai, bi in zip(a, bit)) % 200
    if num not in dic:
        dic[num] = []
    dic[num].append([i+1 for i, bi in enumerate(bit) if bi])

for k, v in dic.items():
    if len(v) >= 2:
        b = [len(v[0])] + v[0]
        c = [len(v[1])] + v[1]
        print('Yes'), print(*b), print(*c)
        break
else:
    print('No')
