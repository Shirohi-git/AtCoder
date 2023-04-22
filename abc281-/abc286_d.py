def main():
    dp = [0] * (X+1)
    dp[0] = 1
    for ai, bi in AB:
        for c in range(bi):
            for x in range(X, 0, -1):
                if x-ai >= 0 and dp[x-ai]:
                    dp[x] = 1
    return print("Yes" if dp[-1] else "No")


if __name__ == '__main__':
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    main()
