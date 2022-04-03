def grid_bfs(s0, h0, w0):
    from collections import deque

    sx, sy = s0
    flag = [[INF] * (w0 * h0) for _ in range(2)]
    flag[0][sx*w0 + sy] = flag[1][sx*w0 + sy] = 1
    que = deque([(sx, sy, 0), (sx, sy, 1)])
    near = [(1, 1, 0), (1, -1, 1), (-1, -1, 0), (-1, 1, 1)]

    while que:
        qx, qy, qc = que.popleft()
        bfo_d = flag[qc][qx*w0 + qy]
        for dx, dy, dc in near:
            px, py, pc = qx + dx, qy + dy, qc ^ dc
            if 0 <= px < h0 and 0 <= py < w0 and S[px][py] == '.':
                if flag[dc][px*w0 + py] <= bfo_d + pc:
                    continue
                flag[dc][px*w0 + py] = bfo_d + pc
                if pc:
                    que.append((px, py, dc))
                else:
                    que.appendleft((px, py, dc))
    return flag


def main():
    ax, ay, bx, by = AX-1, AY-1, BX-1, BY-1
    dist = grid_bfs((ax, ay), N, N)
    ans = min(dist[0][bx*N + by], dist[1][bx*N + by])
    return print(-1 if ans == INF else ans)


if __name__ == '__main__':
    N = int(input())
    AX, AY = map(int, input().split())
    BX, BY = map(int, input().split())
    S = [input() for _ in range(N)]
    INF = 10**9

    main()
