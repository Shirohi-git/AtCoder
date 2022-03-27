def bfs(s0, n0, near0):
    dist = [-1] * n0
    dist[s0] = 0
    que = [s0]

    for q in que:
        for i in near0[q]:
            if dist[i] > 0:
                continue
            dist[i] = 1 + dist[q]
            que.append(i)
    return dist


def tsp_hamilton(n0, lst0, inf=10**10, tsp=True):
    dist = [[inf] * n0 for _ in range(2**n0)]
    dist[1 << 0][0] = 0
    que = [(1 << 0, 0)]
    if not tsp:
        for i in range(n0):
            dist[1 << i][i] = 0
        que = [(1 << i, i) for i in range(n0)]

    for bit, q in que:
        for i in range(n0):
            if (bit >> i) & 1:
                continue
            nxt = bit | (1 << i)
            if lst0[q][i] > 0:
                d_nqi = dist[bit][q] + lst0[q][i]
                if dist[nxt][i] == inf:
                    dist[nxt][i] = d_nqi
                    que.append((nxt, i))
                dist[nxt][i] = min(dist[nxt][i], d_nqi)

    if tsp:
        goal = [inf] * n0
        for i, d in enumerate(dist[-1]):
            goal[i] = d + lst0[i][0]
        dist.append(goal)
    res = min(dist[-1])
    return (res if res < inf else -1)


def main():
    def nearlist(N, LIST):
        res = [[] for _ in range(N)]
        for a, b in LIST:
            res[a - 1].append(b - 1)
            res[b - 1].append(a - 1)
        return res

    near = nearlist(N, AB)
    dist = []
    for ci in C:
        d = bfs(ci-1, N, near)
        dist.append([d[cj-1] for cj in C])
    ans = tsp_hamilton(K, dist, tsp=False)
    return print(ans+1 if ans > -1 else -1)


if __name__ == '__main__':
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    K = int(input())
    C = list(map(int, input().split()))

    main()
