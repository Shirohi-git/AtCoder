n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
mod = 10 ** 9 + 7

dp = [0] * (1 << n)
dp[0] = 1

bitcount = [0]
for _ in range(n):
    bitcount += [i+1 for i in bitcount]

# 集めるDP
for bit in range(1,1 << n):
    i = bitcount[bit]
    for j in range(n):
        if ((bit >> j) & 1 == 1) and (a[i - 1][j] == 1):
            dp[bit] += dp[bit ^ (1 << j)]
    dp[bit] %= mod
print(dp[-1])
