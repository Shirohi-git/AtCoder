from collections import deque

def nearlist(N, LIST):  # 隣接リスト
    NEAR = [set([]) for _ in range(N)]
    DIST = {}
    for a, b, c in LIST:
        NEAR[a - 1].add(b - 1)
        NEAR[b - 1].add(a - 1)
        DIST[(a - 1, b - 1)], DIST[(b - 1, a - 1)] = c, c
    return NEAR, DIST


def bfs(NEAR, N):  # 幅優先探索  # キュー
    ANS = [-1 for _ in range(N)]
    ANS[0] = 0
    que, frag = deque([0]), set([0])

    while len(que) > 0:
        q = que.popleft()
        for i in NEAR[q]:  # 移動先の候補
            if i in frag:  # 処理済みか否か
                continue
            if dist[(q, i)] % 2 == 0:
                ANS[i] = ANS[q]
            elif dist[(q, i)] % 2 == 1:
                ANS[i] = -ANS[q] + 1
            que.append(i), frag.add(i)
    return ANS


n = int(input())
uvw = [list(map(int, input().split())) for _ in range(n - 1)]

near, dist = nearlist(n, uvw)
ans = bfs(near, n)
print(*ans, sep='\n')
