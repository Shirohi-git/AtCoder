from collections import deque

h, w = map(int, input().split())
s = [list(str(input())) for _ in range(h)]


def bfs(h, w, s, s_h, s_w):
    if s[s_h][s_w] == '#':
        return 0
    d_max = 0
    dist = [[-1 for _ in range(w)] for _ in range(h)]
    dist[s_h][s_w] = 0
    que = deque()
    que.append((s_h, s_w))
    while len(que) > 0:
        q = que.popleft()
        near = [(q[0]+1, q[1]), (q[0], q[1]+1), (q[0]-1, q[1]), (q[0], q[1]-1)]
        for i in near:
            if (i[0] < 0) | (i[0] >= h) | (i[1] < 0) | (i[1] >= w):
                continue
            if (dist[i[0]][i[1]] == -1) & (s[i[0]][i[1]] == '.'):
                dist[i[0]][i[1]] = dist[q[0]][q[1]] + 1
                que.append(i)
                d_max = max(dist[q[0]][q[1]] + 1, d_max)
    return d_max


dmax = 0
for i in range(h):
    for j in range(w):
        dist = bfs(h, w, s, i, j)
        dmax = max(dmax, dist)
print(dmax)
