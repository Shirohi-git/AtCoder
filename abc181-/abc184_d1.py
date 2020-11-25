a, b, c = map(int, input().split())
plus = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

dp = [0] * (101 ** 3)
for num in range(101 ** 3)[::-1]:
    i, j, k = num // 10201, num // 101 % 101, num % 101
    if i > 99 or j > 99 or k > 99:
        continue
    for cnt, (p, q, r) in zip((i, j, k), plus):
        if cnt > 0:
            nxt = (i + p) * 10201 + (j + q) * 101 + (k + r)
            dp[num] += cnt * dp[nxt] + cnt
    if num > 0:
        dp[num] /= i + j + k
ans = a * 10201 + b * 101 + c
print(dp[ans])
