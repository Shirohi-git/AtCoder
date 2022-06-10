from itertools import accumulate
from collections import Counter

n, m = map(int, input().split())
a = list(map(int, input().split()))

acc = [0] + list(accumulate(a))
modcnt = Counter(num % m for num in acc)
ans = 0
for cnt in modcnt.values():
    ans += cnt * (cnt - 1) // 2
print(ans)
