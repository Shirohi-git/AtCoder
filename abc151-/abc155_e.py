n = map(int, list(input()))

dp0, dp1 = 0, 1
for num in n:
    tmp0, tmp1 = dp0 + num, dp1 + (10 - num)
    dp0 = min(tmp0, tmp1)
    dp1 = min(tmp0 + 1, tmp1 - 1)
print(dp0)
