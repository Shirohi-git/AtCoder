from itertools import accumulate
from collections import Counter

n = int(input())
a = [0] + list(map(int, input().split()))

ans, cnt = 0, Counter(accumulate(a))
for v in cnt.values():
    ans += v * (v - 1) // 2
print(ans)
