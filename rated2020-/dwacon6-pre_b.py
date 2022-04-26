n = int(input())
x = list(map(int, input().split()))
MOD1 = 10**9 + 7

cnt = [1]
for i in range(n-2):
    cnt.append(cnt[-1] + pow(i+2, MOD1-2, MOD1))
fact = 1
for i in range(1, n):
    fact = fact * i % MOD1

ans = 0
for s, t, c in zip(x, x[1:], cnt):
    ans += (t-s) * c % MOD1
print(ans * fact % MOD1)
