def TSP_hamilton(n0, lst0, inf=10**18):
    popcount = [0]
    for _ in range(M):
        popcount += [i + 1 for i in popcount]
    popcount = [1 << pi for pi in popcount]

    dist = [[inf] * n0 for _ in range(2**n0)]
    dist[1 << 0][0] = 0
    que = [(1 << 0, 0)]
    for bit, q in que:
        boost = popcount[bit >> N+1]
        for i in range(n0):
            if (bit >> i) & 1:
                continue
            nxt = bit | (1 << i)
            if lst0[q][i] > 0:
                d_nqi = dist[bit][q] + lst0[q][i] / boost
                if dist[nxt][i] == inf:
                    dist[nxt][i] = d_nqi
                    que.append((nxt, i))
                dist[nxt][i] = min(dist[nxt][i], d_nqi)

    goal = [inf]
    for bit in range(2**M):
        boost = popcount[bit]
        bit = (bit << N+1) | ((1 << N+1)-1)
        for i, d in enumerate(dist[bit]):
            goal.append(d + lst0[i][0] / boost)
    return min(goal)


def main():
    def dist(a, b):
        (x, y), (p, q) = XYPQ[a], XYPQ[b]
        return ((x-p)**2 + (y-q)**2)**0.5

    near = [[0] * (N+M+1) for _ in range(N+M+1)]
    for i in range(N+M+1):
        for j in range(i):
            near[i][j] = near[j][i] = dist(i, j)
    ans = TSP_hamilton(N+M+1, near)
    return print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    XYPQ = [(0, 0)] + [list(map(int, input().split())) for _ in range(N)]
    XYPQ += [list(map(int, input().split())) for _ in range(M)]

    main()
