from math import gcd


def eratosthenes(n):
    prime = []
    data = [i for i in range(2, n + 1)]
    while True:
        p = data[0]
        if n <= p ** 2:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]
    return data


def factorize(N):  # 素因数分解
    prime = set()
    for p in prime_list:
        if p * p > N:
            break
        while N % p == 0:
            N //= p
            prime.add(p)
    if N > 1:
        prime.add(N)
    return prime


n = int(input())
a = list(map(int, input().split()))

ans = 0
for ai in a:
    ans = gcd(ans, ai)
if ans != 1:
    print('not coprime')
    exit()

prime_list = eratosthenes(max(a))
num = set()
for ai in a:
    prime = factorize(ai)
    if len(prime & num) > 0:
        print('setwise coprime')
        break
    num |= prime
else:
    print('pairwise coprime')
