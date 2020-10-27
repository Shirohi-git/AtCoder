def weighted_nearlist(N, LIST):
    NEAR = [set() for _ in range(N)]
    for a, b, d in LIST:
        NEAR[a - 1].add((b - 1, d))
        NEAR[b - 1].add((a - 1, -d))
    return NEAR


def dfs(S):
    dist[S] = 0
    stack = [S]

    while stack:
        q = stack.pop()
        for i, dqi in near[q]:
            if dist[i] == None:
                dist[i] = dist[q] + dqi
                stack.append(i)
            if dist[i] != dist[q] + dqi:
                return 0
    return 1


n, m = map(int, input().split())
lrd = [list(map(int, input().split())) for _ in range(m)]

near = weighted_nearlist(n, lrd)
ans, dist = 1, [None] * n
for i in range(n):
    if dist[i] == None :
        ans *= dfs(i)
print('Yes' if ans else 'No')
