def ceil(X, Y):  # 天井関数 ceil(X/Y) Y>1
    return (X + Y - 1) // Y


def binary(N):  # 二分探索 # N:探索要素数
    l, r = -1, N
    while r - l > 1:
        if (l + r) // 2 == 0:
            return 1
        cnt = sum(ceil(ai, (l + r) // 2) - 1 for ai in a)
        if cnt <= k:  # 条件式を代入
            r = (l + r) // 2
        else:
            l = (l + r) // 2
    return r


n, k = map(int, input().split())
a = list(map(int, input().split()))

# 解説AC
print(binary(max(a)))
