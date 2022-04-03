def str_bit(s):
    res = 0
    for si in s:
        res |= 1 << (ord(si) - ord('a'))
    return res


def main():
    def bitcount(n0):
        bitcnt = [0]
        for _ in range(n0):
            bitcnt += [i + 1 for i in bitcnt]
        return bitcnt

    ans = 0
    cnt = bitcount(N)
    for bit in range(1, 1 << N):
        str = (1 << 26) - 1
        for i in range(N):
            if (bit >> i) & 1:
                str &= S[i]
        ans += pow(bin(str).count('1'), L, MOD9) * (cnt[bit] % 2 * 2 - 1)
    return print(ans % MOD9)


if __name__ == '__main__':
    N, L = map(int, input().split())
    S = [str_bit(input()) for _ in range(N)]
    MOD9 = 998244353

    main()
