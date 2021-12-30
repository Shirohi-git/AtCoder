class TSP():
    def __init__(self, n0):
        self.n = n0
        self.memo = [[-1] * (1 << n0) for _ in range(n0)]
        self.dist = A

    def tspdp(self, s=0, bit=1):
        if bit == (1 << self.n) - 1:
            self.memo[s][bit] = self.dist[s][0]
            return self.dist[s][0]

        res = float('inf')
        for t in range(self.n):
            if (bit >> t) & 1:
                continue
            nxt = bit + (1 << t)
            if self.memo[t][bit] == -1:
                self.memo[t][bit] = self.tspdp(t, nxt)
            tmp = self.dist[s][t] + self.memo[t][bit]
            res = min(res, tmp)
        return res


def main():
    return print(TSP(N).tspdp())


if __name__ == '__main__':
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    main()
