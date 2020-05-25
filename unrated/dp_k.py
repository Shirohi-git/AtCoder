n, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [0] * (k + 1)  #-1=lose,1=win

for i in range(k + 1):
    list = [j for j in a if i >= j]
    if any(dp[i - j] == -1  for j in list):
        dp[i] = 1
    else:
        dp[i] = -1
print('First' if dp[k] == 1 else 'Second')