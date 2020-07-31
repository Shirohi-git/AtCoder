h, w, k = map(int, input().split())
s = [input() for _ in range(h)]

ans = [[0] * w for _ in range(h)]
cnt, first = 1, -1
for i in range(h):
    tmp = 0
    if '#' in s[i]:
        if first == -1:
            first = i
        for j in range(w):
            if s[i][j] == '#':
                tmp += 1
                if tmp > 1:
                    cnt += 1
            ans[i][j] = cnt
        cnt += 1
    else:
        if i > 0:
            ans[i] = ans[i - 1][:]

for q in range(first):
    ans[q] = ans[first][:]

for i in range(h):
    print(*ans[i])
