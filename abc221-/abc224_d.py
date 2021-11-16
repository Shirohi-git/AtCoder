def bfs(s0, g):
    from collections import defaultdict

    def nearlist():
        res = [[] for _ in range(N)]
        for a, b in UV:
            res[a - 1].append(b - 1)
            res[b - 1].append(a - 1)
        return res

    def swaplst(bfo):
        res = []
        idx = bfo.index('0')
        for i in near[idx]:
            nxt = bfo[::]
            nxt[i], nxt[idx] = nxt[idx], nxt[i]
            res.append(''.join(nxt))
        return res

    near = nearlist()
    dist = defaultdict(lambda: -1)
    dist[s0] = 0
    que = [s0]

    for q in que:
        for i in swaplst(list(q)):
            if dist[i] != -1:
                continue
            dist[i] = dist[q] + 1
            que.append(i)
            if i == g:
                return dist[g]
    return dist[g]


def main():
    goal = ['0'] * N
    for i, pi in enumerate(P, 1):
        goal[pi-1] = str(i)
    start = "123456780"
    goal = ''.join(goal)
    ans = bfs(start, goal)
    return print(ans)


if __name__ == '__main__':
    N, M = 9, int(input())
    UV = [list(map(int, input().split())) for _ in range(M)]
    P = list(map(int, input().split()))

    main()
