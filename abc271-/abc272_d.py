def grid_bfs(s0, h0, w0, near0):
    sx, sy = s0
    dist = [[-1] * w0 for _ in range(h0)]
    dist[sx][sy] = 0
    que = [s0]

    for qx, qy in que:
        dq = dist[qx][qy]
        for dx, dy in near0:
            px, py = qx+dx, qy+dy
            if 0 <= px < h0 and 0 <= py < w0:
                if dist[px][py] > -1:
                    continue
                dist[px][py] = 1 + dq
                que.append((px, py))
    return dist


def main():
    def int_sqrt(num):
        res = int(num**0.5)-1
        while (res+1)**2 <= num:
            res += 1
        return res

    root_m = int_sqrt(M)
    near = []
    for i in range(root_m+1):
        for j in range(root_m+1):
            if i**2 + j**2 == M:
                res = [(i, j), (-i, j), (i, -j), (-i, -j)]
                near += res

    ans = grid_bfs((0, 0), N, N, near)
    for ai in ans:
        print(*ai)
    return


if __name__ == '__main__':
    N, M = map(int, input().split())

    main()
