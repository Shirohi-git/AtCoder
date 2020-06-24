from collections import Counter

n = int(input())
a = list(map(int, input().split()))
minus = Counter([i - a[i] for i in range(n)])
plus = Counter([i + a[i] for i in range(n)])

cnt = 0
for i in minus:
    if i in plus:
        cnt += minus[i] * plus[i]
print(cnt)
