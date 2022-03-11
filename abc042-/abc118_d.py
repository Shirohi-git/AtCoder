def main():
    dp = [-1] * (N+10)
    dp[0] = 0
    for i in range(N):
        for ci in map(lambda x: CNT[x], A):
            dp[i+ci] = max(dp[i+ci], dp[i]+1)

    n = N
    ans = []
    for i in range(dp[N]):
        for ai in A:
            ci = CNT[ai]
            if ci <= n and dp[n-ci] == dp[n]-1:
                ans.append(ai)
                n -= ci
                break
    return print(*ans, sep='')


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = sorted(map(int, input().split()))[::-1]
    CNT = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]

    main()
