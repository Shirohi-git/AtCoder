n, h = map(int, input().split())
a, b = [], []
for _ in range(n):
    ai, bi = map(int, input().split())
    a.append(ai), b.append(bi)
a.sort(), b.sort()

ans, amax = 0, a[-1]
for bi in b[::-1]:
    if bi <= amax or h <= 0:
        break
    h -= bi
    ans += 1
mod = (h + amax - 1) // amax
print(ans + mod if h > 0 else ans)
