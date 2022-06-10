from collections import deque


def bfs():
    dist = [[0] * w for _ in range(h)]
    flag = [[0] * w for _ in range(h)]
    flag[0][0], dist[0][0] = 1, 1
    que = deque([(0, 0)])
    near = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while que:
        p, q = que.popleft()
        for dx, dy in near:
            x, y = p + dx, q + dy
            if 0 <= x < w and 0 <= y < h:
                if flag[y][x] or s[y][x] == '#':
                    continue
                dist[y][x] = dist[q][p] + 1
                flag[y][x] = 1
                que.append((x, y))
    return dist[-1][-1]


h, w = map(int, input().split())
s = [input() for _ in range(h)]

cnt = sum(si.count('.') for si in s)
dist = bfs()
print(cnt - dist if dist else - 1)
