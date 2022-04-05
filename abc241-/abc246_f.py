def main():
    def bitcount(n0):
        bitcnt = [0]
        for _ in range(n0):
            bitcnt += [i + 1 for i in bitcnt]
        return bitcnt

    ans = 0
    pm = [-1, 1]
    cnt = bitcount(N)
    for bit in range(1, 1 << N):
        str = set(Alp)
        for i in range(N):
            if (bit >> i) & 1:
                str &= S[i]
        ans += pow(len(str), L, MOD9) * pm[cnt[bit] % 2]
    return print(ans % MOD9)


if __name__ == '__main__':
    N, L = map(int, input().split())
    S = [set(input()) for _ in range(N)]
    MOD9 = 998244353
    Alp = "abcdefghijklmnopqrstuvwxyz"

    main()
