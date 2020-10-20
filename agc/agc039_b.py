def is_bipartite(S, N):
    color = [0 for i in range(n)]
    stack = [(S, 1)]
    while stack:
        q, c = stack.pop()
        for i, sqi in enumerate(s[q]):
            if sqi and color[i] == c:
                return False
            if sqi and color[i] == 0:
                color[i] = -c
                stack.append((i, -c))
    return True


def warshallfloyd(N):
    from copy import deepcopy
    DIST = deepcopy(s)
    for i in range(N):
        for j in range(N):
            if DIST[i][j] == 0 and i != j:
                DIST[i][j] = N

    for k in range(N):
        for i in range(N):
            for j in range(N):
                DIST[i][j] = min(DIST[i][j],
                                 DIST[i][k] + DIST[k][j])
    return DIST


n = int(input())
s = [list(map(int, input())) for _ in range(n)]

dist = warshallfloyd(n)
ans = max(max(di) for di in dist)
print(ans + 1 if is_bipartite(0, n) else - 1)
