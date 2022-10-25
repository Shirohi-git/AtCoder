def main():
    def dist(a, b):
        (x, y), (p, q) = XYPQ[a], XYPQ[b]
        return ((x-p)**2 + (y-q)**2)**0.5

    nm = N + M
    near = [[0] * nm for _ in range(nm)]
    for i in range(nm):
        near[i][i] = dist(i, -1)
        for j in range(i):
            near[i][j] = near[j][i] = dist(i, j)

    popcount = [0]
    for _ in range(M):
        popcount += [i + 1 for i in popcount]

    dist = [[INF] * nm for _ in range(1 << nm)]
    # この下2行が高速化されている
    # 1つ目の訪問地の距離を最初に記録することで頂点数が1小さくなる
    for i in range(nm):
        dist[1 << i][i] = near[i][i]

    for bit in range(1 << nm):
        boost = 1 << popcount[bit >> N]
        for q in range(nm):
            if (bit >> q) & 1 == 0:
                continue
            for i in range(nm):
                if (bit >> i) & 1:
                    continue
                nxt = bit | (1 << i)
                d_nqi = dist[bit][q] + near[q][i] / boost
                dist[nxt][i] = min(dist[nxt][i], d_nqi)

    ans = INF
    for bit in range(1 << M):
        boost = 1 << popcount[bit]
        bit = (bit << N) | ((1 << N)-1)
        for i, d in enumerate(dist[bit]):
            ans = min(ans, d + near[i][i] / boost)
    return print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    XYPQ = [list(map(int, input().split())) for _ in range(N)]
    XYPQ += [list(map(int, input().split())) for _ in range(M)] + [[0, 0]]
    INF = 10 ** 18

    main()
