n = int(input())
d = list(map(int, input().split()))
MOD = 998244353

cnt = [0] * n
for di in d:
    cnt[di] += 1

ans = (d[0] == 0 and cnt[0] == 1)
for i in range(1, n):
    ans *= pow(cnt[i - 1], cnt[i], MOD)
    ans %= MOD
print(ans)
