class Eratosthenes():
    def __init__(self, N):
        self.fact = [i for i in range(N + 1)]
        for i in range(2, int(N ** 0.5) + 1):
            if self.fact[i] < i:
                continue
            for j in range(i ** 2, N + 1, i):
                self.fact[j] = i
        self.prime = [i for i in range(2, N + 1) if i == self.fact[i]]

    def factor(self, NUM):
        PRIME = []
        while NUM > 1:
            PRIME.append(self.fact[NUM])
            NUM //= self.fact[NUM]
        return len(PRIME) + 1


n = int(input())

era = Eratosthenes(n)
ans = [1]
for i in range(n - 1):
    ans.append(era.factor(i + 2))
print(*ans)
