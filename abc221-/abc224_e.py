class data:
    def __init__(self, size):
        self.d_1st = [(-1, INF)] * size
        self.d_2nd = [-1] * size

    def get(self, idx, num):
        res = self.d_2nd[idx]
        if num < self.d_1st[idx][1]:
            res = max(res, self.d_1st[idx][0])
        return res

    def update(self, idx, num, cnt):
        bfo = self.d_1st[idx]
        if num < bfo[1]:
            self.d_2nd[idx] = bfo[0]
        self.d_1st[idx] = max((cnt, num), bfo)
        return


def main():
    s_rca = sorted(enumerate(RCA), key=lambda x: x[1][2])
    row, col = data(H), data(W)
    ans = [-1] * N

    for i, (ri, ci, ai) in s_rca[::-1]:
        ans[i] = max(row.get(ri-1, ai), col.get(ci-1, ai)) + 1
        row.update(ri-1, ai, ans[i]), col.update(ci-1, ai, ans[i])
    return print(*ans, sep='\n')


if __name__ == '__main__':
    H, W, N = map(int, input().split())
    RCA = [list(map(int, input().split())) for _ in range(N)]
    INF = 10**10

    main()
