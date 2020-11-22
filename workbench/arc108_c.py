from collections import deque


def nearlist(N):
    NEAR = [set() for _ in range(N)]
    for a,b,c in uvc:
        NEAR[a - 1].add((b - 1, c))
        NEAR[b - 1].add((a - 1, c))
    return NEAR


def bfs(S, N):
    num = [-1] * N
    num[S] = 1
    que = deque([S])

    while que:
        q = que.popleft()
        for i, ci in near[q]:
            if num[i] > 0:
                continue
            num[i] = 1 + (ci == 1)
            num[i] += (ci - num[i]) * (num[q] != ci)
            que.append(i)
    return num


n, m = map(int, input().split())
uvc = [list(map(int, input().split())) for _ in range(m)]

near = nearlist(n)
print(*bfs(0, n), sep='\n')
