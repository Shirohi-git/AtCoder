from collections import deque


def bfs(n0):
    flag = [H*W] * n0
    flag[0] = 0
    que = deque([(0, 0)])
    near = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    near2 = [(i, j) for i in range(-2, 3) for j in range(-2, 3)]

    def move(x, y, c, one):
        for dx, dy in (near2 if one else near):
            px, py, p = x+dx, y+dy, (x+dx)*W + (y+dy)
            if 0 <= px < H and 0 <= py < W and flag[p] > c + one:
                if 1-one and S[px][py] == '.':
                    flag[p] = c
                    que.appendleft((px, py))
                if one and abs(dx) + abs(dy) < 4:
                    flag[p] = c + one
                    que.append((px, py))
        return

    while que:
        qx, qy = que.popleft()
        cnt = flag[qx*W + qy]
        if (qx, qy) == (H-1, W-1):
            return cnt
        move(qx, qy, cnt, 0), move(qx, qy, cnt, 1)
    return -1


def main():
    ans = bfs(H*W)
    return print(ans)


if __name__ == '__main__':
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    main()
