from collections import deque


def nearlist(N):
    NEAR = [set() for _ in range(N)]
    for a, b in ab:
        NEAR[a - 1].add(b - 1)
        NEAR[b - 1].add(a - 1)
    return NEAR


def bfs(S, N):
    flag = [0] * N
    for v in (near[S] | {S}):
        flag[v] = 1
    que = deque(near[S])

    res = k * (k - 1) * kperm[len(near[S]) - 1] % MOD
    while que:
        q = que.popleft()
        for i in near[q]:
            if flag[i]:
                continue
            flag[i] = 1
            que.append(i)

        res = res * kperm[len(near[q]) - 1] % MOD
    return res


n, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n - 1)]
MOD = 10 ** 9 + 7

kperm = [1] + [0] * n
for i in range(min(k - 2, n)):
    kperm[i + 1] = (kperm[i] * (k - 2 - i) % MOD)

near = nearlist(n)
print(k if n == 1 else bfs(0, n))
