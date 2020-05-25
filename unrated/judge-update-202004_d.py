from itertools import accumulate
from math import gcd
import sys
input = sys.stdin.readline


def binary(N,LIST,I):  # 二分探索 # N:探索要素数
    l, r = -1, N
    while r - l > 1:
        if gcd(LIST[(l + r) // 2], I) == 1:
            r = (l + r) // 2
        else:
            l = (l + r) // 2
    return r + 1


n, q = map(int, input().split())
a = list(map(int, input().split()))
s = list(map(int, input().split()))

agcd = list(accumulate(a, gcd))
for i in s:
    ans = gcd(i, agcd[-1])
    if ans > 1:
        print(ans)
        continue
    print(binary(n,agcd,i))
