from itertools import accumulate


def binary(N, T):  # 二分探索 # N:探索要素数
    l, r = -1, N
    while r - l > 1:
        if T < b[(l + r) // 2]:  # 条件式を代入
            r = (l + r) // 2
        else:
            l = (l + r) // 2
    return r - 1


n, m, k = map(int, input().split())
a = [0] + list(accumulate(map(int, input().split())))
b = [0] + list(accumulate(map(int, input().split())))

ans = 0
for i, ai in enumerate(a):
    t = k - ai
    if t >= 0:
        j = binary(m + 1, t)
        ans = max(ans, i + j)
print(ans)
