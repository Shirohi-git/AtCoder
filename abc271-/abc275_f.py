def main():
    dp0 = [INF] + [INF] * M
    dp1 = [0] + [INF] * M
    for ai in A:
        nxt = [INF] + [INF] * M
        for j in range(ai, M+1):
            nxt[j] = min(dp0[j-ai], dp1[j-ai])
        dp0 = [min(x, y+1) for x, y in zip(dp0, dp1)]
        dp1 = nxt
    ans = [(di if di < INF else -1) for di in map(min, dp0, dp1)]
    return print(*ans[1:], sep='\n')


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    INF = 10**10

    main()
