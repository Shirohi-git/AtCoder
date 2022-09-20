def dfs(sx, sy, near0):
    dist = [[-1] * W for _ in range(H)]
    dist[sx][sy] = 1
    near_it = [[] for _ in range(H*W)]
    near_it[sx*W + sy] = iter(near0[sx*W + sy])

    res = -1
    stack = [(sx, sy)]
    while stack:
        qx, qy = stack[-1]
        dist_q = dist[qx][qy]
        for px, py in near_it[qx*W + qy]:
            if (px, py) == (sx, sy) and dist_q > 2:
                res = max(res, dist_q)
            if dist[px][py] < 0:
                dist[px][py] = dist_q + 1
                stack.append((px, py))
                near_it[px*W + py] = iter(near0[px*W + py])
                break
        else:
            dist[qx][qy] = -1
            stack.pop()
    return res


def main():
    near = [[] for _ in range(H*W)]
    for i in range(H):
        for j in range(W):
            if C[i][j] == '#':
                continue
            for dx, dy in DIR:
                x, y = i+dx, j+dy
                if 0 <= x < H and 0 <= y < W and C[x][y] == '.':
                    near[i*W + j].append((x, y))
    ans = -1
    for i in range(H):
        for j in range(W):
            if C[i][j] == '.':
                ans = max(ans, dfs(i, j, near))
    return print(ans)


if __name__ == '__main__':
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    main()
