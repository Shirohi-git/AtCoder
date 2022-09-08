def main():
    def nearlist(n0, lst):
        res = [[] for _ in range(n0)]
        for a, b in lst:
            res[a - 1].append(b - 1)
            res[b - 1].append(a - 1)
        return res

    def bfs(s0, n0):
        dist = [-1] * n0
        dist[s0] = 0
        que = [s0]

        for q in que:
            for i in near[q]:
                if dist[i] > -1:
                    continue
                dist[i] = dist[q] + 1
                que.append(i)
            res = q
        return res, dist[res]

    near = nearlist(N, AB)
    dp = [0] * N
    dp[0:2] = [1, 0]
    for i in range(2, N):
        dp[i] = (0 in dp[i-2:i])
    _, l = bfs(bfs(0, N)[0], N)
    return print('First' if dp[l] else 'Second')


if __name__ == '__main__':
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]

    main()
