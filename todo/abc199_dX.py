def nearlist(N):
    NEAR = [set() for _ in range(N)]
    for a, b in ab:
        NEAR[a - 1].add(b - 1)
        NEAR[b - 1].add(a - 1)
    return NEAR


n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

ab = nearlist(n)
