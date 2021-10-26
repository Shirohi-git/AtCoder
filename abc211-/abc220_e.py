def main():
    pow2 = [1]
    for _ in range(2 * N):
        pow2.append(pow2[-1] * 2 % MOD9)

    ans = 0
    for d1 in range(0, D+1):
        d2 = D - d1
        if not (0 <= d1 < N and 0 <= d2 < N):
            continue
        cnt = pow2[max(0, d1-1) + max(0, d2-1)]
        cnt *= pow2[N - max(d1, d2) + 1] - 2
        ans += cnt
    return print(ans % MOD9)


if __name__ == '__main__':
    N, D = map(int, input().split())
    MOD9 = 998244353

    main()
