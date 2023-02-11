def main():
    def zipidx(i, j):
        return N*i + j

    def nearlist(n0, lst0):
        res = [[] for _ in range(n0)]
        for a, b in lst0:
            res[a-1].append(b-1)
            res[b-1].append(a-1)
        return res

    near = nearlist(N, UV)
    s, g = zipidx(0, N-1), zipidx(N-1, 0)
    dist = [-1] * (N**2)
    dist[s] = 0
    que = [(0, N-1)]

    for x, y in que:
        bfo = dist[zipidx(x, y)]
        for nx in near[x]:
            for ny in near[y]:
                nxt = zipidx(nx, ny)
                if dist[nxt] == -1 and C[nx] != C[ny]:
                    dist[nxt] = bfo + 1
                    que.append((nx, ny))
    return dist[g]


if __name__ == '__main__':
    T = int(input())
    ans = []
    for _ in range(T):
        N, M = map(int, input().split())
        C = list(map(int, input().split()))
        UV = [list(map(int, input().split())) for _ in range(M)]
        ans.append(main())
    print(*ans, sep='\n')
