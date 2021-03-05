h, w = map(int, input().split())
s = [input() for _ in range(h)]

ans = 0
near = [(0, 0), (1, 0), (0, 1), (1, 1)]
for i in range(h - 1):
    for j in range(w - 1):
        cnt = sum(s[i + x][j + y] == '#' for x, y in near)
        ans += cnt % 2
print(ans if ans else 4)
