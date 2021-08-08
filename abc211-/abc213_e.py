from collections import deque


def bfs(n0):
    flag = [H*W] * n0
    flag[0] = 0
    que = deque([(0, 0)])
    near = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    dic2 = list(range(-3, 4))
    near2 = [(i, j) for i in dic2 for j in dic2 if 1 < abs(i) + abs(j) < 5]

    while que:
        qx, qy = que.popleft()
        cnt = flag[qx*W + qy]
        if (qx, qy) == (H-1, W-1):
            return cnt

        for dx, dy in near:
            px, py = qx+dx, qy+dy
            if 0 <= px < H and 0 <= py < W:
                if flag[px*W + py] > cnt and S[px][py] == '.':
                    flag[px*W + py] = cnt
                    que.appendleft((px, py))
        for dx, dy in near2:
            px, py = qx+dx, qy+dy
            if 0 <= px < H and 0 <= py < W and flag[px*W + py] > cnt+1:
                if (abs(dx)+abs(dy) < 4 and max(abs(dx), abs(dy)) < 3) or S[px][py] == '.':
                    flag[px*W + py] = cnt + 1
                    que.append((px, py))
    return -1


def main():
    ans = bfs(H*W)
    return print(ans)


if __name__ == '__main__':
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    main()
