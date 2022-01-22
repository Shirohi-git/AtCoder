def bellmanford(s0, n0, edge0, inf=10**18):
    res = [inf] * n0
    res[s0] = 0
    
    for i in range(n0 * 2):
        for a, b, d in edge0:
            d *= -1
            if res[a-1] + d < res[b-1]:
                res[b-1] = (res[a-1] + d if i < n0 else -inf)
    return res

def main():
    ans = bellmanford(0, N, ABC, INF)[-1] * -1
    return print("inf" if ans == INF else ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(M)]
    INF = 10**18

    main()