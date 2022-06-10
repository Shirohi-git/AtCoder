class Eratosthenes():  # エラトステネスの篩
    def __init__(self, N):  # 素数リスト生成 O(n*log(log n))
        self.fact = [i for i in range(N + 1)]
        for i in range(2, int(N ** 0.5) + 1):
            if self.fact[i] < i:
                continue
            for j in range(i ** 2, N + 1, i):
                self.fact[j] = i
        self.prime = set(i for i in range(2, N + 1) if i == self.fact[i])


q = int(input())
lr = [list(map(int, input().split())) for _ in range(q)]

p = Eratosthenes(10 ** 5).prime
acc = [0]
for i in range(1, 10 ** 5, 2):
    tmp = (i in p) and ((i + 1) // 2 in p)
    acc.append(acc[-1] + tmp)

for l, r in lr:
    ans = acc[r // 2 + 1] - acc[l // 2]
    print(ans)
