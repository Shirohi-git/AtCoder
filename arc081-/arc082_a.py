from collections import Counter

n = int(input())
a = Counter(map(int, input().split()))

ans = 0
for i in range(max(a) + 1):
    cnt = a[i - 1] + a[i] + a[i + 1]
    ans = max(cnt, ans)
print(ans)
