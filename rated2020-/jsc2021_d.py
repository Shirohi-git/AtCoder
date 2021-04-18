n, p = map(int, input().split())
MOD1 = 10**9 + 7

ans = (p - 1) * pow(p - 2, n - 1, MOD1)
print(ans % MOD1)
