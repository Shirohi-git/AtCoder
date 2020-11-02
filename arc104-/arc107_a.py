abc = list(map(int, input().split()))
MOD = 998244353

a, b, c = (i * (i + 1) for i in abc)
print(a * b * c // 8 % MOD)
