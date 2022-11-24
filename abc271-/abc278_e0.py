from collections import Counter


class Accumulate_2d:
    def __zip(self, x, y):
        return x*(W+1) + y

    def __init__(self, num):
        self.acc_2d = [0] * (W+1)
        ac2d = self.acc_2d
        for i in range(H):
            ac2d.append(0)
            for j in range(W):
                ac2d.append(ac2d[-1] + (A[i][j] == num))
            for j in range(W+1):
                ac2d[self.__zip(i+1, j)] += ac2d[self.__zip(i, j)]

    def query(self, sx, sy):
        tx, ty = sx+P, sy+Q
        ac2d = self.acc_2d
        res = ac2d[self.__zip(tx-1, ty-1)] + ac2d[self.__zip(sx-1, sy-1)]
        res -= ac2d[self.__zip(sx-1, ty-1)] + ac2d[self.__zip(tx-1, sy-1)]
        return res


def main():
    cnt = Counter(aij for ai in A for aij in ai)
    acc2d = {}
    for a in cnt:
        acc2d[a] = Accumulate_2d(a)

    for i in range(H-P+1):
        ans = []
        for j in range(W-Q+1):
            res = len(cnt)
            for a, v in cnt.items():
                res -= (v == acc2d[a].query(i+1, j+1))
            ans.append(res)
        print(*ans)
    return


if __name__ == '__main__':
    H, W, N, P, Q = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    main()
