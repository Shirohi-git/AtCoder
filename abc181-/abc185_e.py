def levenshtein(S, T):
    ls, lt = len(S), len(T)
    dp = [[0] * (lt + 1) for _ in range(ls + 1)]
    for i in range(ls + 1):
        dp[i][0] = i
    for j in range(lt + 1):
        dp[0][j] = j

    for i in range(1, ls + 1):
        for j in range(1, lt + 1):
            cost = (S[i - 1] != T[j - 1])
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1,
                           dp[i - 1][j - 1] + cost)
    return dp[ls][lt]

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(levenshtein(a, b))
