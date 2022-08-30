def main():
    a, aq, c, cq = 0, 0, *map(S.count, 'C?')
    pow3 = [pow(3, i, MOD1) for i in range(cq+1)]

    ans = 0
    for si in S:
        c, cq = c - (si == 'C'), cq - (si == '?')
        if si in 'B?':
            res_a = a*pow3[aq] + aq*pow3[aq-1]
            res_c = c*pow3[cq] + cq*pow3[cq-1]
            ans += res_a % MOD1 * res_c % MOD1
        a, aq = a + (si == 'A'), aq + (si == '?')
    return print(ans % MOD1)


if __name__ == '__main__':
    S = input()
    MOD1 = 10**9 + 7

    main()
