from collections import defaultdict


def count_half(g):
    dp = defaultdict(lambda: defaultdict(lambda: 0))
    dp[0, 0][g[0][0]] = 1
    for i, gi in enumerate(g):
        for j, gij in enumerate(gi[:N-i]):
            now = dp[i, j]
            bfo = [*dp[i-1, j].items()] + [*dp[i, j-1].items()]
            for k, v in bfo:
                now[k ^ gij] += v
    res = [dp[i, N-1-i] for i in range(N)]
    return res


def main():
    fst = count_half(A)[::-1]
    snd = count_half([ai[::-1] for ai in A[::-1]])
    ans = 0
    for i in range(N):
        ai = A[N-1-i][i]
        for num, c in fst[i].items():
            ans += c * snd[i][num ^ ai]
    return print(ans)


if __name__ == '__main__':
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    main()
