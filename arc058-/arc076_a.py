n, m = map(int, input().split())
mod = 10**9+7

fact = [1]
for i in range(1, max(n, m) + 1):
    fact.append(fact[-1] * i % mod)

if abs(n - m) >= 2:
    print(0)
elif abs(n - m) == 1:
    print(fact[n] * fact[m] % mod)
elif abs(n - m) == 0:
    print(2 * fact[n] * fact[m] % mod)
