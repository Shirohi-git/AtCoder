from collections import deque


def nearlist(N, LIST):  # 隣接リスト
    NEAR = [set() for _ in range(N)]
    for a, b in LIST:
        NEAR[a - 1].add(b - 1)
        NEAR[b - 1].add(a - 1)
    return NEAR


def bfs(NEAR, S, N):  # 幅優先探索  # キュー
    dist = [-1 for _ in range(N)]  # 前処理
    dist[S] = 0
    que, frag = deque([S]), set([S])

    while len(que) > 0:
        q = que.popleft()
        for i in NEAR[q]:  # 移動先の候補
            if i in frag:  # 処理済みか否か
                continue
            dist[i] = dist[q] + 1
            que.append(i), frag.add(i)
    return dist


n, u, v = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n - 1)]

near = nearlist(n, ab)
tkdist, akdist = bfs(near, u - 1, n), bfs(near, v - 1, n)

node = [i for i in range(n) if tkdist[i] <= akdist[i]]
ans = max(akdist[i] for i in node)
print(ans - 1)
