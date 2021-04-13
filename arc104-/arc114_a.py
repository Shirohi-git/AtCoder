from itertools import product
from math import gcd

n = int(input())
x = list(map(int, input().split()))

ans = float('inf')
plst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
for bit in product([0, 1], repeat=15):
    lst = [pi * bi for pi, bi in zip(plst, bit) if bi]
    num = 1
    for li in lst:
        num *= li
    if all(gcd(xi, num) > 1 for xi in x):
        ans = min(ans, num)
print(ans)
