import numpy as np
from copy import deepcopy

n = int(input())
a = np.array([list(map(int, input().split())) for _ in range(n)])

print(n)
for i in range(n):
    ans = deepcopy(a)
    for j in range(n):
        ans[i][j] *= -1
    for j in range(n):
        ans[j][i] *= -1
    for ai in ans:
        print(*ai)
