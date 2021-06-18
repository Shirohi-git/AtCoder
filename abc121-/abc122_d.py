def main():
    dp = [0] * 256
    dp[255] = 1
    for _ in range(N):
        bfodp, dp = [dpi % MOD1 for dpi in dp], [0] * 256
        for bfo in range(256):
            for add in ADD:
                nxt = (bfo >> 2) + add
                res = (nxt >> 2 in NG) | (nxt & 63 in NG)
                res |= (nxt | 12 == 108) | (nxt | 48 == 120)
                dp[nxt] += bfodp[bfo] * (1 - res)
    return print(sum(dp) % MOD1)


if __name__ == '__main__':
    N = int(input())
    MOD1 = 10**9 + 7
    NG, ADD = [18, 24, 36], [0, 64, 128, 192]

    main()
