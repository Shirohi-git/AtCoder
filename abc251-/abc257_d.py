def warshallfloyd(n0, lst0):
    res = [li[:] for li in lst0]
    for k in range(n0):
        for i in range(n0):
            for j in range(n0):
                res[i][j] = min(res[i][j], max(res[i][k], res[k][j]))
    return res



def main():
    dist = [[0] * N for _ in range(N)]
    for i, (xi, yi, pi) in enumerate(XYP):
        for j, (xj, yj, pj) in enumerate(XYP):
            dist[i][j] = INF * (abs(xi-xj) + abs(yi-yj)) // pi
            dist[j][i] = INF * (abs(xi-xj) + abs(yi-yj)) // pj
    
    msp = warshallfloyd(N, dist)
    ans = min(max(mi) for mi in msp)
    return print((ans+INF-1)//INF)


if __name__ == '__main__':
    N = int(input())
    XYP = [list(map(int, input().split())) for _ in range(N)]
    INF = 10**18

    main()
