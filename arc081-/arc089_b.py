from array import array


class Accumulate_2d:
    def __init__(self, n0, m0, k0):
        self.n, self.m, self.k = n0, m0, k0
        self.acc_2d = [array('I', [0] * (m0+1)) for _ in range(n0+1)]

    def update(self, x, y):
        x, y, k = x+1, y+1, self.k
        self.acc_2d[x][y] += 1
        self.acc_2d[x+k][y] += 1
        self.acc_2d[x][y+k] += 1
        self.acc_2d[x+k][y+k] += 1

    def accumulate(self):
        for i in range(self.n+1):
            for j in range(self.m):
                self.acc_2d[i][j+1] += self.acc_2d[i][j]
        for i in range(self.n):
            for j in range(self.m+1):
                self.acc_2d[i+1][j] += self.acc_2d[i][j]
        return

    def query(self, sx, tx, sy, ty):
        ac2d = self.acc_2d
        res = ac2d[tx-1][ty-1] + ac2d[sx-1][sy-1]
        res -= ac2d[sx-1][ty-1] + ac2d[tx-1][sy-1]
        return res


def main():
    k2, k4 = 2*K, 4*K
    w_acc = Accumulate_2d(k4, k4,  k2)
    b_acc = Accumulate_2d(k4, k4,  k2)
    for _ in range(N):
        sx, sy, c = input().split()
        x, y = int(sx) % k2, int(sy) % k2
        mat = (w_acc if c == 'W' else b_acc)
        mat.update(x, y)
    w_acc.accumulate(), b_acc.accumulate()

    ans = 0
    for i in range(1, k2+1):
        for j in range(1, k2+1):
            res = w_acc.query(i, i+K, j, j+K)
            res += w_acc.query(i+K, i+k2, j+K, j+k2)
            res += b_acc.query(i, i+K, j+K, j+k2)
            res += b_acc.query(i+K, i+k2, j, j+K)
            ans = max(res, ans)
    return print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())

    main()
