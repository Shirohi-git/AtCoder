from collections import deque


def bfs(S, G, H, W):
    (sx, sy), (gx, gy) = S, G
    dist = [[-1] * W for _ in range(H)]
    dflag = [0] * 26
    dist[sx][sy] = 0
    que = deque([S])

    vec = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while que:
        p, q = que.popleft()
        for dx, dy in vec:
            i, j = p + dx, q + dy
            if 0 <= i < H and 0 <= j < W:
                if a[i][j] == '#':
                    dist[i][j] = 0
                elif dist[i][j] < 0:
                    dist[i][j] = dist[p][q] + 1
                    que.append((i, j))

        num = ord(a[p][q]) - ord('a')
        if 0 <= num < 26 and dflag[num] == 0:
            for i, j in dic[num]:
                if dist[i][j] < 0:
                    dist[i][j] = dist[p][q] + 1
                    que.append((i, j))
            dflag[num] = 1
    return dist[gx][gy]


h, w = map(int, input().split())
a = [input() for _ in range(h)]

dic = {i: [] for i in range(26)}
for i in range(h):
    for j in range(w):
        num = ord(a[i][j]) - ord('a')
        if num == -14:
            s = (i, j)
        elif num == -26:
            g = (i, j)
        elif 0 <= num < 26:
            dic[num].append((i, j))
print(bfs(s, g, h, w))
