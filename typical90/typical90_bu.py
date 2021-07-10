def bfs(s0, n0, near0):
    pre = [-1] * n0
    pre[s0] = n0

    que = [s0]
    for q in que:
        for i in near0[q]:
            if pre[i] < 0:
                pre[i] = q
                que.append(i)
    return que[::-1], pre


def main():
    def nearlist(n0):
        res = [[] for _ in range(n0)]
        for a, b in AB:
            res[a - 1].append(b - 1)
            res[b - 1].append(a - 1)
        return res

    near = nearlist(N)
    lst, pred = bfs(0, N, near)

    ID_ab = 2
    dp = [[0] * 3 for _ in range(N)]
    for q in lst:
        c_q, cnt1, cnt2 = C[q], 1, 1
        for i in near[q]:
            if i == pred[q]:
                continue
            cnt1 = cnt1 * (dp[i][c_q] + dp[i][ID_ab]) % MOD1
            cnt2 = cnt2 * (sum(dp[i]) + dp[i][ID_ab]) % MOD1
        dp[q] = [(1-c_q) * cnt1, c_q * cnt1, cnt2 - cnt1]

    ans = dp[0][ID_ab] % MOD1
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    C = [(ci == 'b') for ci in input().split()]
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    MOD1 = 10**9 + 7

    main()
