from collections import deque


def bfs(y, x):
    dist = [[-1] * w for _ in range(h)]
    dist[y][x] = 0
    que, frag = deque([(x, y)]), set([(x, y)])

    while que:
        qx, qy = que.popleft()
        near = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for i, j in near:
            i, j = qx + i, qy + j
            if (i, j) in frag:
                continue
            if 0 <= i < w and 0 <= j < h and s[j][i] == '.':
                dist[j][i] = dist[qy][qx] + 1
                que.append((i, j)), frag.add((i, j))
    return dist[qy][qx]


h, w = map(int, input().split())
s = [input() for _ in range(h)]

ans = 0
for i, si in enumerate(s):
    for j, sij in enumerate(si):
        if sij == '.':
            ans = max(ans, bfs(i, j))
print(ans)
