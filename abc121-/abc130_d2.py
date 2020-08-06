from itertools import accumulate

n, k = map(int, input().split())
a = list(map(int, input().split()))
a = [0] + list(accumulate(a))

# 尺取法 O(n)
tmp, ans = 0, 0
for i in range(n + 1):
    for j in range(tmp, n + 1):
        if a[j] - a[i] >= k:
            ans += n - j + 1
            tmp = j
            break
print(ans)
