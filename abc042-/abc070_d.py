def nearlist(N, LIST):  # 隣接リスト
    NEAR = [{} for _ in range(N)]
    for a, b, c in LIST:
        NEAR[a - 1][b - 1] = c
        NEAR[b - 1][a - 1] = c
    return NEAR


def dfs(NEAR, S, N):  # 深優先探索  # スタック
    DIST = [-1 for _ in range(N)]  # 前処理
    DIST[S] = 0
    stack, frag = [S], set([S])

    while stack:
        q = stack.pop()
        for i, c in NEAR[q].items():  # 移動先の候補
            if i in frag:  # 処理済みか否か
                continue
            DIST[i] = DIST[q] + c
            stack.append(i), frag.add(i)
    return DIST


n = int(input())
abc = [list(map(int, input().split())) for _ in range(n - 1)]
q, k = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(q)]

near = nearlist(n, abc)
dist = dfs(near, k - 1, n)
for x, y in xy:
    print(dist[x - 1] + dist[y - 1])
