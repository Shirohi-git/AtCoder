from collections import defaultdict


def main():
    def bfs(s0, k0):
        dist = defaultdict(lambda: -1)
        dist[s0] = 0
        que = [s0]

        for q in que:
            if dist[q] < k0:
                for i in near[q]:
                    if dist[i] == -1:
                        dist[i] = dist[q] + 1
                        que.append(i)
        return sum(que) + len(que)

    def nearlist(n0):
        res = [[] for _ in range(n0)]
        for a, b in AB:
            res[a - 1].append(b - 1)
            res[b - 1].append(a - 1)
        return res

    near = nearlist(N)
    ans = (bfs(x-1, k) for x, k in XK)
    return print(*ans, sep='\n')


if __name__ == '__main__':
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    Q = int(input())
    XK = [list(map(int, input().split())) for _ in range(Q)]

    main()
