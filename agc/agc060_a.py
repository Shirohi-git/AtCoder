def main():

    def loop(l=0, r=K):
        nxt = [[0] * K for _ in range(K)]
        for ti in range(l, r):
            for p in range(K):
                if ti == p:
                    continue
                for q in range(K):
                    if ti == q:
                        continue
                    nxt[ti][p] += dp[p][q]
                    nxt[ti][p] %= MOD9
        return nxt

    # dp[i][x][y] = i-1文字目y i文字目x
    s = [ord(si) - ord_a for si in S]
    dp = [[0] * K for _ in range(K)]
    for p in range(K):
        for q in range(K):
            if p != q and s[1] in [sq, p] and s[0] in [sq, q]:
                dp[p][q] = 1

    for si in s[2:]:
        if si == sq:
            dp = loop()
        else:
            dp = loop(si, si+1)

    ans = 0
    if s[-1] == sq:
        ans = sum(sum(di) % MOD9 for di in dp)
    else:
        ans = sum(dp[s[-1]])
    return print(ans % MOD9)


if __name__ == '__main__':
    N = int(input())
    S = input()

    MOD9 = 998244353
    K = 26
    ord_a = ord('a')
    sq = ord('?') - ord_a

    main()
