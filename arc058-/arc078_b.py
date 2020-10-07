from collections import deque


def nearlist(N, LIST):
    NEAR = [set() for _ in range(N)]
    for a, b in LIST:
        NEAR[a - 1].add(b - 1)
        NEAR[b - 1].add(a - 1)
    return NEAR


def bfs(S):
    dist, flag = [-1] * n, [0] * n
    dist[S], flag[S] = 0, 1
    que = deque([S])

    while que:
        q = que.popleft()
        for i in near[q]:
            if flag[i]:
                continue
            dist[i] = dist[q] + 1
            flag[i] = 1
            que.append(i)
    return dist


n = int(input())
ab = [list(map(int, input().split())) for _ in range(n - 1)]

near = nearlist(n, ab)
fennec, snuke = bfs(0), bfs(n - 1)
ans = sum(fennec[i] <= snuke[i] for i in range(n))
print('Fennec' if ans * 2 > n else 'Snuke')
