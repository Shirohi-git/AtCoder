from collections import Counter, defaultdict
import sys
input = sys.stdin.readline

n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
mod = 1000000007

zero = sum([1 for a, b in ab if a ==  b == 0])
adivb = [(float('inf') if b == 0 else a / b)
         for a, b in ab if not(a == b == 0)]
bdiva = [(float('inf') if a == 0 else -b / a)
         for a, b in ab if not(a == b == 0)]

adb, bda = Counter(adivb), Counter(bdiva)
cntadb, cnt = defaultdict(int), 0
for i in adb:
    if (i in bda) and (i > 0):
        cntadb[i] += 2 ** bda[i] + 2 ** adb[i] - 1
        cnt += bda[i] + adb[i]
ans = 1
for i in cntadb:
    ans *= cntadb[i]
    ans %= mod
if zero > 0:
    print(ans * pow(2, n - cnt - zero, mod) + zero +1 % mod)
else:
    print(ans * pow(2, n - cnt, mod) - 1 % mod)