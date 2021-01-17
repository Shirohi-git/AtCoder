h, w, k = map(int, input().split())
xyc = [input().split() for _ in range(k)]
MOD9 = 998244353
INV = 2 * pow(3, MOD9 - 2, MOD9) % MOD9

vec = [''] * (h * w)
for x, y, c in xyc:
    vec[(int(x) - 1) * w + (int(y) - 1)] = c

dp = [0] * (h * w + w)
dp[0] = 1
for i in range(h):
    for j in range(w):
        now = i * w + j
        tmp = dp[now] % MOD9
        if vec[now] == 'R':
            dp[now + 1] += tmp * (j + 1 < w)
        elif vec[now] == 'D':
            dp[now + w] += tmp * (i + 1 < h)
        elif vec[now] == 'X':
            dp[now + 1] += tmp * (j + 1 < w)
            dp[now + w] += tmp * (i + 1 < h)
        else:
            dp[now + 1] += tmp * (j + 1 < w) * INV
            dp[now + w] += tmp * (i + 1 < h) * INV
print(dp[h * w - 1] * pow(3, h * w - k, MOD9) % MOD9)
