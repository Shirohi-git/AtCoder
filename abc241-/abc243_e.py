def warshallfloyd(n0, lst0):
    res = [li[:] for li in lst0]
    for k in range(n0):
        for i in range(n0):
            for j in range(n0):
                res[i][j] = min(res[i][j], res[i][k] + res[k][j])
    return res


def main():
    dist = [[INF] * N for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0
    for ai, bi, ci in ABC:
        dist[ai-1][bi-1] = ci * N - 1
        dist[bi-1][ai-1] = ci * N - 1

    ans = 0
    dist = warshallfloyd(N, dist)
    for ai, bi, ci in ABC:
        if dist[ai-1][bi-1] < ci * N - 1:
            ans += 1
    return print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(M)]
    INF = 10**18

    main()
