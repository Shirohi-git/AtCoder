from collections import deque
import sys
input = sys.stdin.readline


def bfs(NEAR, S, N):  # 幅優先探索  # キュー
    pas = [-1 for _ in range(N)]
    pas[S] = 's'
    frag = set([S])
    que = deque([S])

    while len(que) > 0:
        q = que.popleft()
        for i in NEAR[q]:
            if i in frag:
                continue
            pas[i] = q
            que.append(i)
            frag.add(i)
    return pas


n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

near = [[] for _ in range(n)]
for a, b in ab:
    near[a - 1].append(b - 1)
    near[b - 1].append(a - 1)
pas = bfs(near, 0, n)

if all(pas[i] != -1 for i in range(n)):
    print('Yes')
    for i in range(1, n):
        print(pas[i] + 1)
else:
    print('No')
