def binary(l, r):
    while abs(r - l) > 1:
        mid = (l + r) // 2
        cnt = sum((max(0, hi - b * mid) + a - 1) // a for hi in h)
        r += (mid - r) * (cnt <= mid)
        l += (mid - l) * (cnt > mid)
    return r


n, a, b = map(int, input().split())
a = a - b
h = [int(input()) for _ in range(n)]

print(binary(0, 10 ** 9))
