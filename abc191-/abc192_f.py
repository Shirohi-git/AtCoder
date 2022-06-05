def sub_dp(cnt):
    dp = [[-INF] * cnt for _ in range(cnt+1)]
    dp[0][0] = 0
    for ai in A:
        for j in range(cnt)[::-1]:
            nxt = dp[j+1]
            for bfo in dp[j]:
                nxtsum = bfo + ai
                if 0 < nxtsum <= X:
                    mod = nxtsum % cnt
                    nxt[mod] = max(nxt[mod], nxtsum)

    if dp[cnt][X % cnt] < 0:
        return X
    return (X - dp[cnt][X % cnt]) // cnt


def main():
    ans = X
    for c in range(N):
        ans = min(sub_dp(c+1), ans)
    return print(ans)


if __name__ == '__main__':
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    INF = 10**18

    main()