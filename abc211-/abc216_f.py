def main():
    ans = 0
    cnt = [1] + [0] * MAXN
    for ai, bi in sorted(zip(A, B)):
        for s in range(bi, MAXN)[::-1]:
            if s <= ai:
                ans += cnt[s-bi]
            cnt[s] = (cnt[s] + cnt[s-bi]) % MOD9
        ans %= MOD9
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD9 = 998244353
    MAXN = 5001

    main()
