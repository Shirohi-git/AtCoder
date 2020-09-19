from collections import Counter

class Eratosthenes():  # エラトステネスの篩
    def __init__(self, N):  # 素数リスト生成 O(n*log(log n))
        self.fact = [i for i in range(N + 1)]
        for i in range(2, int(N ** 0.5) + 1):
            if self.fact[i] < i:
                continue
            for j in range(i ** 2, N + 1, i):
                self.fact[j] = i
        self.prime = [i for i in range(2, N + 1) if i == self.fact[i]]

    def factor(self, NUM):  # 高速素因数分解 O(log num)
        PRIME = []
        while NUM > 1:
            PRIME.append(self.fact[NUM])
            NUM //= self.fact[NUM]
        return Counter(PRIME)

n = int(input())

era = Eratosthenes(n)
ans = 0
for i in range(1, n):
    tmp = 1
    for num in era.factor(i).values():
        tmp *= num + 1
    ans += tmp
print(ans)
