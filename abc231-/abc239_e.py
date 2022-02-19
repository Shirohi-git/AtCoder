def bfs(s0, n0, near0):
    dist = [-1] * n0
    dist[s0] = 0
    que = [s0]
    for q in que:
        for i in near0[q]:
            if dist[i] > -1:
                continue
            dist[i] = dist[q] + 1
            que.append(i)
    return dist


def main():
    def nearlist(n0):
        res = [[] for _ in range(n0)]
        for a, b in AB:
            res[a - 1].append(b - 1)
            res[b - 1].append(a - 1)
        return res

    near = nearlist(N)
    dist = bfs(0, N, near)

    big20 = [[X[q]] for q in range(N)]
    for q in sorted(range(N), key=lambda x: -dist[x]):
        for i in near[q]:
            if dist[i] > dist[q]:
                big20[q] += big20[i][:]
        big20[q] = sorted(big20[q])[::-1][:20]

    for v, k in VK:
        print(big20[v-1][k-1])
    return


if __name__ == '__main__':
    N, Q = map(int, input().split())
    X = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    VK = [list(map(int, input().split())) for _ in range(Q)]

    main()
