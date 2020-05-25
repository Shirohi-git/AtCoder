s, t = str(input()), str(input())

ls, lt = len(s), len(t)
dp = [[0] * (lt + 1) for _ in range(ls + 1)]
dp[0][0], dp[1][0], dp[0][1] = 0, 0, 0
for i in range(ls):
    for j in range(lt):
        dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        if s[i] == t[j]:
            dp[i + 1][j + 1] = max(dp[i][j] + 1, dp[i + 1][j + 1])

ans = []
tmp_i, tmp_j = ls, lt
while tmp_i * tmp_j > 0:
    if dp[tmp_i][tmp_j] == dp[tmp_i - 1][tmp_j]:
        tmp_i -= 1
    elif dp[tmp_i][tmp_j] == dp[tmp_i][tmp_j - 1]:
        tmp_j -= 1
    else:
        tmp_i, tmp_j = tmp_i - 1, tmp_j - 1
        ans.append(s[tmp_i])
print(''.join(ans[::-1]))
