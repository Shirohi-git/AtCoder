from array import array


class Accumulate_2d:
    def __init__(self, n0, m0, lst_2d, k0):
        self.acc_2d = [array('H', [0] * (m0+1))]
        for i in range(n0):
            acc_1d = array('I', [0])
            for lij in lst_2d[i % k0] * 2:
                acc_1d.append(acc_1d[-1] + lij)
            self.acc_2d.append(acc_1d)
            for j in range(m0+1):
                self.acc_2d[i+1][j] += self.acc_2d[i][j]

    def query(self, sx, tx, sy, ty):
        ac2d = self.acc_2d
        res = ac2d[tx-1][ty-1] + ac2d[sx-1][sy-1]
        res -= ac2d[sx-1][ty-1] + ac2d[tx-1][sy-1]
        return res


def main():
    k2, k4 = 2*K, 4*K
    white = [array('H', [0] * k2) for _ in range(k2)]
    black = [array('H', [0] * k2) for _ in range(k2)]
    for _ in range(N):
        sx, sy, c = input().split()
        x, y = int(sx) % k2, int(sy) % k2
        mat = (white if c == 'W' else black)
        mat[x][y] += 1
    w_acc = Accumulate_2d(k4, k4, white, k2)
    b_acc = Accumulate_2d(k4, k4, black, k2)

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
