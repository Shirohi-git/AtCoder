def binary(N, LIST, num):  # 二分探索 # N:探索要素数
    l, r = -1, N
    while r - l > 1:
        if LIST[(l + r) // 2] > num:  # 条件式を代入
            r = (l + r) // 2
        else:
            l = (l + r) // 2
    return r + 1


n, d, a = map(int, input().split())
xh = sorted(list(map(int, input().split())) for _ in range(n))
x = [i for i, j in xh]
h = [(j + a - 1) // a for i, j in xh]

bomb, bsum, ans = [0] * (n + 1), [0] * (n + 1), 0
for i in range(n):
    j = binary(n, x, x[i] + 2 * d) - 1
    bnum = max(h[i] - (bsum[i - 1] + bomb[i]), 0)
    bomb[i] += bnum
    bomb[j] -= bnum
    bsum[i] += bsum[i - 1] + bomb[i]
    ans += bnum
print(ans)
