from collections import deque


def bfs(S):  # 幅優先探索  # キュー
    que = deque([S])
    b, w = 0, 0
    while len(que) > 0:
        p, q = que.popleft()
        b += int(s[p][q] == '#')
        w += int(s[p][q] == '.')
        for i, j in near[p][q]:  # 移動先の候補
            if (i, j) in frag:  # 処理済みか否か
                continue
            if s[i][j] != s[p][q]:
                que.append((i, j)), frag.add((i, j))
    return b * w


h, w = map(int, input().split())
s = [input() for _ in range(h)]

near = [[set() for j in range(w)] for i in range(h)]
for i, si in enumerate(s):
    for j, sij in enumerate(si):
        for p, q in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if 0 <= p < h and 0 <= q < w and s[p][q] != sij:
                near[i][j].add((p, q))

ans, frag = 0,set()
for i in range(h):
    for j in range(w):
        if (i, j) not in frag:
            frag.add((i, j))
            ans += bfs((i, j))
print(ans)
