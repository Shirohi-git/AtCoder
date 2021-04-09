def count(lst):
    res = 0
    for li in lst:
        if li == '#':
            return res
        res += 1
    return res

h, w, x, y = map(int, input().split())
s = [input() for _ in range(h)]

sx = s[x - 1][:]
sy = [s[i][y - 1] for i in range(h)]

ans = count(sx[y - 1:]) + count(sx[y - 1::-1])
ans += count(sy[x - 1:]) + count(sy[x - 1::-1])
print(ans - 3)
