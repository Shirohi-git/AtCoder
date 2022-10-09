def LIS(lst0):
    from bisect import bisect_left
    dp = []
    for ai in lst0:
        idx = bisect_left(dp, ai)
        if len(dp) <= idx:
            dp.append(ai)
        dp[idx] = ai
    return len(dp)


def main():
    ab = sorted([*zip(A, B)])
    ans = N + LIS([bi for _, bi in ab])
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    main()
