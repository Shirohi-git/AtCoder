def main():
    dp_p, dp_m = [0] * N, [0] * N
    dp_p[0], dp_m[0] = (A[0], 1), (0, 0)
    for i, ai in enumerate(A[1:], 1):
        p1, p2 = dp_p[i-1]
        m1, m2 = dp_m[i-1]
        dp_m[i] = ((p1 - ai*p2) % MOD1, p2)
        dp_p[i] = ((p1 + ai*p2 + m1 + ai*m2) % MOD1, (p2+m2) % MOD1)
    return print((dp_m[-1][0] + dp_p[-1][0]) % MOD1)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    MOD1 = 10**9 + 7

    main()
