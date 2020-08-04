from collections import deque


def nearlist(N, LIST):  # 隣接リスト
    NEAR = [set() for _ in range(N)]
    for a, b in LIST:
        NEAR[a - 1].add(b - 1)
        NEAR[b - 1].add(a - 1)
    return NEAR


def bfs(NEAR, S):  # 幅優先探索  # キュー
    ans[S] = c.pop()
    que, frag = deque([S]), set([S])

    while len(que) > 0:
        q = que.popleft()
        for i in NEAR[q]:  # 移動先の候補
            if i in frag:  # 処理済みか否か
                continue
            ans[i] = c.pop()
            que.append(i), frag.add(i)
    return ans


n = int(input())
ab = [list(map(int, input().split())) for _ in range(n - 1)]
c = sorted(map(int, input().split()))

ans = [0] * n
near = nearlist(n, ab)
print(sum(c) - max(c))
print(*bfs(near, 0))
