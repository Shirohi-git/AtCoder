from collections import deque


def bfs(S, G):
    dist = [INF] * (H*W)

    que = deque([(S, -1, -1)])
    while que:
        q, qv, qd = que.popleft()
        if qd > dist[q]:
            continue
        dist[q] = qd
        qx, qy = divmod(q, W)
        near = [(qx+1, qy), (qx, qy+1), (qx-1, qy), (qx, qy-1)]
        for pv, (px, py) in enumerate(near):
            p = px*W + py
            if (0 <= px < H and 0 <= py < W and GRID[px][py] == '.'):
                if dist[p] >= dist[q] and qv == pv:
                    que.appendleft((p, pv, dist[q]))
                elif dist[p] >= dist[q] + 1:
                    que.append((p, pv, dist[q] + 1))
    return dist[G]


# 別ver.
INF = 10**15
if __name__ == '__main__':
    H, W = map(int, input().split())
    SX, SY = map(lambda x: int(x)-1, input().split())
    TX, TY = map(lambda x: int(x)-1, input().split())
    GRID = [input() for _ in range(H)]

    ANS = bfs(SX*W + SY, TX*W + TY)
    print(ANS)
