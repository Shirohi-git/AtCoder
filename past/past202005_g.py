from collections import deque,defaultdict


def bfs(BLOCK, G):  # 幅優先探索 
    S = (0, 0)
    dist = defaultdict(int)
    dist[S] = 0
    frag = set([S]) | BLOCK
    que = deque([S])

    while len(que) > 0:
        x,y = que.popleft()
        near = [(x + 1, y + 1), (x, y + 1), (x - 1, y + 1),
                (x + 1, y), (x - 1, y), (x, y - 1)]
        for i, j in near:
            if (i, j) in frag:
                continue
            if (i, j) == G:
                return dist[(x, y)] + 1
            if (-201 <= i <= 201) and (-201 <= j <= 201):
                dist[(i, j)] = dist[(x, y)] + 1
                que.append((i, j))
                frag.add((i, j))
    return - 1


n, gx, gy = map(int, input().split())
xy = set([tuple(map(int, input().split())) for _ in range(n)])

print(bfs(xy, (gx, gy)))
