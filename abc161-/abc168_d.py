from collections import deque


def nearlist(N, LIST):
    NEAR = [set() for _ in range(N)]
    for a, b in LIST:
        NEAR[a - 1].add(b - 1)
        NEAR[b - 1].add(a - 1)
    return NEAR


def bfs(NEAR, S, N):  # 幅優先探索  # キュー
    PATH = [-1 for _ in range(N)]
    PATH[S] = 's'
    frag, que = set([S]), deque([S])

    while len(que) > 0:
        q = que.popleft()
        for i in NEAR[q]:
            if i in frag:
                continue
            PATH[i] = q
            que.append(i), frag.add(i)
    return PATH


n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

near = nearlist(n, ab)
path = bfs(near, 0, n)

print('Yes')
for i in range(1, n):
    print(path[i] + 1)
