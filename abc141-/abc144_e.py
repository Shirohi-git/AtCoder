def binary(N):
    l, r = -1, N
    while r - l > 1:
        x = (l + r) // 2
        cnt = sum(max(0, ai - x // fi) for ai, fi in zip(a, f))
        r += (x - r) * (cnt <= k)
        l += (x - l) * (cnt > k)
    return r

n, k = map(int, input().split())
a = sorted(map(int, input().split()))
f = sorted(map(int, input().split()))[::-1]

print(binary(a[-1] * f[0]))
