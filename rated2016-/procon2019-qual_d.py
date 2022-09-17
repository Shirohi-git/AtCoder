def main():
    def cost(stt, ai):
        if stt in [0, 4]:
            return ai
        elif stt in [1, 3]:
            return (ai % 2 if ai > 0 else 2)
        else:  # elif stt == 2:
            return 1 - ai % 2

    dp = [[INF] * 5 for _ in range(L+1)]
    dp[0] = [0] * 5
    for i, ai in enumerate(A, 1):
        for p in range(5):
            for q in range(p+1):
                res = dp[i-1][q] + cost(p, ai)
                dp[i][p] = min(dp[i][p], res)
    return print(min(dp[-1]))


if __name__ == '__main__':
    L = int(input())
    A = [int(input()) for _ in range(L)]
    INF = 10**15

    main()
