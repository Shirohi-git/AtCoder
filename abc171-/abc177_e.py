from math import gcd


class Eratosthenes():  # エラトステネスの篩
    def __init__(self, N):  # 素数リスト生成 O(n*log(log n))
        self.fact = [i for i in range(N + 1)]
        for i in range(2, int(N**0.5) + 1):
            if self.fact[i] < i:
                continue
            for j in range(i ** 2, N + 1, i):
                self.fact[j] = i

    def factor(self, NUM):  # 高速素因数分解 O(log num)
        PRIME = set()
        while NUM > 1:
            PRIME.add(self.fact[NUM])
            NUM //= self.fact[NUM]
        return PRIME


n = int(input())
a = list(map(int, input().split()))

ans = 0
for ai in a:
    ans = gcd(ans, ai)
if ans != 1:
    print('not coprime')
    exit()

era = Eratosthenes(max(a))
num = set()
for ai in a:
    prime = era.factor(ai)
    if len(prime & num) > 0:
        print('setwise coprime')
        break
    num |= prime
else:
    print('pairwise coprime')
