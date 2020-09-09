from collections import deque


def nearlist(N, LIST):
    NEAR = [set() for _ in range(N)]
    for a, b in LIST:
        NEAR[a - 1].add(b - 1)
        NEAR[b - 1].add(a - 1)
    return NEAR


def bfs(NEAR):
    que, frag = deque([0]), set([0])
    while que:
        q = que.popleft()
        for i in NEAR[q]:
            if i in frag:
                continue
            ans[i] += ans[q]
            que.append(i), frag.add(i)
    return

n, q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n - 1)]
px = [list(map(int, input().split())) for _ in range(q)]

ans = [0] * n
for p, x in px:
    ans[p - 1] += x

near = nearlist(n, ab)
bfs(near)
print(*ans, sep='\n')
