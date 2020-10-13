t = int(input())
nab = [list(map(int, input().split())) for _ in range(t)]
MOD = 10 ** 9 + 7

for n, a, b in nab:
    mab = n - a - b
    cmb = (mab + 2) * (mab + 1) * (mab >= 0) % MOD
    ans = 2 * (n - a + 1) * (n - b + 1) % MOD
    print((ans - cmb) * cmb % MOD)
