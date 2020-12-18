n, m = map(int, input().split())
a = sorted(map(int, input().split()))[::-1] + [0]
b = sorted(map(int, input().split()))[::-1] + [0]
MOD = 10 ** 9 + 7

ans, grid = 1, 0
cnta, cntb = 0, 0
for i in range(n * m, 0, -1):
    ans *= (a[cnta] <= i and b[cntb] <= i)
    p, q = (a[cnta] == i), (b[cntb] == i)
    grid += cnta * q + cntb * p + p * q
    ans *= [grid, cnta, cntb, 1][2 * p + q]
    ans, grid = ans % MOD, grid - 1
    cnta, cntb = cnta + p, cntb + q
print(ans)
