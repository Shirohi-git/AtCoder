from collections import deque


def bfs(S, G, H, W):
    (sx, sy), (gx, gy) = S, G
    dist = [[-1] * w for _ in range(h)]
    dflag = [0] * 26
    dist[sx][sy] = 0
    que = deque([S])

    while que:
        p, q = que.popleft()
        vec1 = [(p + 1, q), (p - 1, q), (p, q + 1), (p, q - 1)]
        for i, j in vec1:
            if 0 <= i < h and 0 <= j < w:
                if a[i][j] == '#':
                    dist[i][j] = 0
                if dist[i][j] < 0:
                    dist[i][j] = dist[p][q] + 1
                    que.append((i, j))

        num = ord(a[p][q]) - ord('a')
        if 0 <= num < 26 and dflag[num] == 0:
            vec2 = dic[num]
            for i, j in vec2:
                if a[i][j] == '#':
                    dist[i][j] = 0
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
        if a[i][j] == 'S':
            s = (i, j)
        elif a[i][j] == 'G':
            g = (i, j)
        elif 0 <= num < 26:
            dic[num].append((i, j))
print(bfs(s, g, h, w))
