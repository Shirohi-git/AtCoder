def grid_bfs(h0, w0, k0, ini, key):

    dist = [[-1] * w0 for _ in range(h0)]
    que = []
    for x, y in ini:
        dist[x][y] = 0
        que.append((x, y))

    near = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def judge(x, y, u, v):
        res = (0 <= u < h0 and 0 <= v < w0 and dist[u][v] < 0)
        if res:
            res = key or (dist[x][y] < k0 and A[u][v] == '.')
        return res

    for qx, qy in que:
        for dx, dy in near:
            px, py = qx+dx, qy+dy
            if judge(qx, qy, px, py):
                dist[px][py] = dist[qx][qy] + 1
                que.append((px, py))
    return dist


def main():

    def ceil(x, y=K):
        return (x + y - 1) // y

    for i, ai in enumerate(A):
        if 'S' in ai:
            s = i, ai.index('S')

    stt = grid_bfs(H, W, K, ini=[s], key=0)
    lst = []
    for x in range(H):
        lst += [(x, y) for y in range(W) if stt[x][y] >= 0]
    d = grid_bfs(H, W, K, ini=lst, key=1)
    r = [d[i][0] for i in range(H)]
    l = [d[i][-1] for i in range(H)]

    ans = min(H, W)
    for lst in (d[0], d[-1], r, l):
        ans = min(ans, min(map(ceil, lst)))
    return print(ans+1)


if __name__ == '__main__':
    H, W, K = map(int, input().split())
    A = [input() for _ in range(H)]

    main()
