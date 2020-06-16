from collections import Counter


def factorize(N):
    p = 2
    PRIME = []
    while p * p <= N:
        if N % p == 0:
            N //= p
            PRIME.append(p)
        else:
            p += 1
    if N > 1:
        PRIME.append(N)
    return Counter(PRIME)


n = int(input())

prime = factorize(n)
ans = 0
for i in prime:
    for j in range(1, prime[i] + 1):
        if n % i ** j == 0:
            n //= i ** j
            ans += 1
print(ans)
