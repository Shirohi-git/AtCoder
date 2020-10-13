h, w = map(int, input().split())
s = [input() for _ in range(h)]

ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            continue
        if i + 1 < h and s[i + 1][j] == '.':
            ans += 1
        if j + 1 < w and s[i][j + 1] == '.':
            ans += 1
print(ans)
