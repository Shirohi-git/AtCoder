from collections import defaultdict


def factorize(N):  # 素因数分解
    p = 2 
    while p * p <= N:
        while N % p == 0:
            N //= p
            fact[p] += 1
        p += 1
    if N > 1:
        fact[N] += 1

n = int(input())

fact = defaultdict(int)
for i in range(n):
    factorize(i + 1)

cnt = {2: 0, 4: 0, 14: 0, 24: 0, 74: 0}
for vfact in fact.values():
    for i in cnt:
        cnt[i] += (vfact >= i)

ans = cnt[4] * (cnt[4] - 1) * (cnt[2] - 2) // 2
ans += cnt[24] * (cnt[2] - 1) + cnt[14] * (cnt[4] - 1) + cnt[74]
print(ans)
