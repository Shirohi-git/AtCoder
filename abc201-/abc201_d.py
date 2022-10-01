def main():
    a = [[[-1, 1][aij == '+'] for aij in ai] for ai in A]
    bfo = [-INF] * W
    bfo[-1] = 0
    for i in range(H)[::-1]:
        for j in range(W-1)[::-1]:
            bfo[j] = max(bfo[j], -bfo[j+1] + a[i][j+1])
        dp = bfo
        bfo = [-dp[j] + a[i][j] for j in range(W)]

    last = (H*W) % 2 * 2 - 1
    res = (last * dp[0] >= 0) + (last * dp[0] > 0)
    ans = ["Aoki", "Draw", "Takahashi"]
    return print(ans[::last][res])


if __name__ == '__main__':
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    INF = 10**5

    main()
