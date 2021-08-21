def main():
    pow2 = 2**10
    last = [[0] * pow2 for _ in range(10)]
    cnt = [0] * pow2
    cnt[0] = 1

    ans = 0
    for si in S:
        idx = ord(si) - ord_a
        dp = [0] * pow2
        for bit in range(pow2):
            now = bit | (1 << idx)
            if (bit >> idx) & 1:
                dp[now] += last[idx][bit]
            else:
                dp[now] += cnt[bit]

        ans += sum(dp) % MOD9
        for bit in range(pow2):
            if (bit >> idx) & 1:
                last[idx][bit] += dp[bit] % MOD9
            cnt[bit] += dp[bit] % MOD9

    return print(ans % MOD9)


if __name__ == '__main__':
    N, S = int(input()), input()
    MOD9 = 998244353
    ord_a = ord('A')

    main()
