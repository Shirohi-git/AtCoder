from collections import defaultdict

n, t = map(int, input().split())
a = list(map(int, input().split()))

buy = a[0]
gain = defaultdict(int)
for ai in a:
    buy = min(buy, ai)
    gain[ai - buy] += 1
print(gain[max(gain)])
