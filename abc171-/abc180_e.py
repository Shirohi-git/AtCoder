class TSP():
    def __init__(self, n, xyz):
        self.n, self.v = n, xyz
        self.memo = [[-1] * (1 << n) for _ in range(n)]

    def dist(self, x, y):
        (a, b, c), (p, q, r) = self.v[x], self.v[y]
        return abs(p - a) + abs(b - q) + max(0, r - c)

    def tspdp(self, s, bit):
        if bit == (1 << self.n) - 1:
            self.memo[s][bit] = self.dist(s, 0)
            return self.dist(s, 0)

        res = float('inf')
        for t in range(self.n):
            if (bit >> t) & 1:
                continue
            nxt = bit + (1 << t)
            if self.memo[t][bit] == -1:
                self.memo[t][bit] = self.tspdp(t, nxt)
            tmp = self.dist(s, t) + self.memo[t][bit]
            res = min(res, tmp)
        return res


n = int(input())
xyz = [list(map(int, input().split())) for _ in range(n)]

tsp = TSP(n, xyz)
print(tsp.tspdp(0, 1))
