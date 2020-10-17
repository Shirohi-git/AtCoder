def TSP_DP(s, bit, t):
    if bit == 0:
        memo[s * n + t][bit] = dist[s][t]
        return dist[s][t]

    d_min = float('inf')
    for i in range(n):
        if (bit >> i) & 1 == 0:
            continue
        x, nxt = i, bit ^ (1 << i)
        if memo[x * n + t][bit] == -1:
            memo[x * n + t][bit] = TSP_DP(x, nxt, t)
        d_tmp = dist[s][x] + memo[x * n + t][bit]
        d_min = min(d_min, d_tmp)
    return d_min


n = int(input())
xyz = [list(map(int, input().split())) for _ in range(n)]

dist = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        (a, b, c), (p, q, r) = xyz[i], xyz[j]
        dist[i][j] = abs(p - a) + abs(b - q) + max(0, r - c)
        dist[j][i] = abs(p - a) + abs(b - q) + max(0, c - r)

memo = [[-1] * (1 << n) for _ in range(n ** 2)]
print(TSP_DP(0, (1 << n) - 2, 0))
