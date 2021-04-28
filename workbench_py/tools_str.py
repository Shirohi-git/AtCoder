def Z_algo(S):  # 最長共通接頭辞 S:文字列
    bfo, N = 0, len(S)
    z = [0] * N
    for i in range(1, N):
        l = i - bfo
        if i + z[l] < bfo + z[bfo]:
            z[i] = z[l]
        else:
            j = max(0, bfo + z[bfo] - i)
            while i + j < N and S[j] == S[i + j]:
                j += 1
            z[i], bfo = j, i
    z[0] = N
    return z


def lcs(S, T):  # 最長共通部分列  # S,T:文字列
    ls, lt = len(S), len(T)
    dp = [[0] * (lt + 1) for _ in range(ls + 1)]
    dp[0][0], dp[1][0], dp[0][1] = 0, 0, 0
    for i in range(ls):
        for j in range(lt):
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
            if S[i] == T[j]:
                dp[i + 1][j + 1] = max(dp[i][j] + 1, dp[i + 1][j + 1])
    return dp[ls][lt]


def levenshtein(S, T):  # レーベンシュタイン距離  # S,T:文字列
    ls, lt = len(S), len(T)
    dp = [[0] * (lt + 1) for _ in range(ls + 1)]
    for i in range(ls + 1):
        dp[i][0] = i
    for j in range(lt + 1):
        dp[0][j] = j

    for i in range(1, ls + 1):
        for j in range(1, lt + 1):
            cost = 0 if S[i - 1] == T[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,         # insertion
                           dp[i][j - 1] + 1,         # deletion
                           dp[i - 1][j - 1] + cost)  # replacement
    return dp[ls][lt]
