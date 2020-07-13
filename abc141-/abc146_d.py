from collections import deque

def nearlist(N, LIST):  # 隣接リスト
    NEAR = [[] for _ in range(N)]
    for a, b in LIST:
        NEAR[a - 1].append(b - 1)
        NEAR[b - 1].append(a - 1)
    return NEAR


def bfs(NEAR, S, COLOR, ANS):  # 幅優先探索  # キュー
    # 隣点リスト,始点,数
    que, frag = deque([S]), set([S])

    while len(que) > 0:
        q = que.popleft()
        c, cnt = COLOR[q], 0
        for i in NEAR[q]:  # 移動先の候補
            if i in frag:  # 処理済みか否か
                continue
            cnt += 1 + (cnt == c - 1)
            COLOR[i] = cnt
            ANS[(q, i)], ANS[(i, q)] = cnt, cnt
            que.append(i), frag.add(i)
    return


n = int(input())
ab = [list(map(int, input().split())) for _ in range(n - 1)]

color, ans = [-1] * n, {}
near = nearlist(n, ab)
bfs(near, 0, color, ans)
print(max(ans.values()))
for a, b in ab:
    print(ans[(a - 1, b - 1)])
