def main():
    dp = [1] + [0] * (10**4 + 100)
    for a, b in AB:
        nxt = [0] * (10**4 + 101)
        for x, di in enumerate(dp):
            if di:
                nxt[x+a] = nxt[x+b] = 1
        dp = nxt[:]
    return print('Yes' if dp[X] else 'No')


if __name__ == '__main__':
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    main()
