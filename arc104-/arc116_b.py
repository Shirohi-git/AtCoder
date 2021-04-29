n = int(input())
a = sorted(map(int, input().split()))
MOD9 = 998244353

ans, big = 0, 0
for i in range(n-1, -1, -1):
    big = (big + a[i]) % MOD9
    ans = (ans + a[i] * big) % MOD9
    big = 2 * big - a[i]
print(ans)
