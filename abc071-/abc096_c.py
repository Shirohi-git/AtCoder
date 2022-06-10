h, w = map(int, input().split())
s = ['.' * (w + 2)]
s += ['.' + input() + '.' for _ in range(h)]
s += ['.' * (w + 2)]

ans = 1
for i in range(1, h + 1):
    for j in range(1, w + 1):
        vec = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        res = (s[i][j] == '#')
        res &= any(s[x][y] == '#' for x, y in vec)
        ans &= res | (s[i][j] == '.')
print('Yes' if ans else 'No')
