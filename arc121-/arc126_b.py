def main():
    def LIS(L):
        from bisect import bisect_left

        dp = []
        for ai in L:
            idx = bisect_left(dp, ai)
            if len(dp) <= idx:
                dp.append(ai)
            dp[idx] = ai
        return len(dp)

    ab_sort = sorted((ai, -bi) for ai, bi in AB)
    b = [-bi for _, bi in ab_sort]
    ans = LIS(b)
    return print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]

    main()
