def main():
    ans = 0
    for div in range(1, DIV+1):
        dp = [[0] * div for _ in range(div+1)]
        dp[0][0] = 1
        for ai in A:
            for j in range(div)[::-1]:
                for bfo in range(div):
                    nxt = (bfo + ai) % div
                    dp[j+1][nxt] += dp[j][bfo]
        ans = (ans + dp[div][0]) % MOD9
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    DIV = 100
    MOD9 = 998244353

    main()
