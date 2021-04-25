n = int(input())
s, x = input(), input()

dp = [[0] * 7 for i in range(n+1)]
dp[0][0] = 1
for i, si, xi in zip(range(n), s[::-1], x[::-1]):
    for mod in range(7):
        num1, num2 = 10*mod % 7, (10*mod + int(si)) % 7
        if xi == "T":
            dp[i+1][mod] = dp[i][num1] | dp[i][num2]
        if xi == "A":
            dp[i+1][mod] = dp[i][num1] & dp[i][num2]
print("Takahashi" if dp[-1][0] else "Aoki")
