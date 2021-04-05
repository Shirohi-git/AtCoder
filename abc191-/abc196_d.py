from copy import deepcopy


def nextgrid(stt):
    for i, si in enumerate(stt):
        for j, sij in enumerate(si):
            if sij:
                return (i, j)


def add_tatami(r, s, nx, ny, stt):
    stt[nx][ny] = 0
    if r > 0:
        for x, y in [(nx + 1, ny), (nx, ny + 1)]:
            if x < h and y < w and stt[x][y]:
                stt[x][y] = 0
                que.append((r - 1, s, deepcopy(stt)))
                stt[x][y] = 1
    if s > 0:
        que.append((r, s - 1, deepcopy(stt)))


h, w, a, b = map(int, input().split())

ans = 0
room = [[1] * w for _ in range(h)]
que = [(a, b, room)]
for rect, squa, status in que:
    if rect == squa == 0:
        ans += 1
        continue
    next = nextgrid(status)
    add_tatami(rect, squa, *next, status)
print(ans)
