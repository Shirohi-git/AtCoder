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
    for c, d in CD:
        res = (dist[c-1]-dist[d-1])%2
        print('Road' if res else 'Town')


if __name__ == '__main__':
    N, Q = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    CD = [list(map(int, input().split())) for _ in range(Q)]

    main()
