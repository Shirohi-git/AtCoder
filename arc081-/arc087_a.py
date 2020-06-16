from collections import Counter

n = int(input())
a = Counter(map(int, input().split()))

ans = 0
for i in a:
    if a[i] > i:
        ans += a[i] - i
    elif a[i] < i:
        ans += a[i]
print(ans)
