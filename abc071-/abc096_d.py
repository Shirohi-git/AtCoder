class Eratosthenes():  # エラトステネスの篩
    def __init__(self, N):  # 素数リスト生成 O(n*log(log n))
        self.fact = [i for i in range(N + 1)]
        for i in range(2, int(N ** 0.5) + 1):
            if self.fact[i] < i:
                continue
            for j in range(i ** 2, N + 1, i):
                self.fact[j] = i
        self.prime = [i for i in range(2, N + 1) if i == self.fact[i]]

n = int(input())

prime = Eratosthenes(55555).prime
ans = [p for p in prime if p % 5 == 1]
print(*ans[:n])
