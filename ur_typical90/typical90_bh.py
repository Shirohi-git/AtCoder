from bisect import bisect_left


def LIS(L):
    res = []
    dp = []
    for ai in L:
        idx = bisect_left(dp, ai)
        if len(dp) <= idx:
            dp.append(ai)
        dp[idx] = ai
        res.append(len(dp))
    return res


def main():
    front, back = LIS(A), LIS(A[::-1])[::-1]
    ans = max(front[i] + back[i] - 1 for i in range(N))
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    main()
