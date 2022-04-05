def main():

    def binary(ok, ng):

        def knapsack(w0, idx):
            sup = max(0, w0 - A[idx])
            if sup <= 0 < w0:
                return True

            dp = [0] * w0
            dp[0] = 1
            for ai in A[:idx] + A[idx+1:]:
                for nxt in range(w0)[::-1]:
                    if nxt - ai >= 0 and dp[nxt - ai]:
                        dp[nxt] |= 1
                        if sup <= nxt:
                            return True
            return False

        while abs(ng - ok) > 1:
            mid = (ok + ng) // 2
            if knapsack(K, mid):
                ok = mid
            else:
                ng = mid
        return ok

    ans = binary(N, -1)
    return print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = sorted(map(int, input().split()))

    main()
