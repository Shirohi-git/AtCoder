from itertools import accumulate


def binary(N, num):  # 二分探索 # N:探索要素数
    l, r = -1, N
    while r - l > 1:
        if a[(l + r) // 2] - num >= k:
            r = (l + r) // 2
        else:
            l = (l + r) // 2
    return r


n, k = map(int, input().split())
a = list(map(int, input().split()))
a = [0] + list(accumulate(a))

# 二分探索 O(nlogn)
ans = 0
for i in a:
    ans += n - binary(n + 1, i) + 1
print(ans)
