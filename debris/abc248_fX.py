class Enumeration:
    def __init__(self, N, MOD):
        self.mod = MOD
        self.FACT = [1, 1]
        self.INV = [0, 1]
        self.FACTINV = [1, 1]
        for i in range(2, N + 1):
            self.FACT.append((self.FACT[-1] * i) % self.mod)
            self.INV.append(pow(i, self.mod - 2, self.mod))
            self.FACTINV.append((self.FACTINV[-1] * self.INV[-1]) % self.mod)

    def combination(self, N, R):
        if (R < 0) or (N < R):
            return 0
        R = min(R, N - R)
        div = self.FACTINV[R] * self.FACTINV[N-R] % self.mod
        return self.FACT[N] * div % self.mod


def main():
    # なんとなくとりあえず最小全域木の数を求めてみた
    # 使わなかった辺の数を数えてDP, これが二乗の源泉っぽいな？
    # 実装するには残り時間が足りない。

    cmb = 1, 1
    for _ in range(2, N+1):
        b_ok, b_ng = cmb
        ok = (b_ok * 3 + b_ng) % P
        ng = (b_ok * 2 + b_ng) % P
        cmb = ok, ng

    enu = Enumeration(3*N, P)
    ans = []
    for i in range(1, N):
        cnt = enu.combination((3*N-2) - (2*N-1), i)
        ans.append(ok * cnt % P)
    return print(*ans)


if __name__ == '__main__':
    N, P = map(int, input().split())

    main()
