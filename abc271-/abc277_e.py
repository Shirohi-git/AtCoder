def bfs(s0, n0, near0):
    dist = [[-1, -1] for _ in range(n0)]
    dist[s0][1] = 0
    que = [(s0, 1)]

    for q, now in que:
        bfo = dist[q][now]
        btn = (q+1 in S)
        for i, nxt in near0[q]:
            if dist[i][nxt] > -1:
                continue
            if not(btn or nxt == now):
                continue
            dist[i][nxt] = bfo + 1
            que.append((i, nxt))
    return sorted(dist[-1])


def main():
    def weighted_nearlist(n0, lst0):
        res = [set() for _ in range(n0)]
        for a, b, w in lst0:
            res[a-1].add((b-1, w))
            res[b-1].add((a-1, w))
        return res

    near = weighted_nearlist(N, UVA)
    a0, a1 = bfs(0, N, near)
    return print(a0 if a0 != -1 else a1)


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    UVA = [list(map(int, input().split())) for _ in range(M)]
    S = set(map(int, input().split()))

    main()
