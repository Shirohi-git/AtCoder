from collections import defaultdict


def factorize(N):  # 素因数分解
    p = 2
    while p * p <= N:
        if N % p == 0:
            N //= p
            d[p] += 1
        else:
            p += 1
    if N > 1:
        d[N] += 1
    return



n = int(input())
mod = 10 ** 9 + 7

d = defaultdict(int)
for i in range(1, n + 1):
    factorize(i)

ans = 1
for cnt in d.values():
    ans = ans * (cnt + 1) % mod
print(ans)
