from bisect import bisect_left


def main():

    def LIS():
        dp = []
        for qi in Q:
            for qij in idx_lst[qi][::-1]:
                idx = bisect_left(dp, qij)
                if len(dp) <= idx:
                    dp.append(qij)
                dp[idx] = qij
        return len(dp)

    idx_lst = [[] for _ in range(N+1)]
    for i, pi in enumerate(P):
        for num in range(pi, N+1, pi):
            idx_lst[num].append(i)
    return print(LIS())


if __name__ == '__main__':
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    main()
