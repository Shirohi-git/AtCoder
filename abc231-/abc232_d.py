def grid_bfs(s0, h0, w0):
    sx, sy = s0
    flag = [[0] * w0 for _ in range(h0)]
    flag[sx][sy] = 1
    que = [s0]

    near = [(0, 1), (1, 0)]
    for qx, qy in que:
        for dx, dy in near:
            px, py = qx+dx, qy+dy
            if 0 <= px < h0 and 0 <= py < w0:
                if flag[px][py] or C[px][py] == '#':
                    continue
                flag[px][py] = 1
                que.append((px, py))
    return flag


def main():
    res = grid_bfs((0, 0), H, W)
    ans = []
    for i in range(H):
        ans += [i+j+1 for j in range(W) if res[i][j]]
    return print(max(ans))


if __name__ == '__main__':
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]

    main()
