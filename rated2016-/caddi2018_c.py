from collections import defaultdict


def factorize(N):
    P = 2
    PRIME = defaultdict(int)
    while P ** 2 <= N:
        if N % P == 0:
            N //= P
            PRIME[P] += 1
        else:
            P += 1
    if N > 1:
        PRIME[N] += 1
    return PRIME


n, p = map(int, input().split())

prime = factorize(p)
ans = 1
for j in prime:
    if prime[j] >= n:
        ans *= j ** (prime[j] // n)
print(ans)
