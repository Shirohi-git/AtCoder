from copy import deepcopy


def warshallfloyd(N, LIST):
    res = 0
    DIST = deepcopy(LIST)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                DIST[i][j] = min(DIST[i][j], DIST[i][k] + DIST[k][j])
                res += (DIST[i][j] if DIST[i][j]<INF else 0)
    return res


def main():
    near = [[INF] * N for _ in range(N)]
    for i in range(N):
        near[i][i] = 0
    for a, b, c in ABC:
        near[a-1][b-1] = c

    ans = warshallfloyd(N, near)
    return print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(M)]
    INF = 10**10

    main()
