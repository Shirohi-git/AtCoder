def idxzip(x, y): return N*x + y


def warshallfloyd(n0, c0, v0):
    c, v = c0[:], v0[:]
    for k in range(n0):
        for i in range(n0):
            ik = idxzip(i, k)
            for j in range(n0):
                ij, kj = idxzip(i, j), idxzip(k, j)
                if c[ij] > c[ik] + c[kj]:
                    c[ij] = c[ik] + c[kj]
                    v[ij] = v[ik] + v[kj]
                elif c[ij] == c[ik] + c[kj] and v[ij] > v[ik] + v[kj]:
                    v[ij] = v[ik] + v[kj]
    return c, v


def main():
    cost, val = [], []
    for ai, si in zip(A, S):
        for sij in si:
            e = (1 if sij=="Y" else INF)
            cost.append(e), val.append(-ai)

    cost, val = warshallfloyd(N, cost, val)
    for u, v in UV:
        uv = idxzip(u-1, v-1)
        if cost[uv] == INF:
            print("Impossible")
        else:
            print(cost[uv], A[v-1]-val[uv])
    return


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    S = [input() for _ in range(N)]
    Q = int(input())
    UV = [list(map(int, input().split())) for _ in range(Q)]
    INF = 500

    main()