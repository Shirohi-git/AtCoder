from itertools import product

n, m, k = map(int, input().split())

for i, j in product(range(n + 1), range(m + 1)):
    if i * (m - j) + j * (n - i) == k:
        print('Yes')
        break
else:
    print('No')
