from collections import defaultdict


def main():
    def nearlist(n0):
        res = [[] for _ in range(n0)]
        for i, (a, b) in enumerate(UV):
            res[a - 1].append((b - 1, i))
            res[b - 1].append((a - 1, i))
        return res

    def bfs(s0, g0):
        bfo = [-1] * N
        bfo[s0] = 's'

        que = [s0]
        for q in que:
            for p, e_idx in near[q]:
                if bfo[p] != -1:
                    continue
                bfo[p] = (q, e_idx)
                que.append(p)
            if bfo[g0] != -1:
                break

        now = g0
        while now != s0:
            now, e_idx = bfo[now]
            cnt[e_idx] += 1
        return

    near = nearlist(N)
    cnt = [0] * (N-1)
    for s, t in zip(A, A[1:]):
        bfs(s-1, t-1)

    dp = {0: 1}
    for ci in cnt:
        nxt = defaultdict(lambda:0)
        for k, v in dp.items():
            nxt[k-ci] += v
            nxt[k+ci] += v
        dp = {k: v % MOD9 for k, v in nxt.items()}
    return print(dp[K] if K in dp else 0)


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    UV = [list(map(int, input().split())) for _ in range(N-1)]
    MOD9 = 998244353

    main()
