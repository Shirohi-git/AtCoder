from bisect import bisect

a, b, q = map(int, input().split())
s = [-10 ** 11] + [int(input()) for _ in range(a)] + [10 ** 11]
t = [-10 ** 11] + [int(input()) for _ in range(b)] + [10 ** 11]
x = [int(input()) for _ in range(q)]

for xi in x:
    p, q = bisect(s, xi), bisect(t, xi)
    sl, sr = abs(s[p - 1] - xi), abs(s[p] - xi)
    tl, tr = abs(t[q - 1] - xi), abs(t[q] - xi)
    ans = min(max(sl, tl), sl + tr + min(sl, tr),
              max(sr, tr), sr + tl + min(sr, tl))
    print(ans)
