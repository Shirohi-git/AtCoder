def main():
    dp = [0, 0, 0, 0, 0]
    for i in range(1, max(TXA)[0]+1):
        dp = [max(dp[max(0, i-1):min(5, i+2)]) for i in range(5)]
        if i == TXA[-1][0]:
            ti, xi, ai = TXA.pop()
            if ti >= 5 or xi <= ti:
                dp[xi] += ai
    return print(max(dp))


if __name__ == '__main__':
    N = int(input())
    TXA = [list(map(int, input().split())) for _ in range(N)][::-1]

    main()
