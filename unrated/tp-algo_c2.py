def TSP(n0, lst0, inf=10**10):
    n1 = n0-1
    dist = [[inf] * n1 for _ in range(1 << n1)]
    for i in range(n1):
        dist[1 << i][i] = lst0[-1][i]

    for bit in range(1 << n1):
        for q in range(n1):
            if ((bit >> q) & 1) == 0:
                continue
            for i in range(n1):
                if (bit >> i) & 1:
                    continue
                nxt = bit | (1 << i)
                if lst0[q][i] >= 0:
                    d_nqi = dist[bit][q] + lst0[q][i]
                    dist[nxt][i] = min(dist[nxt][i], d_nqi)

    goal = [inf] * n0
    for i, d in enumerate(dist[-1]):
        goal[i] = d + lst0[i][-1]
    return min(goal)


def main():
    ans = TSP(N, A)
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = [[*map(int, input().split())] for _ in range(N)]

    main()
