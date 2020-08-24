from collections import deque


def bfs(S):  # 幅優先探索  # キュー
    dist = [-1] * (w * h)  # 前処理
    que = deque()
    for i, Si in enumerate(S):
        for j, Sij in enumerate(Si):
            if Sij == '#':
                dist[j + (w * i)] = 0
                que.append((i, j))

    while len(que) > 0:
        (x, y) = que.popleft()
        near = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for i, j in near:  # 移動先の候補
            if 0 <= i < h and 0 <= j < w and dist[j + (w * i)] < 0:
                dist[j + (w * i)] = dist[y + (w * x)] + 1
                que.append((i, j))
    return max(dist)


h, w = map(int, input().split())
a = [input() for _ in range(h)]
print(bfs(a))
