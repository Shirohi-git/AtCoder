h, w, k = map(int, input().split())
xyc = [input().split() for _ in range(k)]
MOD9 = 998244353
INV = 2 * pow(3, MOD9 - 2, MOD9) % MOD9
dic = {'X': 1, 'R': 2, 'D': 3}

v = [0] * (h * w)
for x, y, c in xyc:
    v[(int(x) - 1) * w + (int(y) - 1)] = dic[c]

dp = [0] * (h * w + w)
dp[0] = 1
for now in range(h * w):
    vec, com = v[now], dp[now] % MOD9
    tmpr = com * (now % w + 1 < w and vec != 3)
    tmpd = com * (now // w + 1 < h and vec != 2)
    dp[now + 1] += tmpr * pow(INV, (vec == 0))
    dp[now + w] += tmpd * pow(INV, (vec == 0))
print(dp[h * w - 1] * pow(3, h * w - k, MOD9) % MOD9)
