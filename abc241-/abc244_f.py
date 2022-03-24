def bfs(s0, n0, near0):
    dist = [[INF] + [-1] * n0 for _ in range(2**n0)]
    dist[s0][0] = 0
    que = [(s0, 0)]
    for bit, q in que:
        for i in near0[q]:
            nxt = bit
            if i > 0:
                nxt = bit ^ (1 << (i-1))
            if dist[nxt][i] > -1:
                continue
            dist[nxt][i] = 1 + dist[bit][q]
            que.append((nxt, i))
    return dist


def main():
    def nearlist(N, LIST):
        res = [[] for _ in range(N+1)]
        for a, b in LIST:
            res[a].append(b)
            res[b].append(a)
        return res

    near = nearlist(N, UV + [(0, i+1) for i in range(N)])
    ans = bfs(0, N, near)
    return print(sum(min(ai) for ai in ans))


if __name__ == '__main__':
    N, M = map(int, input().split())
    UV = [list(map(int, input().split())) for _ in range(M)]
    INF = 10**9

    main()
