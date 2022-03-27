def tsp_hamilton(n0, lst0, inf=10**10, tsp=True):
    dist = [[inf] * n0 for _ in range(2**n0)]
    dist[1 << 0][0] = 0
    que = [(1 << 0, 0)]
    if not tsp:
        for i in range(n0):
            dist[1 << i][i] = 0
        que = [(1 << i, i) for i in range(n0)]

    for bit, q in que:
        for i in range(n0):
            if (bit >> i) & 1:
                continue
            nxt = bit | (1 << i)
            if lst0[q][i] > 0:
                d_nqi = dist[bit][q] + lst0[q][i]
                if dist[nxt][i] == inf:
                    dist[nxt][i] = d_nqi
                    que.append((nxt, i))
                dist[nxt][i] = min(dist[nxt][i], d_nqi)
    if tsp:
        goal = [inf] * n0
        for i, d in enumerate(dist[-1]):
            goal[i] = d + lst0[i][0]
        dist.append(goal)
    return min(dist[-1])


def main():

    def calc_dist(x, y):
        (a, b, c), (p, q, r) = XYZ[x], XYZ[y]
        return abs(p - a) + abs(b - q) + max(0, r - c)

    near = [[-1] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            near[x][y] = calc_dist(x, y)
    ans = tsp_hamilton(N, near)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    XYZ = [list(map(int, input().split())) for _ in range(N)]

    main()
