h, w, n = map(int, input().split())
sy, sx = map(int, input().split())
s, t = input(), input()

# 解説AC
l, r, u, d = 1, w, 1, h
for si, ti in zip(s[::-1], t[::-1]):
    l = max(l - (ti == 'R'), 1) + (si == 'L')
    r = min(r + (ti == 'L'), w) - (si == 'R')
    u = max(u - (ti == 'D'), 1) + (si == 'U')
    d = min(d + (ti == 'U'), h) - (si == 'D')
    if l > r or u > d:
        break
print('YES' if l <= sx <= r and u <= sy <= d else 'NO')
